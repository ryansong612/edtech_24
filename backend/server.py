from flask import Flask, request
from vector_database import Db
from embed_model import Model, calculate_similarity

app = Flask(__name__)
db = Db()
model = Model()
marked_sheets = {}
tags = ["Object Oriented Programming", "Functional Programming", "Data Structures", "Algorithms",
        "Operating Systems", "Compilers", "Databases",
        "Web Development", "Machine Learning", "Networks and Communication",
        "Natural Language Processing", "Reinforcement Learning", "Robotics",
        "Deep Learning", "Mathematics and Computer Science"]


def initialize_database():
    db.set_index("qtags")
    for tag in tags:
        tag_vector = model.generate_embeddings([tag])
        db.upsert([{
            "id": tag,
            "values": tag_vector
        }], namespace="tags")
    print("Database initialized")
    return


@app.route("/add-student", methods=["POST"])
def add_student():
    try:
        db.set_index("student")
        student_json = request.get_json()
        student_name = student_json["name"]
        db.upsert([{
            "id": student_name,
            "values": [0.01 for _ in range(len(tags))],
        }], namespace="students")
        return {"status": "success"}

    except Exception as e:
        print(e)
        return {"status": "failure"}


@app.route("/add-question", methods=["POST"])
def add_question():
    """
    Takes a question, embeds it and adds it to the database

    question: String, answer: String, difficulty: int, type: String, tags: Optional<Array<String>>
    """
    try:
        db.set_index("qtags")
        question_json = request.get_json()
        question_text = question_json["question"]
        question_type = question_json["type"]
        if question_type == "Short Answer":
            question_embedding = model.generate_embeddings([question_text, question_json["answer"]])
        elif question_type == "MCQ":
            everything = [question_json["answer"][option] for option in question_json["answer"]]
            everything.append(question_text)
            question_embedding = model.generate_embeddings(everything)

        metadata = {key: question_json[key] for key in question_json if key != "question"}

        print(len(question_embedding))
        print(metadata)

        metadata["tags"] = question_tags(question_embedding)
        print(metadata["tags"])
        db.upsert([{
            "id": question_text,
            "values": question_embedding,
            "metadata": metadata
        }], namespace="questions")

        return {"status": "success"}

    except Exception as e:
        print(e)
        return {"status": "failure"}


@app.route("/mark-sheet", methods=["POST"])
def mark_sheet():
    """
    Takes a request containing a homework sheet containing multiple questions.s
    Determines if each is correct/incorrect.
    Uses vector embedding of question to fetch questions from db to recommend

    Sheet is:
    name: student name,
    questions: [question-id: String, user-answer: String]
    """
    db.set_index("qtags")
    response_json = {"questions": []}
    sheet = request.get_json()
    student_name = sheet["name"]
    for question in sheet["questions"]:
        question_text = question["question"]
        user_answer = question["user-answer"]
        fetched_result = db.query(namespace="questions",
                                  top_k=10,
                                  id=question_text)
        metadata = fetched_result['matches'][0]['metadata']
        question_vector = fetched_result['matches'][0]['values']
        correct_answer = metadata['answer']
        question_type = metadata['type']
        incorrect = 0
        if question_type == "MCQ":
            if user_answer == correct_answer:
                question["status"] = "correct"
            else:
                question["status"] = "incorrect"
                incorrect = 1
        elif question_type == "Short Answer":
            user_answer_embedding = model.generate_embeddings([user_answer])
            correct_answer_embedding = model.generate_embeddings([correct_answer])
            similarity = calculate_similarity(user_answer_embedding, correct_answer_embedding)
            threshold = 0.7
            print(similarity)
            if similarity > threshold:
                question["status"] = "correct"
            else:
                question["status"] = "incorrect"
                incorrect = 1
            question["score"] = similarity
        update_student_portfolio(student_name, question_vector, incorrect)
        response_json["questions"].append(question)

    marked_sheets[student_name] = response_json
    print(recommend_tags(student_name, 5))
    return response_json
    # except Exception as e:
    #     print(f"{e}")
    #     return {"status": "failure"}


@app.route("/generate-sheet", methods=["POST"])
def generate_sheet():
    request_json = request.get_json()
    student_name = request_json["name"]
    recommended_tags = recommend_tags(student_name, 5)
    sheet_questions = []

    for tag in recommended_tags:
        fetched_result = db.query(namespace="qtags", id=tag, top_k=1)
        tag_vector = fetched_result['matches'][0]['values']
        similar_questions = db.query(namespace="questions",
                                     top_k=10,
                                     vector=tag_vector)["matches"]

        for question in similar_questions:
            sheet_questions.append(question)

    return {
        "name": student_name,
        "questions": sheet_questions
    }


def update_student_portfolio(student_name: str, question_vector: list[float], incorrect: int):
    db.set_index("student")
    fetched_result = db.query(namespace="students", top_k=1, id=student_name)
    student_vector = fetched_result['matches'][0]['values']
    past_decay = 0.3
    similarity_vector = question_tag_similarity(question_vector)
    updated_vector = [float(past_decay * student_vector[i]
                      - (-1 ** incorrect) * (1.0 - past_decay) * similarity_vector[i])
                      for i in range(len(student_vector))]
    student_json = [{
        "id": student_name,
        "values": updated_vector
    }]
    db.set_index("student")
    db.upsert(student_json, namespace="students")
    return


def question_tag_similarity(question_vector: list[float]):
    db.set_index("qtags")
    res = [0.0 for _ in range(len(tags))]
    for i, tag in enumerate(tags):
        fetched_result = db.query(namespace="tags", id=tag, top_k=1)
        tag_vector = fetched_result['matches'][0]['values']
        res[i] = calculate_similarity(question_vector, tag_vector)
    return res


def recommend_tags(student_name: str, top_k: int) -> list[str]:
    db.set_index("student")
    fetched_result = db.query(namespace="students", top_k=1, id=student_name)
    student_vector = fetched_result['matches'][0]['values']
    student_tag_vector = [[student_vector[i], tags[i]] for i in range(len(tags))]
    student_tag_vector.sort(key=lambda x: x[0], reverse=True)
    return [tag for _, tag in student_tag_vector[:top_k]]


def question_tags(question_vector: list[float]) -> list[str]:
    db.set_index("qtags")
    fetched_result = db.query(namespace="tags",
                              top_k=len(tags),
                              include_values=False,
                              vector=question_vector)
    matches = fetched_result['matches']
    valid_tags = []
    match_threshold = 0.45
    for match in matches:
        print(match)
        if match['score'] > match_threshold:
            valid_tags.append(match['id'])
    return valid_tags


if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)

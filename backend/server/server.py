from flask import Flask, request
from flask_cors import CORS, cross_origin
from vector_database import Db
from embed_model import Model, calculate_similarity

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
db = Db()
model = Model()
tags = ["Object Oriented Programming", "Functional Programming", "Data Structures", "Algorithms",
        "Operating Systems", "Compilers", "Databases",
        "Web Development", "Machine Learning", "Networks and Communication",
        "Natural Language Processing", "Reinforcement Learning", "Robotics",
        "Deep Learning", "Mathematics and Computer Science"]
seen_questions = {}
assigned = {}
assignments = {}


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


def unassign(student_name: str):
    del assigned[student_name]
    return


def assign(student_name: str, questions: list[dict]):
    assignments[student_name] = questions
    assigned[student_name] = True
    return


@app.route("/assignment-status", methods=["POST"])
def assignment_status():
    student_json = request.get_json()
    student_name = student_json["name"]
    if student_name not in assigned and student_name not in assignments:
        return {"status": "unassigned"}
    if student_name not in assigned and student_name in assignments:
        return {"status": "marked"}
    else:
        return {"status": "assigned"}


@app.route("/assign-to", methods=["POST"])
def assign_to():
    assignment_json = request.get_json()
    student_name = assignment_json["name"]
    questions = assignment_json["questions"]
    assign(student_name, questions)
    return {"status": "success"}


@app.route("/get-assignment", methods=["POST"])
def get_assignment():
    assignment_json = request.get_json()
    student_name = assignment_json["name"]
    questions = ""
    if student_name in assignments:
        # could either be marked or unmarked
        questions = assignments[student_name]
    return {"questions": questions}


@app.route("/add-student", methods=["POST"])
def add_student():
    student_json = request.get_json()
    student_name = student_json["name"]
    return add(student_name)


def add(name: str):
    db.set_index("student")
    db.upsert([{
        "id": name,
        "values": [0.01 for _ in range(len(tags))],
    }], namespace="students")
    return {"status": "success"}


@app.route("/get-questions", methods=["GET", "POST"])
@cross_origin()
def get_questions():
    db.set_index("qtags")
    fetched_result = db.query(vector=[0 for _ in range(512)],
                              namespace="questions",
                              top_k=100)
    res = []
    for match in fetched_result['matches']:
        r = {'question': match['id'], 'answer': match['metadata']['answer'],
             'type': match['metadata']['type']}
        res.append(r)
    print(res)
    return {"questions": res}


@app.route("/add-questions", methods=["POST"])
def add_questions():
    """
    Takes a question, embeds it and adds it to the database

    question: String, answer: String, difficulty: int, type: String, tags: Optional<Array<String>>
    """
    db.set_index("qtags")
    questions_json = request.get_json()
    questions = questions_json["questions"]
    print(questions_json)
    new_vectors = []
    for question_json in questions:
        question_text = question_json["question"]
        question_type = question_json["type"]
        if question_type == "Short Answer":
            question_embedding = model.generate_embeddings(
                [question_text, question_json["answer"]])
        elif question_type == "MCQ":
            everything = [question_json["answer"][option] for option in question_json["answer"]]
            everything.append(question_text)
            question_embedding = model.generate_embeddings(everything)

        metadata = {key: question_json[key] for key in question_json if key != "question"}

        metadata["tags"] = question_tags(question_embedding)
        print(f"{question_text} {metadata['tags']}")
        if metadata["tags"]:
            new_vectors.append({
                "id": question_text,
                "values": question_embedding,
                "metadata": metadata
            })
    db.upsert(new_vectors, namespace="questions")
    return new_vectors


@app.route("/generate-questions", methods=["POST"])
def generate_questions():
    """
    Takes a request containing a list of tags and returns a list of questions
    """
    db.set_index("qtags")
    request_json = request.get_json()
    tag = request_json["tag"]
    top_k = request_json["top_k"]
    questions = []
    fetched_result = db.query(namespace="questions",
                              vector=[0 for _ in range(512)],
                              metadata_filter={"tags": tag},
                              top_k=top_k)
    for match in fetched_result['matches']:
        questions.append({
            "question": match['id'],
            "answer": match['metadata']['answer'],
            "type": match['metadata']['type']
        })
    return {"questions": questions}


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
    response_json = {"questions": []}
    sheet = request.get_json()
    student_name = sheet["name"]
    # clear cache
    seen_questions[student_name] = []
    for question in sheet["questions"]:
        db.set_index("qtags")
        question_text = question["question"]
        user_answer = question["user-answer"]
        # add to cache
        seen_questions[student_name].append(question_text)
        fetched_result = db.query(namespace="questions",
                                  top_k=1,
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
            threshold = 0.625
            print(similarity)
            if similarity > threshold:
                question["status"] = "correct"
            else:
                question["status"] = "incorrect"
                incorrect = 1
            question["score"] = similarity
        update_student_portfolio(student_name, question_vector, incorrect)
        response_json["questions"].append(question)
    # returns the marked sheet
    unassign(student_name)
    assignments[student_name] = response_json
    return response_json


@app.route("/generate-sheet", methods=["POST"])
def generate_sheet():
    request_json = request.get_json()
    student_name = request_json["name"]
    recommended_tags = recommend_tags(student_name, 15)
    sheet_questions = []

    # 2 questions for usually failing topics, 2 questions for second most, and 1 for unseen
    tags_wanted = [recommended_tags[0], recommended_tags[1], recommended_tags[-1]]
    for i, tag in enumerate(tags_wanted):
        db.set_index("qtags")
        fetched_result = db.query(namespace="tags", id=tag, top_k=1)
        tag_vector = fetched_result['matches'][0]['values']
        similar_questions = db.query(namespace="questions",
                                     top_k=50,
                                     vector=tag_vector,
                                     include_values=False)["matches"]
        cap = 2 if i < 2 else 1
        for question in similar_questions:
            if cap <= 0:
                break
            if student_name not in seen_questions \
                    or question['id'] not in seen_questions[student_name]:
                sheet_questions.append({
                    "question": question['id'],
                    "answer": question['metadata']['answer'],
                    "type": question['metadata']['type']
                })
                cap -= 1
        for question in similar_questions:
            if cap <= 0:
                break
            if student_name not in seen_questions or question not in sheet_questions:
                sheet_questions.append({
                    "question": question['id'],
                    "answer": question['metadata']['answer'],
                    "type": question['metadata']['type']
                })
                cap -= 1
    res = {
        "name": student_name,
        "questions": sheet_questions
    }
    seen_questions[student_name] = [question["question"] for question in sheet_questions]
    assign(student_name, sheet_questions)
    return res


def update_student_portfolio(student_name: str, question_vector: list[float], incorrect: int):
    db.set_index("student")
    fetched_result = db.query(namespace="students", top_k=1, id=student_name)
    student_vector = fetched_result['matches'][0]['values']
    past_decay = 0.3
    similarity_vector = question_tag_similarity(question_vector)
    updated_vector = [float(past_decay * student_vector[i]
                            - (-1 ** incorrect) * (1.0 - past_decay) * abs(similarity_vector[i]))
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
    fetched_result = db.query(namespace="students", top_k=50, id=student_name)
    if not fetched_result['matches']:
        add(student_name)
        return recommend_tags(student_name, top_k)
    for match in fetched_result['matches']:
        if match['id'] == student_name:
            student_vector = fetched_result['matches'][0]['values']
            student_tag_vector = [[student_vector[i], tags[i]] for i in range(len(tags))]
            student_tag_vector.sort(key=lambda x: x[0], reverse=True)
            return [tag for _, tag in student_tag_vector[:top_k]]
    return []


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
        if match['score'] > match_threshold:
            valid_tags.append(match['id'])
    return valid_tags


if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)

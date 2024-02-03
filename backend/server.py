from flask import Flask, request
from vector_database import Db
from embed_model import Model, calculate_similarity

app = Flask(__name__)
db = Db()
model = Model()


@app.route("/add-question", methods=["POST"])
def add_question():
    """
    Takes a question, embeds it and adds it to the database

    question: String, answer: String, difficulty: int, tags: Optional<Array<String>>
    """
    try:
        question_json = request.get_json()
        question_text = question_json["question"]
        question_embedding = model.generate_embeddings([question_text])

        metadata = {key: question_json[key] for key in question_json if key != "question"}

        print(len(question_embedding))
        print(question_embedding)
        print(metadata)

        db.upsert([{
            "id": question_text,
            "values": question_embedding,
            "metadata": metadata
        }], namespace="questions")

        return {"status": "success"}
    
    except Exception as e:
        print(e)
        return {"status": "failure"}


@app.route("/read-hw-sheet", methods=["POST"])
def read_hw_sheet():
    """
    Takes a request containing a homework sheet containing multiple questions.s
    Determines if each is correct/incorrect.
    Uses vector embedding of question to fetch questions from db to recommend
    """
    pass


if __name__ == "__main__":
    app.run(debug=True)

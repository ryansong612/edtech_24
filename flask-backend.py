from flask import Flask
from vector_database import Db

app = Flask(__name__)
DB = Db()

@app.route("/add-question", methods=["POST"])
def add_question(request):
    """
    Takes a question, embeds it and adds it to the database
    """
    pass

@app.route("/read-hw-sheet", methods=["POST"])
def read_hw_sheet(request):
    """
    Takes a request containing a homework sheet containing multiple questions.s
    Determines if each is correct/incorrect.
    Uses vector embedding of question to fetch questions from db to recommend
    """
    pass

if __name__ == "__main__":
    app.run()
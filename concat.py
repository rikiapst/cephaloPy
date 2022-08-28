from flask import Flask, request
import json
app = Flask(__name__)


@app.route("/concat", methods=["POST"])
def distance():
    print(request.data)
    words = json.loads(request.data)

    word1 = words["word1"]
    word2 = words["word2"]

    new_word = word1 + word2
    new_word = new_word * 3

    brian = {"results": [word1, word2]}
    return brian

from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route("/")
def hello():
    app.logger.info(("name is: {}".format(app.name)))
    return redirect("home")


@app.route("/home/", methods=['GET', 'POST'])
def homepage(name=None):
    if request.method == "POST":
        words = request.form["nm"]
        return redirect(url_for("getClues", words=words))
    else:
        return render_template(
            "home.html"
        )


@app.route('/getClues/<words>')
def getClues(words: str):
    return "The words are: {}".format(words.split(','))


if __name__ == "__main__":
    app.run(host="0.0.0.0",  debug=True, port=5000)

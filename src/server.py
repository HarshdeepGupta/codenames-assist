from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = "hello"


@app.route("/")
def hello():
    app.logger.info(("name is: {}".format(app.name)))
    return redirect("home")


@app.route("/home/", methods=['GET', 'POST'])
def homepage(name=None):
    if request.method == "POST":
        words = request.form["nm"]
        if len(words):
            session["words"] = words
        return redirect(url_for("getClues"))
    else:
        return render_template(
            "home.html"
        )


@app.route('/getClues')
def getClues():
    if "words" in session:
        words = session['words']
        return "The words are: {}".format(words.split(','))
    else:
        return redirect("home")


if __name__ == "__main__":
    app.run(host="0.0.0.0",  debug=True, port=5000)

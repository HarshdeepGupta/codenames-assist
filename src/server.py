from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session
from config import config
from Logger import Logger
app = Flask(__name__)
app.config.from_object(config)
logger = Logger(app)



@app.route("/")
def hello():
    logger.log(("name is: {}".format(app.name)))
    return redirect("home")


@app.route("/home/", methods=['GET', 'POST'])
def homepage():
    return render_template(
        "home.html"
    )


@app.route('/results', methods=["POST"])
def results():
    listOfWords: str = request.form.get("listOfWords")
    results = listOfWords.split(",")
    return render_template("results.html", results=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0",  debug=True, port=5000)

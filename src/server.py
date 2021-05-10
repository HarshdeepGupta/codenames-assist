from datetime import datetime
from flask import Flask, render_template
server = Flask(__name__)


@server.route("/")
def hello():
    return "Hello World!"


@server.route("/home/")
def hello_there(name=None):
    server.logger.error("THis is it")
    return render_template(
        "home.html"
    )


if __name__ == "__main__":
    server.run(host="0.0.0.0",  debug=True, port=5000)

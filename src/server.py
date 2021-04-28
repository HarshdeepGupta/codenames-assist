from flask import Flask, render_template
server = Flask(__name__)
from datetime import datetime

@server.route("/")
def hello():
   return "Hello World!"


@server.route("/hello/")
@server.route("/hello/<name>")
def hello_there(name = None):
    server.logger.error("THis is it")
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

if __name__ == "__main__":
   server.run(host='0.0.0.0')
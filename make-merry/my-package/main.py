from flask import Flask

app = Flask(__name__)


@app.route("/")
def greet():
    return "vanakkam vaiyyagame!"


if __name__ == "__main__":
    app.run()
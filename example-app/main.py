from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World from Docker!"


@app.route("/monitoring/healthcheck")
def healthcheck():
    return "I'm ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

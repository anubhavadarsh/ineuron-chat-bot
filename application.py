from flask import Flask, jsonify, request
from model2 import ask_question
from flask_cors import CORS, cross_origin

# init app


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config["Content-Type"] = "application/json"

    @app.route("/")
    def hello():
        return "hello world"

    @app.route("/api/kira", methods=["POST"])
    def send():
        jn = request.json
        ans = ask_question(jn["question"])
        return jsonify(ans)

    return app

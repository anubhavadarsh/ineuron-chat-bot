from flask import Flask

# init app
def create_app():
    app = Flask(__name__)

    @app.route("/hello")
    def hello():
        return "hello, world!"

    return app

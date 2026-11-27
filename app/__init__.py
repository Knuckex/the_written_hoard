from flask import Flask
from .routes import root_bp
from .services.apis.ApiClient import ApiClient


def create_app():
    app = Flask(__name__)

    app.register_blueprint(root_bp)
    app.config.from_object("config.Config")

    app.extensions["open_library_api"] = ApiClient(
        app.config["OPEN_LIBRARY_BASE_URL"],
        headers={"User-Agent": "bfmlvl6cw1"}
    )

    app.extensions["poetrydb_api"] = ApiClient(
        app.config["POETRYDB_BASE_URL"]
    )

    return app
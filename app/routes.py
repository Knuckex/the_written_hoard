import re
from .services.apis.google_books import *

from flask import Blueprint, render_template, request, current_app
from datetime import datetime
from flask import render_template



root_bp = Blueprint("root", __name__)

@root_bp.route("/")
def home_page():
    return render_template("home.html")


@root_bp.route("/api")
def api_page():
    response = get_volumes(
        str(current_app.config["GOOGLE_BOOKS_API_BASE_URL"]),
        str(current_app.config["GOOGLE_BOOKS_API_KEY_SUFFIX"])
        )
    return render_template(
        "api.html",
        response=response
        )


@root_bp.route("/hello/")
@root_bp.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )
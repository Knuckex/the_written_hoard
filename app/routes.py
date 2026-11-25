import re

from flask import Blueprint, render_template, request
from datetime import datetime
from flask import render_template


root_bp = Blueprint("root", __name__)

@root_bp("/")
def home_page():
    return render_template("home.html")


@root_bp("/api")
def api_page():
    return "Henlo"


@root_bp("/hello/")
@root_bp("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )
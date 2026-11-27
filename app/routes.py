import re
import pandas as pd
import json


from .services.apis.ApiClient import *
from .services.apis.helpers.open_library import *

from flask import Blueprint, render_template, request, current_app
from datetime import datetime
from flask import render_template



root_bp = Blueprint("root", __name__)

@root_bp.route("/")
def home_page():
    return render_template("home.html")


@root_bp.route("/api")
def api_page():
    api_response = search_authors("Clive Cussler")
    #normalised_response = pd.json_normalize(api_response["docs"][0])
    #print(normalised_response.to_string())
    
    return render_template(
        "api.html",
        response=api_response
        )


@root_bp.route("/hello/")
@root_bp.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )
import re
import pandas as pd
import json
import base64
import io

from flask import Blueprint, render_template, request, current_app
from datetime import datetime
from flask import render_template
from matplotlib.figure import Figure

from .services.apis.ApiClient import *
from .services.apis.helpers.open_library import *
from .services.visualisation.open_library import *


root_bp = Blueprint("root", __name__)

@root_bp.route("/")
def home_page():
    return render_template("home.html")


@root_bp.route("/api")
def api_page():
    api_response = search_authors("Clive Cussler")
    author_name = "Clive Cussler"
    author_pie_chart = create_author_pie_chart(api_response)

    buf = io.BytesIO()
    author_pie_chart.savefig(buf, format="png")
    chart_data = base64.b64encode(buf.getvalue()).decode("ascii")

    
    return render_template(
        "api.html",
        response=api_response,
        author_name=author_name,
        pie_chart=chart_data
        )


@root_bp.route("/hello/")
@root_bp.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )
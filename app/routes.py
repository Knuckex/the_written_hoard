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

from .services.apis.helpers.poetrydb import *

root_bp = Blueprint("root", __name__)

@root_bp.route("/")
def home_page():
    return render_template("home.html")


@root_bp.route("/api")
def create_open_library_api_page():
    api_response = search_authors("Clive Cussler")
    author_name = "Clive Cussler"
    author_pie_chart = create_author_pie_chart(api_response)

    buf = io.BytesIO()
    author_pie_chart.savefig(buf, format="png")
    chart_data = base64.b64encode(buf.getvalue()).decode("ascii")

    return render_template(
        "open_library_api.html",
        response=api_response,
        author_name=author_name,
        pie_chart=chart_data
        )

@root_bp.route("/api/poetrydb")
def create_poetrydb_api_page():

    response_list = None
    
    try:
        api_response_1 = search_poets("Emily Dickinson")
        api_response_2 = search_poets("Samuel Taylor Coleridge")
        api_response_3 = search_poets("William Wordsworth")
        response_list = [api_response_1, api_response_2, api_response_3]

    except ApiError as e:
        print(e)

    if response_list is not None:
        merged_responses = append_poet_data(response_list)


        return render_template(
            "poetrydb_api.html",
            response=merged_responses
        )
    else:
        return render_template(
            "poetrydb_api.html"
            )


@root_bp.route("/hello/")
@root_bp.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )
from flask import current_app
import pandas as pd

def search_poets(poet: str):
    """Search poets by name, return details as a dataframe"""

    api = current_app.extensions["poetrydb_api"]
    data = api.get_json(
        f"{current_app.config["POETRYDB_AUTHOR_SEARCH"]}/{poet}/info"
    )

    df = pd.DataFrame(data)

    poet_data = df[["name",
                      "born",
                      "died",
                      "nationality",
                      "poem_count"]]

    return poet_data

def search_poem(title: str):
    """Input title, parse json response and return poem"""

    api = current_app.extensions["poetrydb_api"]
    data = api.get_json(
        f"{current_app.config["POETRYDB_TITLE_SEARCH"]}/{title}"
    )


def append_poet_data(poet_data: list):
    """Input dataframe array, merge dataframes together"""

    try:
        if len(poet_data) == 1:
            return poet_data[0]
        if len(poet_data) > 1:
            combined_data = pd.concat(poet_data)
        else:
            raise IndexError
    except IndexError:
        print("poet_data list is empty!") 
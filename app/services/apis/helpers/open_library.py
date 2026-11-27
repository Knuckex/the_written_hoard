from flask import current_app 
import pandas as pd

def search_authors(author: str):
    """Search authors, return author details as a dataframe"""

    api = current_app.extensions["open_library_api"]
    data = api.get_json(
        current_app.config["OPEN_LIBRARY_AUTHORS_SEARCH_URL"],
        {"q": author}
        )

    data = pd.json_normalize(data["docs"][0])

    author_data = data[["name", 
                       "birth_date", 
                       "work_count", 
                       "ratings_count", 
                       "ratings_average", 
                       "ratings_count_1", 
                       "ratings_count_2", 
                       "ratings_count_3", 
                       "ratings_count_4", 
                       "ratings_count_5" 
                        ]]

    return author_data
    #for the purposes of this coursework I am assuming the top result is correct
    #author_id = data.docs[0].key
    #return author_id


def get_author(author_id: str):
    """Input author id, return author information in json"""
    
    api = current_app.extensions["open_library_api"]
    data = api.get_json(
        f"{current_app.config["OPEN_LIBRARY_AUTHOR_GET_URL"]}/{author_id}.json")



def search_site():
    """Search open library based on provided parameters"""
import requests
import app
import pandas as pd

def get_volumes(base_url: str, api_key: str ):
    url = base_url + "q=flowers+inauthor:keyes" + api_key 
    response = requests.get(url)
    #response.json()
    return response.json()


def parse_response(json_response):
    df = pd.DataFrame(json_response)
    print(df)
    return df
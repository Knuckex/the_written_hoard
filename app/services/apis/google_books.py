import requests
import app

def get_volumes(base_url: str, api_key: str ):
    url = base_url + "q=flowers+inauthor:keyes" + api_key 
    response = requests.get(url)
    response.json()
    return response
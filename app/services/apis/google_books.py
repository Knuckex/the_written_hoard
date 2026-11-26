import requests
import app
import pandas as pd
from pathlib import Path

# documentation: https://openlibrary.org/developers/api

# step 1 do a search for the author
#step 2 get authors id
# step 3 search author id 

def get_volumes(base_url: str, author_fetch_url: str ):
    url = base_url + author_fetch_url + "OL23919A" + ".json"
    user_agent = "bfmlvl6cw1"

    response = requests.get(url)
    #response.json()
    return response.json()


def parse_response(json_response):
    df = pd.DataFrame(json_response)
    print(df)
    
    output = Path('outputs')
    output.mkdir(exist_ok=True)
    report_path = output / 'google_books_response.csv'
    df.to_csv(report_path, index=False)

    return df

# open library seems better than google books
#user_agent=bfmlvl6cw1
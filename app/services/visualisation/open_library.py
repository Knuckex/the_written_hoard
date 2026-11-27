import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np

from matplotlib.figure import Figure

def create_author_pie_chart(author_data: pd.DataFrame):
    """Input a dataframe and return a pie chart as a Figure type"""

    # We need to pull out the first value specifically from each column. 
    # Even though there's only 1 row just taking the column will give us a series 
    cols = ["ratings_count_1", 
            "ratings_count_2", 
            "ratings_count_3", 
            "ratings_count_4", 
            "ratings_count_5"
            ]
    y = author_data[cols].iloc[0].to_numpy()
    
    labels = ["1 Star", "2 Stars", "3 Stars", "4 Stars", "5 Stars"]

    #returing a figure so we can use the io library to pass it into memory
    fig = Figure()
    ax = fig.subplots()
    ax.pie(y, labels=labels)
    ax.set_title("Rating Breakdown")

    return fig
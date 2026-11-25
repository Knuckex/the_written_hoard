import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    FLASK_APP = os.getenv("FLASK_APP", "run.py")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", "1")

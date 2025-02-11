from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    API_TOKEN = os.getenv('API_TOKEN')
    API_BASE_URL = os.getenv('API_BASE_URL')
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv() 

class Config: 
    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    LLAMA_INDEX_API_KEY = os.getenv("LLAMA_INDEX_API_KEY")
    LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

    # Flask Settings
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", "True").lower() == "true"
    FLASK_APP = os.getenv("FLASK_APP", "app.py")

    # Database
    DATABASE_URL = os.getenv("DATABASE_URL")

    # AWS
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

    # GitHub
    GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")

    # Streamit
    STREAMLIT_SERVER_PORT = int(os.getenv("STREAMLIT_SERVER_PORT", 8502))
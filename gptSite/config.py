import os
from dotenv import load_dotenv

load_dotenv()  # загружает .env

class Config:
    chatgpt_key = os.getenv("OPENAI_API_KEY")
    deepseek_key = os.getenv("DEEPSEEK_API_KEY")

config=Config()

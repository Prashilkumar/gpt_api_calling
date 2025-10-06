import os 
from openai import OpenAI
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

API_KEY =os.getenv('OPENAI_API_KEY')

if not API_KEY:
    pass

def get_client()->OpenAI:
    if not API_KEY:
        raise RuntimeError("OPENAI_API_KEY not set put it in environment file")
    return OpenAI(api_key=API_KEY)
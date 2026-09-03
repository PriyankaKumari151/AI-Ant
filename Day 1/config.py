##Environment Management and Secrets

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
env = os.getenv("ENVIRONMENT","development")

print(f"API Key fectched successfully") if api_key else print(f"GROQ API Key not found in {env} .env file")
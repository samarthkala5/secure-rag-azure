import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("Missing GROQ_API_KEY in .env")

MODEL_NAME = "llama-3.1-8b-instant"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

SIMILARITY_THRESHOLD = 0.93

MAX_RESPONSE_CHARS = 1200
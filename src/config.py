# src/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env if present

GAMMA_BASE_URL = os.getenv("GAMMA_BASE_URL", "https://gamma-api.polymarket.com")
CLOB_BASE_URL = os.getenv("CLOB_BASE_URL", "https://clob.polymarket.com")
DATA_BASE_URL = os.getenv("DATA_BASE_URL", "https://data-api.polymarket.com")
DEFAULT_TIMEOUT = int(os.getenv("HTTP_TIMEOUT", "10"))
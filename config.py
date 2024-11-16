# config/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot Token and default delete time (in seconds)
BOT_TOKEN = os.getenv("BOT_TOKEN")
DELETE_TIME = int(os.getenv("DELETE_TIME", 10))  # Default to 10 seconds

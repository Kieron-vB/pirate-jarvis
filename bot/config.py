from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
QB_USERNAME = os.getenv("QB_USERNAME")
QB_PASSWORD = os.getenv("QB_PASSWORD")
QB_HOST = os.getenv("QB_HOST", "127.0.0.1")
QB_PORT = int(os.getenv("QB_PORT", "8080"))

# Parse comma-separated user IDs as integers
ALLOWED_USER_IDS = [int(uid.strip()) for uid in os.getenv("ALLOWED_USER_IDS", "").split(",") if uid.strip()]


import os
from dotenv import load_dotenv

load_dotenv()

BOTS = {
    "marat": os.getenv("BOT_MARAT"),
}
ADMIN_BOT_TOKEN = os.getenv("ADMIN_BOT_TOKEN")

ADMIN_ID = os.getenv("ADMIN_ID")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")



import os

from dotenv import load_dotenv

load_dotenv()



DEVS = [
    6334438071 #DEVAIU
]

KYNAN = list(map(int, os.getenv("KYNAN", "6334438071").split()))

API_ID = int(os.environ.get("API_ID", "28524972"))

API_HASH = os.environ.get("API_HASH", "409130d1d167a2c26862e65e8779a3d6")

LOG_SELLER = int(os.getenv("LOG_SELLER", "-1002333374162"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001876092598 -1001864253073 -1001451642443 -1001825363971 -1001797285258 -1001927904459 -1001287188817 -1001812143750 -1001608701614 -1001473548283 -1001608847572 -1001982790377 -1001538826310 -1001861414061 -1001876092598 -1002079962899 -10015748196677").split()))

USER_ID = list(map(int, os.getenv("USER_ID", "6334438071").split()))

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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",
).split()

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7696179651:AAHKlvY1xYz_F14QPv3DcVqJYgBcWUj4MTQ")

OWNER_ID = int(os.environ.get("OWNER_ID", "6334438071"))

MAX_BOT = int(os.environ.get("MAX_BOT", "45"))

SKY = int(os.environ.get("SKY", "-1002479656527"))

MONGO_URL = os.environ.get(
    "MONGO_URL",
    "mongodb+srv://musicbot9809:buburayam1@cluster0.vwbhb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)

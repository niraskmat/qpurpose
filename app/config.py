import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE_ME")

if SECRET_KEY == "CHANGE_ME":
    print("[WARNING] Using fallback SECRET_KEY for development only. Set SECRET_KEY in production.")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

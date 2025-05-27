import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "FALLBACK_KEY")

if SECRET_KEY == "FALLBACK_KEY":
    print("[WARNING] Using fallback SECRET_KEY. Set SECRET_KEY in production.")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

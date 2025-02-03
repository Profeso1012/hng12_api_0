from fastapi import APIRouter
import os
from dotenv import load_dotenv
from app.utils import get_current_datetime

# Load environment variables from .env
load_dotenv()

# Create a router object
router = APIRouter()

@router.get("/")
def get_info():
    """Returns the required API response in JSON format."""
    return {
        "email": os.getenv("EMAIL"),
        "current_datetime": get_current_datetime(),
        "github_url": os.getenv("GITHUB_URL")
    }

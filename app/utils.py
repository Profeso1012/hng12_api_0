from datetime import datetime

def get_current_datetime():
    """Returns the current datetime in ISO 8601 format (UTC)."""
    return datetime.utcnow().isoformat() + "Z"
    
from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%dT%H:%M")
        return True
    except ValueError:
        return False

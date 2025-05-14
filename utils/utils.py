import random
import string

def generate_random_string(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def validate_ip(ip):
    parts = ip.split(".")
    if len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts):
        return True
    return False

def validate_port(port):
    try:
        port = int(port)
        return 0 <= port <= 65535
    except ValueError:
        return False
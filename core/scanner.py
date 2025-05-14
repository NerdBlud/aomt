import asyncio
import aiohttp
from utils.logger import setup_logger
from utils.http_tools import get_http_headers

log = setup_logger()

async def scan_ports(target, ports):
    open_ports = []
    async with aiohttp.ClientSession() as session:
        tasks = []
        for port in ports:
            task = asyncio.ensure_future(scan_port(session, target, port))
            tasks.append(task)
        open_ports = await asyncio.gather(*tasks)
    return [port for port, status in open_ports if status]

async def scan_port(session, target, port):
    url = f"http://{target}:{port}"
    try:
        async with session.get(url, timeout=2):
            log.info(f"Port {port} is open on {target}")
            return (port, True)
    except Exception as e:
        return (port, False)

def run(target, config):
    ports = list(map(int, config.get("SCANNER", "ports").split(",")))
    log.info(f"Scanning {target} on ports {ports}")
    open_ports = asyncio.run(scan_ports(target, ports))
    if open_ports:
        log.info(f"Open ports: {open_ports}")
    else:
        log.info(f"No open ports found on {target}.")

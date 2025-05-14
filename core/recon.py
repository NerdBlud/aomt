import whois
import dns.resolver
from utils.http_tools import simple_get
from utils.logger import setup_logger

log = setup_logger()

def run(target, config):
    log.info(f"Running reconnaissance on {target}")
    whois_data = perform_whois(target)
    log.info(f"WHOIS Data: {whois_data}")
    
    dns_data = perform_dns_enum(target)
    log.info(f"DNS Data: {dns_data}")
    
    http_response = simple_get(f"http://{target}")
    log.info(f"HTTP Response: {http_response[:100]}...")  # Truncate for log brevity

def perform_whois(target):
    """Performs a WHOIS lookup."""
    try:
        w = whois.whois(target)
        return w
    except Exception as e:
        log.error(f"WHOIS lookup failed for {target}: {e}")
        return None

def perform_dns_enum(target):
    """Performs a basic DNS enumeration."""
    dns_info = []
    try:
        for record_type in ['A', 'MX', 'NS', 'TXT']:
            dns_info.extend(dns.resolver.resolve(target, record_type))
    except Exception as e:
        log.error(f"DNS enumeration failed for {target}: {e}")
    return dns_info

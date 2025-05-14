import logging
from rich.logging import RichHandler

def setup_logger(log_level="INFO"):
    logger = logging.getLogger("AOMT")
    logger.setLevel(log_level)
    console_handler = RichHandler(rich_tracebacks=True)
    formatter = logging.Formatter("%(message)s")
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger
    
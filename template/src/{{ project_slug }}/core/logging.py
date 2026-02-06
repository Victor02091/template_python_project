import logging
import sys
from typing import Literal

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


def setup_logging(log_level: LogLevel = "INFO") -> logging.Logger:
    """
    Configures the root logger to print to stdout.
    Call this ONCE at the start of your program.
    """
    logger = logging.getLogger()

    # 1. Set the Global Log Level
    logger.setLevel(log_level.upper())

    # 2. Configure Output (Stdout)
    # We use stdout so logs appear in Docker/Kubernetes logs automatically
    handler = logging.StreamHandler(sys.stdout)

    # 3. Define Format
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s in %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)

    # 4. Avoid Duplicates
    # If this function is called twice, clear the old handler first
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(handler)

    return logger

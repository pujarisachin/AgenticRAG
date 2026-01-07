# app/core/logging.py

import logging
import sys
from typing import Optional

def setup_logging(log_level: str) -> None:
    """
    Configure application-wide logging.
    This should be called ONCE at application startup.
    """

    logging.basicConfig(
        level=log_level.upper(),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Get a logger instance with the given name.
    """
    return logging.getLogger(name)

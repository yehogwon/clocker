from time import time


def _millis() -> float:
    """
    Returns the current time in milliseconds.
    """
    return time() * 1000

import time
from functools import wraps
from selenium.common.exceptions import StaleElementReferenceException

def retry(retries=3, delay=0.25, exception=StaleElementReferenceException):
    """
    A decorator that retries a function call if a specified exception occurs.

    :param retries: Number of retry attempts before giving up.
    :param delay: Delay in seconds between retries.
    :param exception: Exception type to catch and retry on.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = retries
            while attempts > 0:
                try:
                    return func(*args, **kwargs)
                except exception as e:
                    attempts -= 1
                    if attempts == 0:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

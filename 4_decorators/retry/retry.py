# реализуйте декоратор вида @retry(count: int, delay: timedelta, handled_exceptions: tuple[type(Exceptions)])

import time
from datetime import timedelta
from functools import wraps


def retry(count=3, delay=timedelta(seconds=1), handled_exceptions=(Exception,)):
    if count < 1:
        raise ValueError("Нельзя передавать count меньший 1")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for request_attempt in range(count):
                try:
                    return func(*args, **kwargs)
                except handled_exceptions as e:
                    exception = e
                    if request_attempt < count - 1:
                        time.sleep(delay.total_seconds())
                    else:
                        raise exception
        return wrapper
    return decorator

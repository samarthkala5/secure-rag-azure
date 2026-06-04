from time import time

REQUESTS = []

MAX_REQUESTS = 10
WINDOW = 10


def reset_rate_limit():
    REQUESTS.clear()


def rate_limit_exceeded():

    now = time()

    while REQUESTS and now - REQUESTS[0] > WINDOW:
        REQUESTS.pop(0)

    if len(REQUESTS) >= MAX_REQUESTS:
        return True

    REQUESTS.append(now)

    return False
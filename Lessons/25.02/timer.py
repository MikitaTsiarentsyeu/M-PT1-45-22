import time

is_started = False

def start():
    global start_time, is_started
    is_started = True
    start_time = time.time()

def stop():
    if is_started:
        res = time.time() - start_time
        is_started = False
        return res


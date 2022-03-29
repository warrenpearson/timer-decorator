import functools
import time

def timed(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        t = time.localtime()
        curr_time = time.strftime("%H:%M:%S", t)
        print(f"Entering {func.__name__} at {curr_time}")
        value = func(*args, **kwargs)
        t = time.localtime()
        curr_time = time.strftime("%H:%M:%S", t)
        print(f"Exiting {func.__name__} at {curr_time}")
        return value
    return wrapper_decorator

@timed
def sleep_three():
    time.sleep(3)
    print("sleeping 3")

@timed
def sleep_five():
    time.sleep(5)
    print("sleeping 5")


sleep_three()
sleep_five()

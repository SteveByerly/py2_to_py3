
from functools import wraps
from threading import Thread
from time import sleep
from time import time


def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        return_value = func(*args, **kwargs)
        message = "Executing {} took {:.03} seconds.".format(func.__name__, time() - start)
        print(message)
        return return_value
    return wrapper


def fib(n):
    return fib(n - 1) + fib(n - 2) if n > 1 else n


def repeat_input():
    while True:
        n = int(input())
        timed_fib = log_execution_time(fib)
        print('fib({}) = {}'.format(n, timed_fib(n)))


def repeat_hello():
    while True:
        print("{} - Hello world!".format(int(time())))
        sleep(3)


def threaded_loop():
    """ Print 'Hello World' every three seconds while
    simultaneously accepting user input to calculate the
    Fibonacci sequence
    """

    # Put the hello world task into a new thread that can run
    # seperately from the fibonacci one
    t = Thread(target=repeat_hello)
    t.daemon = True
    t.start()
    # Main thread will read and process input
    repeat_input()

    """
    1470946642 - Hello World!
    1470946645 - Hello World!
    > 25
        Executing fib took 0.0358 seconds.
        fib(25) = 75025
    1470946648 - Hello World!
    1470946651 - Hello World!
    > 35
    1470946654 - Hello World!
        Executing fib took 4.11 seconds.
        fib(35) = 9227465
    1470946657 - Hello World!
    1470946660 - Hello World!
    """

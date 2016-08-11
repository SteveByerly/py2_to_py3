
import asyncio
from functools import wraps
import selectors
import sys
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


def print_hello(now=None):
    now = now or time()
    print("{} - Hello world!".format(int(now)))


def print_input(n):
    n = int(n)
    timed_fib = log_execution_time(fib)
    print('fib({}) = {}'.format(n, timed_fib(n)))


def run_custom_loop():
    selector = selectors.DefaultSelector()
    # Register the selector to poll for "read" readiness on stdin
    selector.register(sys.stdin, selectors.EVENT_READ)
    last_hello = 0  # Setting to 0 means the timer will start right away
    while True:
        # Wait at most 100 milliseconds for input to be available
        for event, mask in selector.select(0.1):
            text = event.fileobj.readline()
            print_input(text.strip())

        now = time()
        if now - last_hello > 3:
            last_hello = now
            print_hello(now=now)

    """
    1470947240 - Hello world!
    1470947243 - Hello world!
    > 10
        Executing fib took 4.08e-05 seconds.
        fib(10) = 55
    1470947246 - Hello world!
    1470947249 - Hello world!
    > 15
        Executing fib took 0.00038 seconds.
        fib(15) = 610
    1470947252 - Hello world!
    1470947255 - Hello world!
    > 35
        Executing fib took 4.11 seconds.
        fib(35) = 9227465
    1470947260 - Hello world!
    1470947263 - Hello world!
    """


def process_input():
    text = sys.stdin.readline()
    print_input(text.strip())


@asyncio.coroutine
def repeat_hello():
    while True:
        print_hello()
        yield from asyncio.sleep(3)


def run_asyncio():
    loop = asyncio.get_event_loop()
    loop.add_reader(sys.stdin, process_input)
    loop.run_until_complete(repeat_hello())

    """
    1470947855 - Hello world!
    1470947858 - Hello world!
    > 10
        Executing fib took 4.03e-05 seconds.
        fib(10) = 55
    1470947861 - Hello world!
    1470947864 - Hello world!
    > 15
        Executing fib took 0.000389 seconds.
        fib(15) = 610
    1470947867 - Hello world!
    1470947870 - Hello world!
    > 35
        Executing fib took 4.12 seconds.
        fib(35) = 9227465
    1470947875 - Hello world!
    1470947878 - Hello world!
    """


def do_fib():
    i = 0
    while i < 50:
        res = fib(i)
        print("fib: {0}".format(res))
        i += 1


def do_double():
    i = 0
    while i < 50:
        print("double: {0}".format(i * 2))
        i += 1


def run_asyncio_non_blocking():
    from concurrent.futures import ProcessPoolExecutor
    executor = ProcessPoolExecutor(2)
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(loop.run_in_executor(executor, do_fib))
    asyncio.ensure_future(loop.run_in_executor(executor, do_double))

    loop.run_forever()

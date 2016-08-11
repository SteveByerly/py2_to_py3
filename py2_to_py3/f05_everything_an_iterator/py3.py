
import timeit


def costly_func(num):
    for i in range(num + 1):
        pass


def wrap(num):
    def wrapped():
        return costly_func(num)
    return wrapped


def run1():
    last = 0
    for x in [100000, 1000000, 10000000, 100000000]:
        wrapped = wrap(x)
        time = timeit.timeit(wrapped, number=2)
        print('%s slower' % (time - last))
        last = time

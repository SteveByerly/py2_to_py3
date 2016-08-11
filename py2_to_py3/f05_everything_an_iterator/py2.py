
import timeit


def costly_func(num):
    for i in range(num + 1):
        pass


def less_costly_func(num):
    for i in xrange(num + 1):
        pass


def wrap(func, num):
    def wrapped():
        return func(num)
    return wrapped


def run1():
    last = 0
    for x in [100000, 1000000, 10000000, 100000000]:
        wrapped = wrap(costly_func, x)
        time = timeit.timeit(wrapped, number=2)
        print '%s slower' % (time - last)
        last = time


def run2():
    last = 0
    for x in [100000, 1000000, 10000000, 100000000]:
        wrapped = wrap(less_costly_func, x)
        time = timeit.timeit(wrapped, number=2)
        print('%s slower' % (time - last))
        last = time

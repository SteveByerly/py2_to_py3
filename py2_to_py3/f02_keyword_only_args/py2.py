

def sum1(a, b, do_bad=False):
    if do_bad:
        raise Exception('oops')

    return a + b


def sum2(a, b, *args, **kwargs):
    tally = a + b
    for var in args:
        tally += var

    if kwargs.get('do_bad'):
        raise Exception('oops')

    return tally


def run1():
    return sum1(1, 2)  # 3


def run2():
    try:
        sum1(1, 2, 3)
    except Exception as err:
        print(err)
        # Exception: 'oops'


def run3():
    func = 'def foo(a, b, *args, bar=None): pass'

    try:
        exec func
    except Exception as err:
        print(err)
        # Exception: SyntaxError


def run4():
    first = sum2(1, 2)
    second = sum2(1, 2, 3)

    print first  # 3
    print second  # 6

    try:
        sum2(1, 2, 3, do_bad=True)
    except Exception as err:
        print(err)
        # Exception: 'oops'

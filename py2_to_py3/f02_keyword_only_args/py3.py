

def run1():
    func = 'def foo(a, b, *args, bar=None): pass'

    exec(func)

    print('it works in py3')


def sum_1(a, *args, do_bad=False):
    if do_bad:
        raise Exception('oops')

    for var in args:
        a += var

    return a


def sum_2(a, b, *, do_bad=False):
    if do_bad:
        raise Exception('oops')

    return a + b


def run2():
    first = sum_1(1, 2)
    print(first)  # 3

    second = sum_1(1, 2, 3)
    print(second)  # 6


def run3():
    first = sum_2(1, 2)
    print(first)  # 3

    try:
        second = sum_2(1, 2, 3)
    except Exception as err:
        print(err)
        # Exception: TypeError

    try:
        third = sum_2(1, 2, do_bad=True)
    except Exception as err:
        print(err)
        # Exception: 'oops'

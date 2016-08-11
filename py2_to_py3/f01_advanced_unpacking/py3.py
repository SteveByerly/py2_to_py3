
import os


def run1():
    a, b, *rest = range(10)

    print(a)  # 0
    print(b)  # 1
    print(*rest)  # 2 3 4 5 6 7 8 9


def run2():
    a, *rest, b = range(10)

    print(a)  # 0
    print(*rest)  # 1 2 3 4 5 6 7 8
    print(b)  # 9

    *rest, b = range(10)

    print(*rest)  # 0 1 2 3 4 5 6 7 8
    print(b)  # 9


def run3():
    script_dir = os.path.dirname(__file__)

    with open(os.path.join(script_dir, 'test.txt'), 'rU') as f:
        first, *mid, last = f.readlines()

        print(first)  # line 1
        print(last)  # line 5

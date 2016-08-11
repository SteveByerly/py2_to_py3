
import os


def run1():
    a, b = range(2)

    print a  # 0
    print b  # 1


def run2():
    script_dir = os.path.dirname(__file__)

    with open(os.path.join(script_dir, 'test.txt'), 'rU') as f:
        lines = f.readlines()
        first = lines[0]
        mid = lines[1:-2]
        last = lines[-1]

        print first  # line 1
        print last  # line 5

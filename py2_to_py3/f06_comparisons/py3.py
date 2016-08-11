

def run1():
    max(['one', 2])
    # TypeError: unorderable types: int() > str()


def run2():
    'abc' > 12
    # TypeError: unorderable types: str() > int()


def run3():
    sorted(['1', 2, '3'])
    # TypeError: unorderable types: int() < str()

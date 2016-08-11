

def tally1(a, b):
    yield from range(a)
    yield from range(b)


def run1():
    tally = 0

    for val in tally1(5, 10):
        tally += val

    return tally  # 55


def multiply(num):
    for val in range(num):
        factor = yield val
        yield factor * val


def multiple_tally(a, b):
    yield from multiply(a)
    yield from multiply(b)


def run2():
    tally = 0
    gen = multiple_tally(5, 10)

    for val in gen:
        tally += gen.send(val)

    return tally  # 315

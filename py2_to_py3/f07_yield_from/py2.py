

# Bad
def tally1(a, b):
    vals = []

    for val in range(a):
        vals.append(val)

    for val in range(b):
        vals.append(val)

    return vals


def run1():
    tally = 0

    for val in tally1(5, 10):
        tally += val

    return tally  # 55


# Better
def tally2(a, b):
    for val in range(a):
        yield val

    for val in range(b):
        yield val


def run2():
    tally = 0

    for val in tally2(5, 10):
        tally += val

    return tally  # 55


def multiple_tally(a, b):
    for val in range(a):
        factor = yield val
        yield factor * val

    for val in range(b):
        factor = yield val
        yield factor * val


def run3():
    tally = 0
    gen = multiple_tally(5, 10)

    for val in gen:
        tally += gen.send(val)

    return tally  # 315

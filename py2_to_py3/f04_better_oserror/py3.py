
def do_secret(bar):
    raise OSError(13, 'No way!')


def run1():
    try:
        do_secret('bar')
    except PermissionError:
        print('Not Allowed')

    # Not Allowed

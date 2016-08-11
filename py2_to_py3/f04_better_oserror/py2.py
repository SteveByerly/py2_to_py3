
import errno


def do_secret(bar):
    raise OSError(13, 'No way!')


def run1():
    try:
        do_secret('bar')
    except OSError as e:
        if e.errno in [errno.EPERM, errno.EACCES]:
            print 'Not Allowed'
        else:
            print 'IDK?'

    # Not Allowed

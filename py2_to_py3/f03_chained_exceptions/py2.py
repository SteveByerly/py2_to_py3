

def run1():

    def handle(original_err):
        print missing_var

    try:
        var = 1 / 0
    except Exception as err:
        handle(err)

    """
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "f03_chained_exceptions/py2.py", line 11, in run1
        handle(err)
    File "f03_chained_exceptions/py2.py", line 6, in handle
        print missing_var
    NameError: global name 'missing_var' is not defined
    """
    # Where's the ZeroDivisionError ?

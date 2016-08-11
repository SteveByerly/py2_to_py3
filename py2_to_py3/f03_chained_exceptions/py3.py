

def run1():

    def handle(original_err):
        print(missing_var)

    try:
        var = 1 / 0
    except Exception as err:
        handle(err)

    """
    Traceback (most recent call last):
        File "/home/vagrant/py2_to_py3/f03_chained_exceptions/py3.py", line 9, in run1
            var = 1 / 0
    ZeroDivisionError: division by zero

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "/home/vagrant/py2_to_py3/f03_chained_exceptions/py3.py", line 11, in run1
            handle(err)
        File "/home/vagrant/py2_to_py3/f03_chained_exceptions/py3.py", line 6, in handle
            print(missing_var)
    NameError: name 'missing_var' is not defined
    """
    # We get both raised exceptions


def run2():
    # Chain exceptions explicitly
    try:
        var = 1 / 0
    except ZeroDivisionError as err:
        raise NotImplementedError from err

    """
    Traceback (most recent call last):
        File "/home/vagrant/py2_to_py3/f03_chained_exceptions/py3.py", line 35, in run2
            var = 1 / 0
    ZeroDivisionError: division by zero

    The above exception was the direct cause of the following exception:

    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "/home/vagrant/py2_to_py3/f03_chained_exceptions/py3.py", line 37, in run2
            raise NotImplementedError from err
    NotImplementedError
    """


import numpy as np


def test_print():
    print('hi')  # hi


def test_division():
    print(1 / 2)  # 0.5
    print(1 // 2)  # 0


def test_list_comprehension():
    x = 'hi'

    bar = [x for x in range(5)]

    print x  # hi


class Foo(object):

    def speak(self):
        return 'hi'


class Bar(Foo):

    def speak(self):
        out = super().speak()
        return out + ' there'


def test_super():
    foo = Foo()
    bar = Bar()

    print(foo.speak())  # 'hi'
    print(bar.speak())  # 'hi there'


def test_matrix_mult():
    a = np.array([[1, 0], [0, 1]])
    b = np.array([[4, 1], [2, 2]])

    return a @ b
    # array([[4, 1], [2, 2]])


def annotated_function(one: str, two: int = 2) -> str:
    print("Annotations:", annotated_function.__annotations__)
    # Annotations: {'one': <class 'str'>, 'return': <class 'str'>, 'two': <class 'int'>}

    print("Arguments:", one, two)
    # Arguments: three 2

    return '{} and {}'.format(one, two)


def test_function_annotations():
    val = annotated_function('three')
    print(val)  # three and 2

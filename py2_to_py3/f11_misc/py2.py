
import numpy as np


def test_print():
    print 'hi'  # hi


def test_division():
    print 1 / 2  # 0
    print 1 / 2.0  # 0.5

    from __future__ import division

    print 1 / 2  # 0.5
    print 1 // 2  # 0


def test_loop():
    x = 'hi'

    bar = [x for x in range(5)]

    print x  # 4


class Foo(object):

    def speak(self):
        return 'hi'


class Bar(Foo):

    def speak(self):
        out = super(Bar, self).speak()
        return out + ' there'


def test_super():
    foo = Foo()
    bar = Bar()

    print foo.speak()  # 'hi'
    print bar.speak()  # 'hi there'


def test_matrix_mult():
    a = np.array([[1, 0], [0, 1]])
    b = np.array([[4, 1], [2, 2]])

    return np.dot(a, b)
    # array([[4, 1], [2, 2]])

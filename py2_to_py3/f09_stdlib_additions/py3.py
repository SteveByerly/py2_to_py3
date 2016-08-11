
import ctypes
from enum import Enum
import faulthandler
from functools import lru_cache
import ipaddress
import urllib.error
import urllib.request


def killme():
    ctypes.string_at(0)


def test_faulthandler():
    # Note: this will kill your active python process
    faulthandler.enable()
    return killme()

    """
    Fatal Python error: Segmentation fault

    Current thread 0x00007f51f0fca740 (most recent call first):
    File "/usr/lib/python3.5/ctypes/__init__.py", line 491 in string_at
    File "/home/vagrant/py2_to_py3/f09_stdlib_additions/py3.py", line 7 in killme
    File "/home/vagrant/py2_to_py3/f09_stdlib_additions/py3.py", line 12 in test_faulthandler
    File "<stdin>", line 1 in <module>
    Segmentation fault (core dumped)
    """


def test_ipaddress():
    ipv4 = ipaddress.ip_address('192.168.0.1')
    ipv6 = ipaddress.ip_address('2001:db8::')

    print(ipv4)  # IPv4Address('192.168.0.1')
    print(ipv6)  # IPv6Address('2001:db8::')


@lru_cache(maxsize=32)
def get_pep_page(num):
    'Retrieve text of a Python Enhancement Proposal'
    resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except urllib.error.HTTPError:
        return 'Not Found'


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def test_lru_cache():
    for n in [8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991]:
        get_pep_page(n)

    print(get_pep_page.cache_info())
    # CacheInfo(hits=3, misses=8, maxsize=32, currsize=8)

    [fib(n) for n in range(16)]
    print(fib.cache_info())
    # CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)


class Color(Enum):
    red = 1
    green = 2
    blue = 3


def test_enum():
    print(Color.red)  # Color.red
    print(Color.red.name)  # red
    print(Color.red.value)  # 1

    print(Color(2))  # <Color.green: 2>
    print(Color['blue'])  # <Color.blue: 3>

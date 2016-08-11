Standard Library Additions

faulthandler:
https://docs.python.org/3/library/faulthandler.html

- When enabled, will dump Python tracebacks explicitly, on a fault, after a timeout, or on a user signal
- Tracebacks written to sys.stderr by default, but can pass a log file to the faulthandler `enable` function
- Either enable explicitly in code `import faulthandler; faulthandler.enable()`, or via command line `python -X faulthandler`


ipaddress:
https://docs.python.org/3/library/ipaddress.html

- create, manipulate and operate on IPv4 and IPv6 addresses and networks.


lru_cache (Least Recently Used Cache):
https://docs.python.org/3/library/functools.html#functools.lru_cache

- Decorator to wrap a function with a memoizing callable that saves up to the maxsize most recent calls. 
- Can save time when an expensive or I/O bound function is periodically called with the same arguments.
- Dictionary is used to cache results, the positional and keyword arguments to the function must be hashable.

enum:
https://docs.python.org/3/library/enum.html

- A set of symbolic names (members) bound to unique, constant values.
- Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over.
- Names must be unique, but values can be duplicated
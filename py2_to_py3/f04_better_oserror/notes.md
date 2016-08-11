Improved OS/IO Exceptions

PEP 3151
https://www.python.org/dev/peps/pep-3151/

- Provides a more comprehensive set of exception classes for errors related to operating system calls (OSError, IOError, mmap.error, select.error, and all their subclasses).
- Allows you to catch specific errors instead of inspecting the error for its error number
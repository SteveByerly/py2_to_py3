General Changes:

Print:

- The print statement is now a function. You must pass what to print as an argument.


Division:

- Normal division now returns a float instead of a truncated integer. New infix operator for old behavior


List Comprehension:

- Using an existing variable name in a list comprehension no longer overwrites its value

Super:

PEP 3135
https://www.python.org/dev/peps/pep-3135/

- No longer need to pass arguments to a super call


Matrix Multiplication:

PEP 465
https://www.python.org/dev/peps/pep-465/

- Adds new `@` infix operator for multiplying matrices
- Any object can override `__matmul__` to use the `@` infix operator


Function Annotations:

PEP 3107
https://www.python.org/dev/peps/pep-3107/

- Allow you to add arbitrary metadata annotations to Python functions
- Completely optional and have no effect on the function
- Get stored in the `__annotations__` attribute of the function



# Resources about changes

http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html#returning-iterable-objects-instead-of-lists

https://asmeurer.github.io/python3-presentation/slides.html


# Resources about porting

https://docs.python.org/3/howto/pyporting.html

http://python3porting.com/differences.html

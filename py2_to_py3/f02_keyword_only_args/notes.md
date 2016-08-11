Keyword Only Arguments

PEP 3102
https://www.python.org/dev/peps/pep-3102/

-You can now specify a variable number of args prior to defining required kwargs:
`def foo(a, b, *args, bar=None)`

-Prevent accidentally setting a kwarg by passing too many arguments. Do this by sending an unnamed vararg:
`def foo(a, b, *, bar=None)`

-Good way to harden an api. Prevent functions from being called incorrectly (e.g. arguments pass in different order), or make changing method signature easier.
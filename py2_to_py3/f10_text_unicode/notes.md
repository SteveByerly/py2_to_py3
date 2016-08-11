Unicode and Text

- Python 2 treated all strings (str) like bytes of data
- There is also unicode to handle text, which can be further encoded
- Depending on the text, the length of the str and unicode representation will differ based on the number of bytes needed for each character
- Python 2 was happy to automatically coerce `str` and `unicode` into a single `unicode` string

- Python 3 now treats all strings (str) like python 2 unicode types. To get the old behavior of bytes, you need to explicitly make a byte string: `b'my byte string'`
- Python 3 will no longer auto-coerce different string types for you.
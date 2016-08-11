# encoding=utf-8


def test_strings():
    strings = [
        'normal string',
        'ünicôdé strįng',
    ]

    for string in strings:
        print(string)
        print(len(string))
        print(type(string))  # <class 'str'>

        try:
            new = string.encode('ascii')
            print(type(new))  # <class 'bytes'>
            print(new)  # b'normal string'
        except UnicodeEncodeError:
            new = string.encode('utf-8', 'ignore')
            print(new)  # b'\xc3\xbcnic\xc3\xb4d\xc3\xa9 str\xc4\xafng'
            print(len(new))  # 18
            print(type(new))  # <class 'bytes'>

            new = string.encode('ascii', 'ignore')
            print(new)  # b'nicd strng'
            print(type(new))  # <class 'bytes'>

    try:
        combo = 'normal string ' + b'byte string'
        print(combo)
    except TypeError:
        print('No more type coercion!')

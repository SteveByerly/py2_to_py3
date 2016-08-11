# encoding=utf-8


def test_strings():
    strings = [
        'normal string',
        'ünicôdé strįng',
    ]
    for string in strings:
        print string
        print len(string)
        print type(string)  # <type 'str'>

        try:
            new = string.encode('ascii')
            print type(new)  # <type 'str'>
            print new  # normal string
        except UnicodeDecodeError:
            print len(string)  # 18

            new = unicode(string, 'utf-8')
            print new  # u'\xfcnic\xf4d\xe9 str\u012fng'
            print len(new)  # 14
            print type(new)  # <type 'unicode'>

            new = new.encode('ascii', 'ignore')
            print new  # nicd strng (yuck)
            print type(new)  # <type 'str'>

    strings = [
        u'normal string',
        u'ünicôdé strįng',
    ]
    for string in strings:
        print type(string)  # <type 'unicode'>

    combo = 'normal string ' + u'ünicôdé strįng'
    print combo
    print type(combo)  # <type 'unicode'>

def is_str(s):
    result = isinstance(s, basestring)
    if result :
        print s + ' is baseString'
    else:
        print s + ' is not baseString'


def is_unicode(s):
    result = isinstance(s, unicode)
    if result:
        print s + ' is unicode'
    else:
        print s + ' is not unicode'
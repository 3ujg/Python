import codecs
x = 'some string'
y = codecs.encode(x, 'rot13')
codecs.decode(y, 'rot13')
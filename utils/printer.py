''' Output module
'''

def print_header():
    print '\nPython accessibility checker report:\n'

def print_warn(warn):
    print warn['content'] + ' is missing in ' + warn['local']
    print 'comment: ' + warn['explanation'] + '\n'

def print_not_found():
    print 'No html found!'

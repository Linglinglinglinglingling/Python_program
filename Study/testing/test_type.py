import sys
def test_type_line(variable):
    linenum=sys._getframe(1).f_lineno
    if isinstance(variable,int):
        print('variable at line {0} is int'.format(linenum))
    elif isinstance(variable,str):
        print('variable at line {0} is string'.format(linenum))
    elif isinstance(variable,list):
        print('variable at line {0} is list'.format(linenum))
    elif isinstance(variable,tuple):
        print('variable at line {0} is tuple'.format(linenum))
    elif isinstance(variable,dict):
        print('variable at line {0} is dictionary'.format(linenum))
    elif isinstance(variable,set):
        print('variable at line {0} is set'.format(linenum))

if __name__ == '__main__':
    test_type_line({1:'a'})
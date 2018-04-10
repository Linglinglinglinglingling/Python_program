import sys
def test_bool_line(did_pass):
    linenum=sys._getframe(1).f_lineno
    if did_pass:
        print('test at line {0} True'.format(linenum))
    else:
        print('test at line {0} False'.format(linenum))

if __name__ == '__main__':

    a=lambda x,y:x+y
    test_bool_line(a(1,12)==2)
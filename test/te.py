import sys

try:
    compat_str = unicode  # Python 2
except NameError:
    compat_str = str


def encodeFilename(s, for_subprocess=False):
    """
    @param s The name of the file
    """

    assert type(s) == compat_str

    # Python 3 has a Unicode API
    if sys.version_info >= (3, 0):
        return s

    # Pass '' directly to use Unicode APIs on Windows 2000 and up
    # (Detecting Windows NT 4 is tricky because 'major >= 4' would
    # match Windows 9x series as well. Besides, NT 4 is obsolete.)
    if not for_subprocess and sys.platform == 'win32' and sys.getwindowsversion()[0] >= 5:
        return s

    # Jython assumes filenames are Unicode strings though reported as Python 2.x compatible
    if sys.platform.startswith('java'):
        return s

    #return s.encode(get_subprocess_encoding(), 'ignore')



    def encodeArgument(s):
        if not isinstance(s, compat_str):
            # Legacy code that uses byte strings
            # Uncomment the following line after fixing all post processors
            # assert False, 'Internal error: %r should be of type %r, is %r' % (s, compat_str, type(s))
            s = s.decode('ascii')
        return encodeFilename(s, True)
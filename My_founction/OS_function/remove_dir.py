import os


def rmtree(path):
    for name in os.listdir(path):
        fname = os.path.join(path, name)
        if os.path.isdir(fname):
            rmtree(fname)
        else:
            #os.chmod(fname, 0o666)
            os.remove(fname)
    os.rmdir(path)

if __name__ == '__main__':
    rmtree("C:\\Users\\ASUS\\Desktop\\New folder - Copy")
def a(length, width):
    a = [None] * length
    board = []
    for i in range(width):
        board.append(a[:])
    return board

b=a(2,5)

b[1][1]=3
print(b)
#
class A:
    def __init__(self):
        pass

    #accessor
    def get(self):
        pass

    #mutator
    def set(self):
        pass

    def __str__(self):
        pass

    def __contains__(self, item):
        pass

def main():
    pass


if __name__ == '__main__':
    main()


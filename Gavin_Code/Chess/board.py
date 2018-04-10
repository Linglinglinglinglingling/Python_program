class Board:

    def __init__(self,n,the_empty=0):

        self.theBoard = []
        self.size = n
        self.empty = the_empty
        i = 0

        while (i < n):
            self.theBoard.append([self.empty]*n)
            i += 1

    def __str__(self):

        new_string = ""

        for row in self.theBoard:
            for item in row:
                new_string += str(item) + "\t"
            new_string.strip('\t')
            new_string += "\n"

        return new_string

    def get_piece(self,x,y):

        if (x < self.size and y < self.size):
            return self.theBoard[x][y]
        else:
            print("Lurn 2 pley scroob. Outside of board.")

    def place_piece(self,x,y,the_piece):

        if(x < self.size and y < self.size):
            self.theBoard[x][y] = the_piece
        else:
            print("Lurn 2 pley scroob. Outside of board.")

    def remove_piece(self,x,y):
        self.place_piece(x,y,self.empty)

    def move_piece(self,from_x,from_y,to_x,to_y):

        the_piece = self.get_piece(from_x,from_y)
        self.place_piece(to_x,to_y,the_piece)
        self.remove_piece(from_x,from_y)

    def flip_board(self):

        i = 0

        while i < self.size:

            j = 0
            while j < self.size:
                self.remove_piece(i,j)
                j += 1
            i += 1

    def is_empty(self,x,y):
        return self.theBoard[x][y] == self.empty

def main():
    testBoard = Board(4,"F")

    testBoard.place_piece(1, 1, "g")

    print(testBoard)

    testBoard.flip_board()

    print(testBoard)

if __name__ == "__main__":
    main()
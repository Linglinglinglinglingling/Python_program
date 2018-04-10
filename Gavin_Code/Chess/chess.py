from board import Board
from piece import Piece

class Chess:

    def __init__(self):
        self.chessBoard = Board(8,"-:-")

        i = 0

        while(i < 8):
            firstPiece = Piece("pawn",0)
            self.chessBoard.place_piece(1,i,firstPiece)
            secondPiece = Piece("pawn",1)
            self.chessBoard.place_piece(6,i,secondPiece)
            i += 1

        self.chessBoard.place_piece(0,0,Piece("rook",0))
        self.chessBoard.place_piece(0,7,Piece("rook",0))

        self.chessBoard.place_piece(7, 0, Piece("rook", 1))
        self.chessBoard.place_piece(7, 7, Piece("rook", 1))

        self.chessBoard.place_piece(0,1, Piece("knight",0,the_character="N"))
        self.chessBoard.place_piece(0, 6, Piece("knight", 0,the_character= "N"))

        self.chessBoard.place_piece(7, 1, Piece("knight", 1,the_character= "N"))
        self.chessBoard.place_piece(7, 6, Piece("knight", 1,the_character= "N"))

        self.chessBoard.place_piece(0,2,Piece("bishop",0))
        self.chessBoard.place_piece(0, 5, Piece("bishop", 0))

        self.chessBoard.place_piece(7, 2, Piece("bishop", 1))
        self.chessBoard.place_piece(7, 5, Piece("bishop", 1))

        self.chessBoard.place_piece(0,4, Piece("queen",0))
        self.chessBoard.place_piece(0, 3, Piece("king", 0))

        self.chessBoard.place_piece(7, 4, Piece("king", 1))
        self.chessBoard.place_piece(7, 3, Piece("queen", 1))

    def __str__(self):
        return str(self.chessBoard)

    def get_moves(self,x,y):

        the_piece = self.chessBoard.get_piece(x,y)
        character = the_piece.get_character()
        colour = the_piece.get_colour()

        moves = []

        if character == "P":

            if colour == 0:

                #if in front is free, add move
                if(self.chessBoard.is_empty(x+1,y)):
                    moves.append((1,0))

                    # if 2 in front is free, and is first move, add move
                    if(self.chessBoard.is_empty(x+2,y)):
                        if(x == 1):
                            moves.append((2,0))

                if(not(self.chessBoard.is_empty(x+1,y+1))):
                    if(self.chessBoard.get_piece(x+1,y+1).colour != 0):
                        moves.append((1,1))

                if (not (self.chessBoard.is_empty(x + 1, y - 1))):
                    if (self.chessBoard.get_piece(x + 1, y - 1).colour != 0):
                        moves.append((1,-1))

def main():
    game = Chess()

    print(game)

    choice = "0"

    while choice != "q":
        choice = input("make a choice")

        if choice == 1:
            fart
        # elif choice ==0

if __name__ == "__main__":
    main()
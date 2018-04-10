class Piece:

    def __init__(self,the_name,the_colour,**kwargs):
        self.name = the_name
        self.colour = the_colour

        if "the_character" in kwargs:
            self.character = kwargs["the_character"]
        else:
            self.character = self.name[0].upper()

    def __str__(self):
        return str(self.character) + ":" + str(self.colour)

    def get_colour(self):
        return self.colour

    def get_name(self):
        return self.name

    def get_character(self):
        return self.character

def main():
    testPiece = Piece("pawn",0)

    print(testPiece.name)
    print(testPiece)

if __name__ == "__main__":
    main()
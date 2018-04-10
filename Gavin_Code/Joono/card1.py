
# define a class Card used to create single card
class Card:

# define a __init__method which is used to set the card attributes like card_face and card_suit
    def __init__(self, card_face, card_suit):
# define an instance variable which is used to transfer the integers number to string.
        self.card_face_dictionary = {"1": "A", "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": "T","11": "J", "12": "Q", "13": "K"}
# define an instance variable self.card_face which is used to store the card_face

        self.card_face = self.card_face_dictionary[str(card_face)]


# define an instance variable self.card_suit which is used to store the card_suit
        self.card_suit = card_suit

# define a self.character variable to store the first letter in every suit
        self.character = self.card_suit[0].upper()

# overload __str__ metho to let the instance becoming the str
    def __str__(self):

# return a particular format of string which combine self.character with self.card_face
        return str(self.character) + str(self.card_face)

# define get_card_face which is used to return the self.card_face in string data type
    def get_card_face(self):

        return str(self.card_face)

# define get_card_suit which is used to return the self.character in string data type
    def get_card_suit(self):
        return str(self.character)

# define change_card_face which is used to let the Card class become changable
    def change_card_face(self, face):

# define a variable to change the card face
        self.card_face = face

# define change_card_suit which is used to change the card face
    def change_card_suit(self, suit):

# define change_card_suit which is used to change the card suit
        self.card_suit = suit




# Test the program

if __name__ == '__main__':
    a = Card("5", "Spade")
    print(a)
    print(type(a.get_card_face()))

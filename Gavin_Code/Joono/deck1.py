# import Card class from card file
from Gavin_Code.Joono.card1 import Card
# import random to use shuffle
import random

# define a class which is called Deck used to store 52 disorder cards

class Deck:

# define a __init__ method, which contain self.value_start, self.value_end, self.number_of_suits and self.cards
    def __init__(self, value_start, value_end, number_of_suits):

# define a variable self.suit to store the suit name.
        self.suit = ["Diamond", "Heart", "Spade", "Club"]
# define a self.value_start variable which is used to set the start number.
        self.value_start = value_start

# define a self.value_end variable which is used to set the end number.
        self.value_end = value_end

# define a self.number_of_suits variable which is used to set the number of suit
        self.number_of_suits = number_of_suits

# define self.cards which is used to store the cards
        self.card_list = []

# overload __str__ method to let the instance becoming the str
    def __str__(self):

# call the add_card() method which is used to let the self.card_list store the cards
        self.add_card()

# define card_list_str to store the self.card_list
        card_list_str = "{}".format(self.card_list)
        return card_list_str

    def add_card(self):

# use while loop to add cards to deck
        while self.number_of_suits > 0:

# define no_suit to let the number of suit without constraint.
            no_suit = (self.number_of_suits % 4) - 1

# append the card to deck
# variable n means means "number" which is used to iterate the number from value_start to value_end
            for n in range(self.value_start, self.value_end, 1):
# define single_card to store the generated card
                single_card = Card(n, self.suit[no_suit]).get_card_suit() + Card(n,self.suit[no_suit]).get_card_face()
                self.card_list.append(single_card)

            self.number_of_suits = self.number_of_suits - 1

# return the self.card_list
        return self.card_list

# define enlarge_the_suits which is used to enlarge the number of the suits
    def enlarge_the_suits(self, num):

        while num > 0:

# define no_suit to let the number of suit without constraint.
            no_suit = (num % 4) - 1

# add the card to deck
# variable n means means "number" which is used to iterate the number from value_start to value_end
            for n in range(self.value_start, self.value_end, 1):
                # define single_card to store the generated card
                single_card = Card(n, self.suit[no_suit]).get_card_suit() + Card(n, self.suit[no_suit]).get_card_face()
                self.card_list.append(single_card)

            num = num - 1

            # return the self.card_list
        return self.card_list


# shuffle the cards
    def shuffle_the_card(self):
        self.add_card()
        random.shuffle(self.card_list)
        return self.card_list

# define a draw method which is used to distribute the card to the game table
    def draw(self):

# the vairiable 'pcard' means pop the card which is used to store the card from self.card_list.pop()
        pcard = self.card_list.pop()
        return pcard



if __name__ == '__main__':
    a = Deck(1,14,8)
    print(a.card_list)
    print(a)
    a.shuffle_the_card()
    print(a.card_list)
    b = Deck(1,14,4)
    print(b)
    a.enlarge_the_suits(3)
    print(len(a.card_list))




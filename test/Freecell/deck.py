#Deck
import random
from card import Card
class Deck:


    def __init__(self,value_start,value_end,number_of_suits):
        self.value_start=value_start
        self.value_end=value_end
        self.number_of_suits=number_of_suits
        self.the_deck=[]

        self.suit_list=['H','D','C','S']
        #start from the suit 1, assign the first suit-value in the suit_list to
        #the suit 1. Then suit 2 use second-suit value, do the same to rest
        #of suits

        for j in range(self.number_of_suits):
            suit=self.suit_list[j%4]
            for m in range(self.value_start,self.value_end+1):
                self.the_deck.append(Card(m,suit))


    #accessor, get a list of all item inside the deck
    def get_deck(self):
        return self.the_deck

    def get_minimal_value(self):
        return self.value_start

    def get_maximal_value(self):
        return self.value_end

    def get_suit_number(self):
        return self.number_of_suits

    #mutator, change the card in a given index
    def change_card(self,index,card):
        self.the_deck[index]=card


    #for test purpose, not used in notfreecell
    def __str__(self):
        display=''
        number_inline=0
        for i in self.the_deck:
            display+=str(i)+'\t'
            number_inline+=1
            if number_inline%8==0:
                display+='\n'
        return display


    #shuffle the deck list
    def shuffle(self):
        random.shuffle(self.the_deck)
        return self.the_deck

    # add card into deck list
    def add_card(self,card):
        self.the_deck.append(card)

    #draw a card from the last item in the deck list
    def draw_card(self):
        if len(self.the_deck)==0:
            print('There is no card left')
        return self.the_deck.pop()


def main():
   pass

if __name__ == '__main__':
    main()

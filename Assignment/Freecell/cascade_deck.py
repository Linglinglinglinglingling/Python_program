#
from card import Card
class Cascade_deck:
    def __init__(self):
        self.cascade_deck=[]

    #get the length of cascade_deck list
    def length_cascade_deck(self):
        return len(self.cascade_deck)

    #accessor, given an index return the correspond card
    def get_cascade_deck(self,index):
        return self.cascade_deck[index]

    #mutator, change the card in given index
    def change_cascade_deck(self,index,card):
        self.cascade_deck[index]=card


    def add_card(self,card):
        #if empty, can add any card
        if len(self.cascade_deck)==0:
            self.cascade_deck.append(card)
            return None

        #if not empty, only card in different color with topmost card
        #and value less by 1 can be added
        elif len(self.cascade_deck)>0 and \
           self.get_cascade_deck(-1).get_face()-1==card.get_face() and \
           self.get_cascade_deck(-1).get_color()!=card.get_color():
            self.cascade_deck.append(card)
            return None

        #return False ,it will be used in notfreecell.move_card
        else:
            print('\n'+'\n'+'please add the valid card in cascade deck'+'\n'+'\n')
            return False

    def remove_card(self):
        # if cascade_empty, return False which will be used in notfreecell.move_card
        if len(self.cascade_deck)==0:
            print('\n'+'\n'+'There is no card in cascade_deck to remove'+'\n'+'\n')
            return False
        else:
            return self.cascade_deck.pop()


    ##append a card into cascade list, it is used to undo the remove_card
    def append_card(self, card):
        self.cascade_deck.append(card)


    #for test purpose, not used in notfreecell
    def __str__(self):
        display = ''
        if len(self.cascade_deck)==0:
            return display
        else:
            for i in self.cascade_deck:
                display+=str(i)+'\n'
            return display


def main():
    pass


if __name__ == '__main__':
    a=Cascade_deck()
    a.add_card(Card(2,'H'))
    a.add_card(Card(1,'C'))
    print(a)

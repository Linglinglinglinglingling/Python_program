#Foundation Class
from card import Card
class Foundation:
    def __init__(self):
        self.foundation=[]

    #return length of the foundation list, it is used to check whether the game wins
    def length_foudation(self):
        return len(self.foundation)

    #accessor get the topmost card
    def get_foundation(self):
        if len(self.foundation)==0:
            print('There is no card in the foundation')
        else:
            return self.foundation[-1]

    def get_card(self,index):
        return self.foundation[index]

    #mutator, change the card in a given index
    def change_foundation_card(self,index,card):
        self.foundation[index]=card


    def add_card(self,card):
        # if no card in foundation, only card with face=1 can be appended
        if len(self.foundation)==0 and card.get_face()==1:
            self.foundation.append(card)
            return None

        #if not empty, only card with same suit as the topmost card and value greater by 1 can be appended
        elif len(self.foundation)>0 and \
            self.get_foundation().get_suit()==card.get_suit() and \
            self.get_foundation().get_face()+1==card.get_face():
            self.foundation.append(card)
            return None

        #Otherwise return False,False will be used in the notfreecell.move_card function
        else:
            print('\n'+'\n'+'Please add the valid card in foundation'+'\n'+'\n')
            return False

    def remove_card(self):
        if len(self.foundation)==0:
            print('\n'+'\n'+'There is no card in foundation to remove''+\n'+'\n')
            #false will be used in notfreecell.move_card function
            return False
        else:
            return self.foundation.pop()


    #append a card into foundation list, it is used to undo the remove_card
    def append_card(self, card):
        self.foundation.append(card)


    def __str__(self):
        #if empty, display as []
        if len(self.foundation)==0:
            return str(self.foundation)
        #if not empty, display topmost card
        else:
            return str(self.get_foundation())




def main():
   pass





if __name__ == '__main__':
    main()

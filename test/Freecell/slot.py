#Slot class
from card import Card
class Slot:
    def __init__(self):
        self.slot=[]

    #get the topmost card
    def get_slot(self):
        if len(self.slot)==0:
            print('There is no card in the slot')
        else:
            return self.slot[0]

     #mutator,change the topmost card
    def change_slot_card(self,card):
        self.slot[0]=card


    #append card into slot list, if there is already a card in it, return False
    #the False is used in Notfreecell move_card function
    def add_card(self,card):
        if len(self.slot)==1:
            print('\n'+'\n'+'There is already a card in the slot,please remove it first'+'\n'+'\n')
            return False
        else:
            self.slot.append(card)
            return None

    #remove the topmost card from the slot list. False is used in Notfreecell move_card
    def remove_card(self):
        if len(self.slot)==0:
            print('\n'+'\n'+'There is no card in slot to remove'+'\n'+'\n')
            return False
        else:
            return self.slot.pop()


    #append a card into slot list, it is used to undo the remove_card
    def append_card(self, card):
        self.slot.append(card)

    #display the slot,if the slot is empty,show as []; else, show the topmost card
    def __str__(self):
        if len(self.slot)==0:
            return str(self.slot)
        else:
            self.display_slot=str(self.get_slot())
            return str(self.display_slot)




def main():
    pass


if __name__ == '__main__':
    main()

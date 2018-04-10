#Card class
class Card:
    def __init__(self,card_face,card_suit):
        self.card_face=card_face
        self.card_suit=card_suit
        self.the_card=(self.card_face,self.card_suit)
        #Red color card is represented by 0, black card by 1
        if self.card_suit=='H' or self.card_suit=='D':
            self.card_color=0
        else:
            self.card_color=1
    #get the face of a card
    def get_face(self):
        return self.card_face

    #get the suit of a card
    def get_suit(self):
        return self.card_suit

    def get_color(self):
        return self.card_color

    #mutator, change card's face, suit
    def set_face(self,face):
        self.card_face=face

    def set_suit(self,suit):
        self.card_suit=suit
        if self.card_suit=='H' or self.card_suit=='D':
            self.card_color=0
        else:
            self.card_color=1

    # card display in A:H,X:H,J:H
    def __str__(self):
        # change the display format for 1 ,10 ,11, 12, 13
        translate={1:'A',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'X',11:'J',12:'Q',13:'K'}
        return translate[self.card_face]+':'+str(self.card_suit)


def main():
    pass


if __name__ == '__main__':
    a=Card(7,'H')
    print(a.get_color)

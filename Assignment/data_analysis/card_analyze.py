#
from card import Card
from deck import Deck
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Card_analysis:
    #create a deck with given number of suit
    def __init__(self,num_suit):
        self.num_suit=num_suit
        self.deck=Deck(1,13,self.num_suit)

    #given a list that contains multiple cards,check if it is flush
    def is_flush(self,card_list):
        base_suit=card_list[0].get_suit()
        # pick the suit of first card as the base suit,
        # if there is any card that is not in the same suit with base suit,
        # then it is not a flush
        for i in card_list:
            if i.get_suit()!=base_suit:
                return False
        return True

    #given a list that contains multiple cards, check if it contains any pair
    def contain_pair(self,card_list):
        #add all cards' face values to a set,
        #if length is changed,then origin list contains pair
        face_set=set()
        for i in card_list:
            face_set.add(i.get_face())
        if len(face_set)!=len(card_list):
            return True
        else:
            return False


    #given a list of appear times of flush or pair(e.g. [1,2], each item is divided by 1000 then
    #return the average value of all possibility and display in following format:
    # (1/1000+2/1000)/2=0.3%
    def result_string(self,result_list):
        res_string='('
        #last item in result_list don't need '+'
        for item in result_list[:-1]:
            res_string+=str(item)+'/1000'+'+'
        #                                                                         use sum/(1000*len(list) to calculate average,then change to
        #                                                                         percentage
        res_string+=str(result_list[-1])+'/1000'+')'+'/'+str(len(result_list))+'='+str(sum(result_list)/(1000*len(result_list))*100)+'%'
        return res_string


    #draw card 1000 times,if a card is drawn,its occurrence time +1,
    #return the list record each card's occurrence time and sum of all drawn card's face value
    def average_value(self):
        sum_face = 0
        # create a list to record each card's number of occurrence
        num_occurrence = [0] * 13
        # each loop, shuffle deck, draw card--add the value to sum and the drawn card's
        #  occurrence +1. Then add the card back into deck
        for i in range(1000):
            self.deck.shuffle()
            drawn_card = self.deck.draw_random_card()
            sum_face += drawn_card.get_face()
            # occurrence time of drawn card +1
            num_occurrence[drawn_card.get_face() - 1] += 1
            self.deck.add_random_card(drawn_card)

        return num_occurrence,sum_face


    #used the data from function--average_value to draw the bar graph
    #x-axis: A--k
    #y-axis: occurrence time of each card face
    def draw_average_value(self):
        num_occurrence,sum_face=self.average_value()
        # x-axis 1-13
        x=range(1,14)
        #draw the bar graph
        plt.bar(x,num_occurrence,color='g')
        plt.xlabel('Card face')
        plt.ylabel('times of appearance ')
        plt.title('There are ' + str(self.num_suit) + ' suits, ' + 'draw one cards for 1000 times ')
        #show the occurrence of each card on top of the bar graph
        for x, y in zip(x, num_occurrence):
            plt.text(x-0.2 , y , str(y))
        #change the display format for x-axis to A--k
        plt.xticks(np.arange(1,14),('A','2','3','4','5','6','7','8','9','10','J','Q','K'))
        plt.show()
        print('The average face value is:', str(sum_face) + '(sum of face value)' + '/' + '1000(times) =',
              sum_face / 1000)


    #given the number of times of running the experiment,each time starts by drawing 5 cards from deck
    #and check if it is flush or contains pair. If it is flush then number of flush +1,
    #if it contains pair, then number of pair +1. After this ,put the drawn card back into
    #deck and repeat this move 1000 times. Before the end of one experiment, record the
    # total number of flush and pair into result_list.
    #Finally, return 2 list record the number of flush and pair respectively
    def flush_pair_chance(self,number_exp):
        result_list=[]
        # user specify how many times to run the experiment
        for times in range(number_exp):
            num_pair = 0
            num_flush = 0
        # run a thousand times
            for i in range(1000):

                drawn_card_list = []
                # draw five random cards from deck
                for j in range(5):
                    self.deck.shuffle()
                    drawn_card_list.append(self.deck.draw_random_card())
                # if they are flush, number of flush +1; if they contain pairs,
                # number of pair + 1
                if self.is_flush(drawn_card_list):
                    num_flush+=1

                if self.contain_pair(drawn_card_list):
                    num_pair+=1
                # put the removed cards back in the random location of the deck
                for i in drawn_card_list:
                    self.deck.add_random_card(i)
            result_list.append((num_flush,num_pair))
        #seperate the number of flush and pair from result list
        num_flush=[i[0] for i in result_list]
        num_pair=[j[1] for j in result_list]
        return num_pair,num_flush


    # used the data from function--flush_pair_chance to draw the bar graph
    # x-axis: the nth time experiment
    # y-axis: occurrence time of flush or pair
    def draw_flush_pair_chance(self,number_exp):
        num_pair,num_flush=self.flush_pair_chance(number_exp)

        #draw bar graph for flush
        #x-axis
        x1=range(1,number_exp+1)
        plt.bar(x1,num_flush)
        plt.xlabel('the nth experiment time')
        plt.ylabel('flush appearance times')
        plt.title('There are '+str(self.num_suit)+' suits, '+'drawing 5 cards for 1000 times ')
        ##show the occurrence of flush on top of the bar graph
        for x,y in zip(x1,num_flush):
            plt.text(x-0.05,y,str(y))
        plt.show()
        print('Possibility of drawing a flush from '+str(self.num_suit)+' suits is '+self.result_string(num_flush))

        #draw bar graph for pair
        #x-axis
        x2 = range(1,number_exp+1)
        plt.bar(x1, num_pair)
        plt.xlabel('the nth experiment time')
        plt.ylabel('pair appearance times')
        plt.title('There are '+str(self.num_suit)+' suits, '+'draw 5 cards for 1000 times ')
        #show the occurrence of pair on top of the bar graph
        for x, y in zip(x1, num_pair):
            plt.text(x - 0.1, y + 0.2, str(y))
        plt.show()

        print('Possibility of drawing a pair from '+str(self.num_suit)+' suits is '+self.result_string(num_pair))

    #given the start value of suit and end value of suit , return the two lists record number of
    #apperance of pair and flush during the number of suit is changing
    def change_in_chance(self,start_value,end_value):
        res_list=[]
        for suit in range(start_value,end_value+1):
            #for each number of suit ,run the experiment once
            res_list.append(Card_analysis(suit).flush_pair_chance(1))
        num_flush=[i[1][0] for i in res_list]
        num_pair=[j[0][0] for j in res_list]
        return num_flush,num_pair


    # used the data from function--change_in_chance to draw the scatter graph
    # x-axis: the number of suit
    # y-axis: possibility of drawing a flush or pair
    def draw_change_in_chance(self,start_value,end_value):
        num_flush,num_pair=self.change_in_chance(start_value,end_value)
        #create list to record the possibility to draw a flush and pair
        pos_flush=[i/1000 for i in num_flush]
        pos_pair=[j/1000 for j in num_pair]
        #x-axis
        x1=range(start_value,end_value+1)
        x2=range(start_value,end_value+1)
        plt.scatter(x1,pos_flush)
        plt.scatter(x2,pos_pair)
        for x, y in zip(x1, pos_pair):
            plt.text(x-0.2 , y+0.01 , str(y))
        for x, y in zip(x2, pos_flush):
            plt.text(x -0.2, y+0.01 , str(y))
        plt.xlabel('the number of suits')
        plt.ylabel('possibility')
        plt.xticks(x1)
        plt.title( 'possibility of drawing 5 cards and get pair or flush ')
        plt.legend(('draw flush','draw pair'))
        plt.show()

    #print the deck
    def __str__(self):
        return str(self.deck)



def main():
    a=Card_analysis(4)
    print(a)

if __name__ == '__main__':
    main()

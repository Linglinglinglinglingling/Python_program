from deck import Deck
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

the_deck=Deck(1,13,4)
sum_face=0
#number of occurrence
new_list=[0]*13
num_occurrence=new_list[:]
#each loop, shuffle deck, draw card--add the value to sum and its occurrence +1
for i in range(1000):
    the_deck.shuffle()
    drawn_card=the_deck.draw_random_card()
    sum_face+=drawn_card.get_face()
    #occurrence time of drawn card +1
    num_occurrence[drawn_card.get_face()-1]+=1
    the_deck.add_random_card(drawn_card)


the_dataframe=pd.DataFrame({ 'Occurrence times':num_occurrence})
#set X-axis
card_list=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
the_dataframe.index = np.array(card_list)
the_dataframe.plot(kind='bar',title='occurrence times of each card',color=['blue'])
plt.legend(loc="upper center")
#set max value of y-axis to 100
plt.axis([None,None,0,100])
plt.show()


print('The average face value is:',str(sum_face)+'(sum of face value)'+'/'+'1000(times) =',sum_face/1000)




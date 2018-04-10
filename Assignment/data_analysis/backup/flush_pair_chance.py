from deck import Deck
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a_deck=Deck(1,13,4)
num_pair=0
num_flush=0
# run a thousand times
for i in range(1000):
    drawn_card_list=[]
    #draw five random cards from deck
    for j in range(5):
        a_deck.shuffle()
        drawn_card_list.append(a_deck.draw_random_card())
    if drawn_card_list




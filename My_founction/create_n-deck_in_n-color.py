def deck(number_of_suit,*color):

    num_color=len(color)
    deck=[(j,color[i%num_color]) for i in range(number_of_suit) for j in range(1,14)]
    print(deck)

if __name__ == '__main__':

    deck(6,'h','c','s')
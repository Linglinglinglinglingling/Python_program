import create_null_list

def deal(deck,*player):
    number_of_player=len(player)
    #create list [[],[],....]
    play_list=create_null_list.create_empty_list(number_of_player)
    #i used to shift between player_list
    i=0
    for item in deck:
        play_list[i%number_of_player].append(item)
        i+=1

    #print player 1--number of play
    n=0
    for i in player:
        print('player'+i+str(play_list[n]))
        n+=1

if __name__ == '__main__':
    a=[(i,j)for i in range(1,14) for j in ['a','b','c']]
    deal(a,'a','b','c','d')



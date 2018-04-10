#
class Tictactoe:
    def __init__(self):
        self.board=[[None,None,None],[None,None,None],[None,None,None]]
        self.step=0
        self.flag=0
        self.end=False

    #get the item from row ,column
    def get(self,row,column):
        return self.board[row-1][column-1]

    def turn(self):
        self.flag=self.step%2
        if self.flag:    #first player use x
            return 'x'
        else:
            return 'o'


    #mutator
    def set(self,row,column):
        self.board[row-1][column-1]=self.turn()

    def move(self):
        self.step += 1
        move=input('player'+str(self.flag+1)+' '+'please choose row and column  ')
        self.set(int(move[0]),int(move[1]))



    def __str__(self):
        return str(self.board[0])+'\n'+str(self.board[1])+'\n'+str(self.board[2])


    def gameover(self):
        for i in range(3):
            if self.board[i].count('x')==3 or self.board[i].count('o')==3:
                if self.get(i+1,1)=='x':
                    self.end=True
                    return print('player1 wins')
                else:
                    self.end = True
                    return print('player2 wins')

        for m in range(1,4):
            if self.get(1,m)!=None:
                if self.get(1,m)==self.get(2,m) and self.get(2,m)==self.get(3,m):
                    if self.get(1,m)=='x':
                        self.end= True
                        return print('player1 wins')
                    else:
                        self.end = True
                        return print('player2 wins')

        if self.get(1,1)==self.get(2,2)and self.get(2,2)==self.get(3,3):
            if self.get(1,1)=='x':
                self.end = True
                return print('player1 wins')
            if self.get(1, 1) == 'o':
                self.end = True
                return print('player2 wins')

        if self.get(1,3)==self.get(2,2)and self.get(2,2)==self.get(3,1):
            if self.get(1,3)=='x':
                self.end = True
                return print('player1 wins')
            if self.get(1, 3) == 'o':
                self.end = True
                return print('player2 wins')

    def clearboard(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j]=None
        self.step = 0
        self.flag = 0
        self.end = False








    def play(self):
        while True:
            for i in range(9):
                self.move()
                print(self)
                self.gameover()
                if self.end==True:
                    break
            if self.end==False:
                print('Draw game')

            self.clearboard()





if __name__ == '__main__':
    game=Tictactoe()
    game.play()

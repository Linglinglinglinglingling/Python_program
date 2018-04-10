class Matrix_1:

    def __init__(self,length,width,empty=None):
        self.length=length
        self.width=width
        self.empty=empty

        self.board = []
        for i in range(width):
            self.board.append([empty] * length)


    #accessor
    def get(self,row,column):
        return self.board[row-1][column-1]

    #mutator
    def set(self,row,column,item):
        if row<=self.width and column<=self.length and row>0 and column>0:
            self.board[row-1][column-1]=item
        else:
            print('exceed limit')


    def __str__(self):
        output=''
       #for i in range(self.width):
            #output+=str(self.board[i]) + '\n'
        for i in range(self.width):
            for j in self.board[i]:
                output+=str(j)+'\t'
            output.strip('\t')
            output+='\n'
        return output



def main():

    a=Matrix_1(3,4,'G')
    print(a.get(2,1))
    a.set(1,3,9)
    print(a)


if __name__ == '__main__':
    main()


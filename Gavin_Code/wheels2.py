class Wheels:

    def __init__(self):
        self.wheelSet = [0,0,0,0]
        self.type = "Black"

    def __str__(self):
        return str(self.wheelSet)

    #Puts condition tyre in slot wheelNumber
    #condition is a number
    #wheel number is an integer
    def changeTyre(self,wheelNumber,condition):
        if(wheelNumber > -1):
            if (wheelNumber < len(self.wheelSet)):
                self.wheelSet[wheelNumber] = condition

def main():
    pass

if __name__ == "__main__":
    main()
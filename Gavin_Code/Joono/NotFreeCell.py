from Gavin_Code.Joono.deck1 import Deck

# Define NotFreeCell class which could call the deck class and implements the rules of freecell.

class NotFreeCell:

# define __init__ method to store the instance variables
    def __init__(self):

# define self.removecard which is used to record the card when the card is removed on the board.
        self.removedcard = ""

# define self.operation which is used to record the operation that users input.
        self.operation = "G"

# define self.goback which is used to judge the operation whether it is allowable.
        self.goback = False

# define self.columns which is used to store every column cards in cascade
        self.columns = []

# define self.recordnum which is used to record the number of the last getting card operation
        self.recordnum = ""

# define self.recordarea which is used to record the area of the last moving card operation
        self.recordarea = ""

# define self.slotlist which is used to store the card in the slot
        self.slotlist = ["##", "##", "##", "##"]

# define self.present_foundation which is used to present the current top card of foundation in board
        self.present_foundation = ["**", "**", "**", "**"]

# define self.the_foundation which is used to store the cards in foundation.
        self.the_foundation = [[], [], [], []]

# call the Deck class to generate 4 suits cards which are from Ace to King
        get_card_from_deck = Deck(1, 14, 4)
# call the Deck method shuffle_the_card() to let the cards randomly
        get_card_from_deck.shuffle_the_card()
# call the Deck instance attribute card_list, and store the list to random_cards
        random_cards = get_card_from_deck.card_list

# slice the random_cards to 8 columns
        col1 = random_cards[0:7]
        col2 = random_cards[7:14]
        col3 = random_cards[14:21]
        col4 = random_cards[21:28]
        col5 = random_cards[28:34]
        col6 = random_cards[34:40]
        col7 = random_cards[40:46]
        col8 = random_cards[46:52]

# store these columns to instance varialbe self.columns
        self.columns = [col1, col2, col3, col4, col5, col6, col7, col8]

# define a method transpose which is used to present the self.columns list to vertical view
    def transpose(self):

# define a variable empty to store a space " "
        empty = "  "

# define a variable red to store the string colour
        red = "\033[31m"

# define a variable black to store the string colour
        black = '\033[30m'

# define a list theCascade which is used to store the transposed self.columns list
        theCascade = []

# define a variable t which is used for while loop
        t = 0

# use while loop to generate a 8(columns) * 25(rows) string
        while t < 25:
            theCascade.append([empty] * 8)
            t += 1

# use for loop to store the self.columns elements as a vertical way.
        for stack_ndx, stack in enumerate(self.columns):
            for card_ndx, card in enumerate(stack):
                theCascade[card_ndx + 1][stack_ndx] = str(card)

# define check_space to store a string " "
        check_space = "  "

# new_list to store slotlist and present_foundation list
        new_list = self.slotlist + self.present_foundation

# theCascade[0] is assigned with new_list
        theCascade[0] = new_list

# define board_position as a "" which is used to print
        board_postion = ""

# use for loop to generate the game board
        for row in theCascade:

# this if statement is used to filter the list which only contains the " " string
            if row.count(check_space) != 8:
                for item in row:

# this if statement is used to judge the colour of the card, and add corresponding colour to them
                    if item[0] in "DH":
                        board_postion += "[" + red + str(item) + black + "]" + "\t"

                    else:
                        board_postion += "[" + str(item) + "]" + "\t"

                board_postion += "\n"

        return board_postion


# overload __str__ metho to let the instance becoming the str
    def __str__(self):

        return self.transpose()


# define start method which is used to start the game
    def start(self):

# define a variable operation assigned with "", which is used to store the user's command
        operation = ""

# define a command_line to list the valid command
        command_line = ["GF", "GS", "GC", "MF", "MS", "MC"]

# define a while loop to start the game and judge it when the game will end.
        while (not self.gameover()) and ("Q" not in operation):

# call the moveback method when the user input invalid command, it will be activated.
            self.moveback()

# print the column index
            print("-01-    -02-    -03-    -04-    -05-    -06-    -07-    -08-   <<---column number")
            print(" ^^      ^^      ^^      ^^      ^^      ^^      ^^      ^^ ")

# present the board
            print(self)

# print the instruction of the vaild commands
            print("Command: |{GC--Get card from cascade} | {GF--Get card from foundation} | {GS--Get card from slots} |")
            print("\t\t " + "|{MC--Move card to cascade}  | {MF--Move card to foundation}  | {MS--Move card to slots}  |")

# use the operation variable to store the user inputting command
            operation = input("What kinds of Command do you want to use? ").upper()

# use if-else statements to judge the command whether it is vailid or not.
            if operation in command_line:

# use if-else statements to judge the command whether it is same as the last command, only compare with "G" and "M"
                if operation[0] == self.operation:

# if the opeartion is valid, the operation will be transferred to command method.
                    self.command(operation)

                else:
                    print("Invalid operation")

            else:
                print("Please input your opeartion again:")
                continue

# if the gameover method returns True, the game will end as a result of victory
        if self.gameover():
            print("Congradualation. You win the game")

# if the users input "Q", the game will end as "quit".
        else:
            print("You quit the game")

# This method is used to parse the command from users inputting and call the correspond method to implement the operation

    def command(self, operation):

# If the opeartion[0] is "G", then it will judge the area
        if operation[0] == "G":

# If the operation[1] is "C", then it will require the users to input a number of the column
            if operation[1] == "C":

# define gnum1 which is used to store the column number that the users want to get
                gnum1 = input("In cascade, which column card do you want to get? ")

# judge the gnum1 domain which is from 1 to 8.
                if int(gnum1) < 9 and int(gnum1) > 0:

# call the method cascade_get
                    self.cascade_get(gnum1)

# let the recordnum to store gnum1
                    self.recordnum = gnum1

                else:
                    print("Out of the casde range")

# If the operation[1] is "S", then it will require the users to input a number of the Slot
            elif operation[1] == "S":

# define gnum2 which is used to store the slot number that the users want to get
                gnum2 = input("In slot, which cell card do you want to get? ")

# judge the gnum1 domain which is from 1 to 4.
                if int(gnum2) < 5 and int(gnum2) > 0:

# call the method slots_get
                    self.slots_get(gnum2)

# let the recordnum to store gnum2
                    self.recordnum = gnum2

                else:
                    print("Out of the casde range")

# If the operation[1] is "F", then it will require the users to input a number of the Foundation
            elif operation[1] == "F":

# define gnum3 which is used to store the foundation number that the users want to get
                gnum3 = input("In foundation, which foundation card do you want to get? ")

# judge the gnum1 domain which is from 1 to 4.
                if int(gnum3) < 5 and int(gnum3) > 0:

# call the method foundation_get
                    self.foudation_get(gnum3)

# let the recordnum to store gnum3
                    self.recordnum = gnum3

                else:
                    print("Out of the casde range")

# If the opeartion[0] is "M", then it will judge the area
        if operation[0] == "M":

# If the operation[1] is "C", then it will require the users to input a number of the column
            if operation[1] == "C":

# define mnum1 which is used to store the column number that the users want to move
                mnum1 = input("In cascade, which column do you want to move? ")

# call the method cascade_move
                self.cascade_move(mnum1)

# If the operation[1] is "S", then it will require the users to input a number of the Slot
            elif operation[1] == "S":

# define mnum2 which is used to store the number that the users want to move
                mnum2 = input("In slots, which one do you want to move? ")

# call the method slots_move
                self.slots_move(mnum2)

# If the operation[1] is "F", then it will require the users to input a number of the Foundation
            elif operation[1] == "F":

# define mnum3 which is used to store the number that the users want to move
                mnum3 = input("In foundation, which one do you want to move? ")

# call the method foundation_move
                self.foundation_move(mnum3)

# This method means getting card from a specific column in the cascade
    def cascade_get(self, gnum1):

# define 'cn1' which is used to store the valid columns index.
        cn1 = int(gnum1) - 1

# "if" statement is used to check whether the column has card or not.
        if len(self.columns[cn1]) != 0:

# let the removedcard to store the last card of the one of the columns
            self.removedcard = self.columns[cn1][len(self.columns[cn1]) - 1]

# In columns[cn1] list, pop the last item of it.
            self.columns[cn1].pop()

# change the self.operation to "M", which will be used to check the next operation
            self.operation = "M"

# self.recordare is used to record the area First character
            self.recordarea = "C"
        else:
            print("Invalid operation: There is no card for you to get")

# This method means moving the card to a specific column in the cascade.
    def cascade_move(self, mnum1):

# define a variable 'cn2' which will store the valid column index.
        cn2 = int(mnum1) - 1

# define a variable 'lencolumn' which will store the length of the specific column
        lencolumn = len(self.columns[cn2])

# deifne 'dicn' which is used to store the card face from Ace to King.
        dicn = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12,"K": 13}

# if 'lencolumn' doesn't equal to 0, it will judge the card whether it follow the rules fo freecell.
        if lencolumn != 0:

# judge the colour (red or black)
            if (self.removedcard[0] in "SC") and (self.columns[cn2][lencolumn - 1][0] in "DH"):

# judge the order
                if (dicn[self.removedcard[1]] + 1) == (dicn[self.columns[cn2][lencolumn - 1][1]]):
                    self.columns[cn2].append(self.removedcard)
                    self.operation = "G"

                else:
                    print("It is disorder operation in cascade")
                    self.goback = True

# judge the colour (red or black)
            elif (self.removedcard[0] in "DH") and (self.columns[cn2][len(self.columns[cn2]) - 1][0] in "SC"):

# judge the order
                if (dicn[self.removedcard[1]] + 1) == (dicn[self.columns[cn2][lencolumn - 1][1]]):
                    self.columns[cn2].append(self.removedcard)
                    self.operation = "G"

                else:
                    print("It is disorder operation in cascade")
                    self.goback = True

            else:
                print("Invalid operation in cascade: Colour should be different")
                self.goback = True

# if the column doesn't have any cards, it will append any single card.
        else:
            self.columns[cn2].append(self.removedcard)
            self.operation = "G"

# This method means getting card from a specific cell in the slots.
    def slots_get(self, gnum2):

# define a variable 'sln1' which will store the gnum2 in numeric data type.
        sln1 = int(gnum2)

# define 'slng' which means the getting slotslist index
        slng = sln1 - 1

# if the card could be removed from slots, it will show "##" in front of the users, which means empty.
# Additionally, the 'slotlist' will pop the card.
        if (sln1 > 0) and (sln1 < 5):
            if (self.slotlist[slng] != "##"):
                self.removedcard = self.slotlist[slng]
                self.slotlist[slng] = "##"
                self.operation = "M"
                self.recordarea = "S"

            else:
                print("There is no card for you ")
        else:
            print("Invalid operation: Out of the slots getting range")

# This method means moving the card to a specific cell of the slot.
    def slots_move(self, mnum2):

# define a variable 'sln2' which will store the mnum2 in numeric data type.
        sln2 = int(mnum2)

# define 'slne' which means the existed slotslist index
        slne = sln2 - 1

# if the card could be moved to slots, the card will be stored in 'slotlist' and the "##" will be replaced.
        if sln2 > 0 and sln2 < 5:
            if self.slotlist[slne] == "##":
                self.slotlist[slne] = self.removedcard
                self.operation = "G"

# if the moving operation can't excute sucessfully, self.goback will be assigned with True
# Furthermore, the moveback method will be activated, and the card that users get will go back to the former position
            else:
                print("You cannot put a card in here because there is a card in here")
                self.goback = True
        else:
            print("Invalid operation: Out of the slots moving range")

# This method means getting the card from a specific cell of the foundation.
    def foudation_get(self, gnum3):

# define a variable 'findx1' which is used to store the_foundation list index
        findx1 = int(gnum3) - 1

# define 'no_foundation1' which is used to store a single foundation list.
        no_foundation1 = self.the_foundation[findx1]

# define 'count1' which is used to store the length of the single foundation list.
        count1 = len(no_foundation1)

# define "top1" which is used to store the last card index in the single foundation list
        top1 = count1 - 1

# if "count1" is 1, it means that when get a card from this foundation list, it will show "**" in front of users
# Additionally, the single foundation list will pop the last card.
        if count1 == 1:
            self.removedcard = self.the_foundation[findx1][top1]
            self.the_foundation[findx1].pop()
            self.present_foundation[findx1] = "**"
            self.operation = "M"
            self.recordarea = "F"

# if count1 > 1, it will execute getting operation, so the single foundation list will pop the last card
# Additionally, the single foundation list will present the [top1-1] card in front of the users
        elif count1 > 1:
            self.removedcard = self.the_foundation[findx1][top1]
            self.the_foundation[findx1].pop()
            self.present_foundation[findx1] = self.the_foundation[findx1][top1 - 1]
            self.operation = "M"
            self.recordarea = "F"

        else:
            print("Invalid operation: there is no card for you to get")

# This method means moving the card to a specific cell of the foundation.
    def foundation_move(self, mnum3):

# define "findx" to store the foundation valid index
        findx = int(mnum3) - 1

# define "no_foundation" which is used to store a single foundation list.
        no_foudation = self.the_foundation[findx]

# define "count" varirable which is used to store the length of the single foundation list.
        count = len(no_foudation)

# define "top" which is used to store the last card index in the single foundation list
        top = count - 1

# define 'dicf' which is used to store the card face from Ace to King.
        dicf = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13}

# In foundation, the first card should be Ace, so when the foundation is empty, only Ace can be put in.
        if count == 0:
            if self.removedcard[1] == "A":
                no_foudation.append(self.removedcard)
                self.present_foundation[findx] = self.removedcard
                self.operation = "G"

# if the card can't put into the foundation, the goback method will be activated
            else:
                print("Invalid operation, you can only put Ace in here")
                self.goback = True

# place the card on foundation from 1 to 13 in order
        elif (count > 0) and (count < 14):
            if dicf[self.removedcard[1]] == (count + 1):
                if self.removedcard[0] == no_foudation[top][0]:
                    no_foudation.append(self.removedcard)
                    self.present_foundation[findx] = self.removedcard
                    self.operation = "G"

# if the card can't put into the foundation, the goback method will be activated
            else:
                print("Invalid operation, you cannot put another colour {} in here".format(self.removedcard))
                self.goback = True

# if the card can't put into the foundation, the goback method will be activated
        else:
            print("It is disorder")
            self.goback = True

# This method is used to let the card back when users input no allowable command.
    def moveback(self):

# when self.goback is True, the the while loop will be excuted.
        while self.goback:

# when self.recordare is "C", the removed card will go back to the former place
            if (self.recordarea == "C"):
                self.columns[int(self.recordnum) - 1].append(self.removedcard)
                self.operation = "G"
                self.goback = False
                break

# when self.recordare is "S", the removed card will go back to the former place
            elif (self.recordarea == "S"):
                self.slotlist[int(self.recordnum) - 1] = self.removedcard
                self.operation = "G"
                self.goback = False
                break

# when self.recordare is "F", the removed card will go back to the former place
            elif (self.recordarea == "F"):
                self.the_foundation[int(self.recordnum) - 1].append(self.removedcard)
                self.present_foundation[int(self.recordnum)-1] = self.removedcard
                self.operation = "G"
                self.goback = False
                break


# this method is used to let the users know when the game has ended as a result of victory.
    def gameover(self):

# define a list 'computation' which is used to record the length of every foundation cell
        computation = []
        for single_foundation in self.the_foundation:
            computation.append(len(single_foundation))

# if the length of every foundation is 13, the method will return True.
        return computation == [13, 13, 13, 13]


if __name__ == '__main__':
    a = NotFreeCell()
    a.start()


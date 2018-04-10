#
from card import Card
from deck import Deck
from slot import Slot
from foundation import Foundation
from cascade_deck import Cascade_deck
import pickle


class Notfrecell:
    # Notfreecell comprise of 4 slots, 4 foundations, 8 cascade_deck, 1 deck
    def __init__(self):
        self.slot_0 = Slot()
        self.slot_1 = Slot()
        self.slot_2 = Slot()
        self.slot_3 = Slot()

        self.foundation_0 = Foundation()
        self.foundation_1 = Foundation()
        self.foundation_2 = Foundation()
        self.foundation_3 = Foundation()

        self.cascade_deck_0 = Cascade_deck()
        self.cascade_deck_1 = Cascade_deck()
        self.cascade_deck_2 = Cascade_deck()
        self.cascade_deck_3 = Cascade_deck()
        self.cascade_deck_4 = Cascade_deck()
        self.cascade_deck_5 = Cascade_deck()
        self.cascade_deck_6 = Cascade_deck()
        self.cascade_deck_7 = Cascade_deck()

        self.deck = Deck(1, 13, 4)

        # lists that contain the all objects from the same class
        self.list_slot = [self.slot_0, self.slot_1, self.slot_2, self.slot_3]

        self.list_foundation = [self.foundation_0, self.foundation_1,
                                self.foundation_2, self.foundation_3]

        self.list_cascade_deck = [self.cascade_deck_0, self.cascade_deck_1,
                                  self.cascade_deck_2, self.cascade_deck_3,
                                  self.cascade_deck_4, self.cascade_deck_5,
                                  self.cascade_deck_6, self.cascade_deck_7]

    # translate user's input to correspond component.e.g. SO means Slot_0
    def position_translate(self, position):
        list_position = ['S0', 'S1', 'S2', 'S3', 'F0', 'F1', 'F2', 'F3', 'C0',
                         'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7']
        list_notfreecell = self.list_slot + self.list_foundation + self.list_cascade_deck
        position_dict = dict(list(zip(list_position, list_notfreecell)))
        return position_dict[position]

    # shuffle deck , then deal the card in the order that C0-C7, then from C0 again
    def deal(self):
        self.deck.shuffle()
        cascade_deck_number = 0
        for i in self.deck.get_deck():
            self.list_cascade_deck[cascade_deck_number % 8].append_card(i)
            cascade_deck_number += 1

    # the position that user need to input is like S0,F1,C5, represent slot_0
    # foundation_1,cascade_deck_5 respectively. The from_position means topmost
    # card in which position is to be moved, to_position means move card to which position
    def move_card(self, from_position, to_position):
        removed_card = self.position_translate(from_position).remove_card()
        # if the removed action is invalid,stop the function
        if removed_card == False:
            return None
        flag = self.position_translate(to_position).add_card(removed_card)
        # if the add_card action is invalid, return the removed card back to where it was
        if flag == False:
            self.position_translate(from_position).append_card(removed_card)
            return None

    # check user's input
    def move_check(self, move):
        if move in ['S0', 'S1', 'S2', 'S3', 'F0', 'F1', 'F2', 'F3', 'C0',
                    'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7']:
            return True
        else:
            return False

    # if length of all foundation equal 13, then win
    def game_win(self):
        if self.foundation_0.length_foudation() == 13 and \
                        self.foundation_0.length_foudation() == 13 and \
                        self.foundation_0.length_foudation() == 13 and \
                        self.foundation_0.length_foudation() == 13:
            return True
        else:
            return False

    # max length of all cascade_deck
    def max_length(self):
        self.list_of_length = []
        for j in self.list_cascade_deck:
            self.list_of_length.append(j.length_cascade_deck())
        return max(self.list_of_length)

    def __str__(self):
        display_notfreecell = 'S0' + '\t' + 'S1' + '\t' + 'S2' + '\t' + 'S3' + '\t' \
                                                                               'F0' + '\t' + 'F1' + '\t' + 'F2' + '\t' + 'F3' + '\n'
        # print all slot in one line
        for n in self.list_slot:
            display_notfreecell += str(n) + '\t'
        # print all foundation in the same line
        for m in self.list_foundation:
            display_notfreecell += str(m) + '\t'
        display_notfreecell += '\n' + '\n'
        display_notfreecell += 'C0' + '\t' + 'C1' + '\t' + 'C2' + '\t' + 'C3' + '\t' \
                                                                                'C4' + '\t' + 'C5' + '\t' + 'C6' + '\t' + 'C7' + '\n'

        # start from first row, print each cascade_deck's first item
        # then ..... second...............................second item until reach the max length of all cascade_deck
        for row in range(self.max_length()):
            for item in self.list_cascade_deck:
                # if index out of range, display '   '
                if row >= item.length_cascade_deck():
                    display_notfreecell += '   ' + '\t'
                else:
                    display_notfreecell += str(item.get_cascade_deck(row)) + '\t'
            display_notfreecell += '\n'
        # change the color back to normal
        return display_notfreecell

    # just save the board
    def save_game(self):
        saved_game = open('saved_file.txt', 'w')
        saved_game.write(str(self))
        saved_game.close()


def main():
    game = Notfrecell()
    game.deal()
    win = False
    while not win:
        print(game)
        valid_input = False
        while not valid_input:
            from_position = input('please input the position of card that you want to move:  ' + '\n' \
                                                                                                 'You can also press q to leave or r to restart or s to save the game or l to reload ')
            # input q then quit the game
            if from_position == 'q':
                return None
            # input r then restart the game
            if from_position == 'r':
                return main()
            if from_position == 's':
                # game.save_game()
                with open('saved_file.txt', 'wb') as f:
                    pickle.dump(game, f)
                continue

            if from_position == 'l':
                with open('saved_file.txt', 'rb') as f:
                    game = pickle.load(f)
                print(game)
                continue
            to_position = input('please input the position that you want the card to move to:  ')
            # if user's inputs are valid ,game continue; Otherwise input the position again
            if game.move_check(from_position.upper().strip()) and \
                    game.move_check(to_position.upper().strip()):
                valid_input = True
            else:
                print('\n' + '\n' + 'please input the valid position' + '\n' + '\n')
                print(game)

        game.move_card(from_position.upper().strip(), to_position.upper().strip())
        if game.game_win():
            print('You Win!!')
            win = True
    # user input q to quit or r to restart the game
    while True:
        end_game = input('You can also press q to leave or r to restart  ')
        if end_game == 'q':
            return None

        if end_game == 'r':
            return main()


if __name__ == '__main__':
    main()

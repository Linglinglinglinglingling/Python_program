class TicTacToe:
    
    # if we visualize the tic tac toe gird as position values like
    #  [ 1 2 3 ]
    #  [ 4 5 6 ]
    #  [ 7 8 9 ]
    # the following list store the set of winning positions
    win_pos = [{1, 2, 3},
               {4, 5, 6},
               {7, 8, 9},
               {1, 4, 7},
               {2, 5, 8},
               {3, 6, 9},
               {1, 5, 9},
               {3, 5, 7}]

    # dictionary that maps each positional value to i,j values of the grid matrix
    board = dict([(1, (0, 0)),
                  (2, (0, 1)),
                  (3, (0, 2)),
                  (4, (1, 0)),
                  (5, (1, 1)),
                  (6, (1, 2)),
                  (7, (2, 0)),
                  (8, (2, 1)),
                  (9, (2, 2))])

    # the number of elements in grid
    grid_size = 9

    # dictionary that maps a player to his marker
    player_marker = {'p1': 'x', 'p2': 'o'}

    def __init__(self):
        """
        Object initializer with variables
        * played_pos : list to store the history of played positions
        * grid : initial grid state
        * player_played_pos : dictionary to map a player to his played positions initialized as empty set for players
        """
        self.played_pos = []
        self.grid = [['-', '-', '-'],
                     ['-', '-', '-'],
                     ['-', '-', '-']]
        self.player_played_pos = {'p1': set(), 'p2': set()}

    def __str__(self):
        """"
        Overriding string representation of TicTacToe object
        """
        grid_str = ""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                grid_str = grid_str + self.grid[i][j] + '\t'
            grid_str = grid_str.strip('\t')
            grid_str = grid_str + '\n'
        return grid_str

    def check_win(self, player):
        """
        Method to check whether the player has marked his marker in any of the winning positions
        :param player: the player for which we check whether he won or not
        :return: True if the player win, else False
        """
        for win_pos in TicTacToe.win_pos:
            # for each winning position defined we take the set difference to the positions played be player
            # if there are not elements left after resulting set after difference operator
            # we get False as return. ie he has placed his marker in the winning positions which in turn makes him
            # the winner
            if not win_pos.difference(self.player_played_pos[player]):
                return True

        # if after checking for every winning positions if the control still reaches here,
        # the player has not marked the winning positions. returns False
        return False

    def mark_pos(self, position, marker):
        """
        Method to mark a grid position with specified marker
        :param position: positional value which ranges from 1 to 9
        :param marker: the player marker
        :return: None
        """
        i, j = self.board[position]
        self.grid[i][j] = marker

    def play(self, player, position, whos_play):
        """
        Method to execute a play for a player in a position
        :param player: the player who is making the move
        :param position: the position he played
        :param whos_play: boolean: if True the player is p1 else p2
        :return: pair of booleans to represent whether all the positions has been played and whose turn is next
        """

        # check if the position has already been marked
        if position not in self.played_pos:

            # mark the position with players marker
            self.mark_pos(position, TicTacToe.player_marker[player])

            # keep the played position in history of played position
            self.played_pos.append(position)

            # keep the position played by player
            self.player_played_pos[player].add(position)

            # print the current state of the game
            print(self)

            # after the move, check if the player won the game. If so exit the program
            if self.check_win(player):
                print("{} wins".format(player))
                exit(0)

            # check if all the positions in grid have been played. If so game is a draw.
            # returns True for is_all_moves_over variable.
            if len(self.played_pos) == TicTacToe.grid_size:
                return True, not whos_play

            # if the method doesnt return till now, return False for is_all_moves_over
            # and reverses the p1_move variable in calling method to indicate move of the next person.
            return False, not whos_play

        else:
            print("Position already played.. player {} play again..".format(player))

            # if the play is invalid, indicate that the game is still on, but doesnt invert the p1_move in the
            # calling method which force the same player to play again
            return False, whos_play

    def start_game(self):
        """
        Starting point of the game.
        Initializes the first player as p1
        Initializes the is_all_moves_over to False indicating that the game is not over
        :return: None
        """
        p1_move = True
        is_all_moves_over = False
        while not is_all_moves_over:

            while p1_move and not is_all_moves_over:
                p1 = int(input("Player 1 pos:"))
                is_all_moves_over, p1_move = self.play('p1', p1, p1_move)

            while not p1_move and not is_all_moves_over:
                p2 = int(input("Player 2 pos:"))
                is_all_moves_over, p1_move = self.play('p2', p2, p1_move)

        print("Game Ended in Draw")


tic_tac_toe = TicTacToe()
print("Starting game....")

# print the initial state of the game
print(tic_tac_toe)

# starting the game
tic_tac_toe.start_game()

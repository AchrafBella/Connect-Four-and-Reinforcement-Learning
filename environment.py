import numpy as np


class Env:
    def __init__(self, dimension=(6, 7)):
        """
        this class create the game environment
        we have to respect that the first drop of peace should be in the deep
        also the game is over when one player get 4 peaces or the board left with 0 vacant column
        :param dimension: the dimension represent the board limits
        """
        self.dimension = dimension
        self.board = np.zeros(dimension)
        self.game_over = False

    def get_state(self):
        return self.board

    def get_game_state(self):
        return self.game_over

    def drop_peace(self, row, column, peace):
        """
        this function will put an element in board using the agent
        :param row:
        :param column:
        :param peace:
        :return:
        """
        if row>6 or row<0 or column>7 or column<0:
            raise Exception("Please check where you put your peace")
        self.board[row][column] = peace

    def is_valid_location(self, row, column):
        """

        :param row:
        :param column:
        :return:
        """
        return

    def is_done(self):
        """
        in this function we are going to check if all the value are full then game is over,
        we are going to check if there is 4 peaces vertically then game is over,
        we are going to check if there is 4 peaces  negatively sloped diagonals then game is over
        we are going to check if there is 4 peaces  positively sloped diagonals then game is over
        :return:
        """
        # check for if there's no place
        if self.board.any():
            self.game_over = True
        else:
            # check for vertical location
            for i in range(self.dimension[0]):
                for j in range(self.dimension[1]-3):
                    if self.board[j][i] != 0 and self.board[j+1][i] != 0 and self.board[j+2][i] != 0 \
                            and self.board[j+3][i] != 0:
                        self.game_over = True
                        pass
                    pass
                pass
            # check for horizontal location
            for i in range(self.dimension[0]-3):
                for j in range(self.dimension[1]):
                    if self.board[i][j] != 0 and self.board[i][j+1] != 0 and self.board[i][j+2] != 0 \
                            and self.board[i][j+3] != 0:
                        self.game_over = True
                        pass
                    pass
                pass
        return self.game_over


    def get_agent1_wins(self):
        pass

    def get_agent2_wins(self):
        pass

    def display_env(self):
        print(*self.board, sep='\n')

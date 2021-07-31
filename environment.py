import numpy as np


class Env:
    def __init__(self, dimension=(6, 7)):
        """
        this class create the game environment
        we have to respect that the first drop of peace should be in the deep
        also the game is over when one player get 4 peaces or the board left with 0 vacant column
        :param dimension: the dimension represent the board limits
        """
        self.__dimension = dimension
        self.__board = np.zeros(self.__dimension)
        self.__game_over = False
        self.__message = None

    def drop_piece(self, row, column, piece):
        """
        A specific function for agents
        :param row:
        :param column:
        :param piece:
        :return:
        """
        if self.__board[row][column] != 0:
            row -= 1
        self.__board[row][column] = piece

    def drop_manually_piece(self, column, piece, row=5):
        """
        this function will put an element in board using the agent
        :param row:
        :param column:
        :param piece:
        :return:
        """
        if row > 6 or row < 0 or column > 7 or column < 0:
            raise Exception("Please check where you put your peace")
        if not np.any(self.__board[self.__dimension[0] - 1] == 0):
            row -= 1
        if self.__board[row][column] != 0:
            row -= 1
            raise Exception("You can't put the peace at this position")
        self.__board[row][column] = piece

    def check_game_over(self):
        """
        in this function we are going to check if all the value are full then game is over,
        :return:
        """
        if not np.any(self.__board == 0):
            self.__game_over = True
            self.__message = 'Game is over no one won'

    def check_wining_move(self, agent):
        """
        we are going to check if there is 4 peaces vertically then game is over,
        we are going to check if there is 4 peaces  negatively sloped diagonals then game is over
        we are going to check if there is 4 peaces  positively&negatively sloped diagonals then game is over
        :param agent: the agent
        :return:
        """
        if self.__game_over:
            return

        # check vertical locations
        for r in range(self.__dimension[0] - 3):
            for c in range(self.__dimension[1]):
                if self.__board[r][c] == agent.get_piece() and self.__board[r + 1][c] == agent.get_piece() \
                        and self.__board[r + 2][c] == agent.get_piece() and self.__board[r + 3][c] == agent.get_piece():
                    self.__game_over = True
                    self.__message = agent.get_agent_name() + ' win with a 4 piece in vertical'
                    pass
                pass
            pass

        # check horizontal location
        for r in range(self.__dimension[0]):
            for c in range(self.__dimension[1] - 3):
                if self.__board[r][c] == agent.get_piece() and self.__board[r][c + 1] == agent.get_piece() \
                        and self.__board[r][c + 2] == agent.get_piece() and self.__board[r][c + 3] == agent.get_piece():
                    self.__game_over = True
                    self.__message = agent.get_agent_name() + ' win with a 4 piece in horizontal'
                    pass
                pass
            pass

        # check negative diagonal
        for r in range(self.__dimension[0]):
            for c in range(self.__dimension[1] - 3):
                if self.__board[r][c] == agent.get_piece() and self.__board[r - 1][c + 1] == agent.get_piece() \
                        and self.__board[r - 2][c + 2] == agent.get_piece() and self.__board[r - 3][c + 3] == \
                        agent.get_piece():
                    self.__game_over = True
                    self.__message = agent.get_agent_name() + ' win with a 4 piece in negative diagonal'
                    pass
                pass
            pass

        # check positive diagonal
        for r in range(self.__dimension[0] - 3):
            for c in range(self.__dimension[1] - 3):
                if self.__board[r][c] == agent.get_piece() and self.__board[r + 1][c + 1] == agent.get_piece() \
                        and self.__board[r + 2][c + 2] == agent.get_piece() and self.__board[r + 3][c + 3] == \
                        agent.get_piece():
                    self.__game_over = True
                    self.__message = agent.get_agent_name() + ' win with a 4 piece in positive diagonal'
                    pass
                pass
            pass

        return self.__game_over

    def get_agent1_wins(self):
        pass

    def get_agent2_wins(self):
        pass

    def get_dimension(self):
        return self.__dimension

    def get_observation(self):
        return self.__board

    def get_game_state(self):
        return self.__game_over

    def get_message(self):
        return self.__message

    def display_env(self):
        print(*self.__board, sep='\n')

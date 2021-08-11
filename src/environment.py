import numpy as np
import matplotlib.pyplot as plt


class Env:
    def __init__(self, agents, dimension=(6, 7)):
        """
        This class represent the game environment
        We have to respect that the first drop of piece should be in the bottom
        also the game is over when one player get 4 peaces or the board left with zero vacant column.

        The environment contains both the 2 players (agents)
        Each agents should at least have 2 attributes disk & agent_name (get_disk(), get_agent_name)
        and a function action with 2 parameters state & dimension that return row and column

        :param dimension: the dimension represent the board limits
        :param agents: dict of agents
        """
        self.__dimension = dimension
        self.__board = np.zeros(self.__dimension)
        self.__winner = None

        self.__agent1 = agents.get('agent1', None)
        self.__agent2 = agents.get('agent2', None)

    def reset_configuration(self):
        """
        :return:
        """
        self.__board = np.zeros(self.__dimension)
        self.__winner = None

    def __valid_location(self, row, column):
        """
        :param row:
        :param column:
        :return:
        """
        return self.__board[row][column] == 0

    def __get_next_valid_location(self, column):
        """
        :param column:
        :return:
        """
        for row in reversed(range(self.__dimension[0])):
            if self.__valid_location(row, column):
                return row

    def __drop_disk(self, row, column, piece):
        """
        :param row:
        :param column:
        :param piece:
        :return:
        """
        if self.__board[row][column] != 0:
            row -= 1
        self.__board[row][column] = piece

    def drop_disk_manually(self, piece):
        """
        :param piece:
        :return:
        """
        row = 5
        column = int(input('Your turn: please choose a column: '))
        if column >= 7 or column < 0 or np.all((self.__board != 0), axis=0)[column]:
            raise PieceMisplaced("Please check the column you want to put your piece in")
        if self.__valid_location(row, column):
            self.__board[row][column] = piece
        else:
            row = self.__get_next_valid_location(column)
            self.__board[row][column] = piece

    def check_game_over(self):
        """
         This function check if all the value are full, if it's the case then game is over.
        :return:
        """
        if not np.any(self.__board == 0):
            return True

    def check_wining_move(self, agent):
        """
        we are going to check if there is 4 peaces vertically then, game is over
        we are going to check if there is 4 peaces  horizontally sloped diagonals then, game is over
        we are going to check if there is 4 peaces  positively&negatively sloped diagonals then, game is over
        :param agent: the agent
        :return: boolean to know if we won the game or not yet
        """
        # check vertical locations
        for r in range(self.__dimension[0] - 3):
            for c in range(self.__dimension[1]):
                if self.__board[r][c] == agent.get_disk() and self.__board[r + 1][c] == agent.get_disk() \
                        and self.__board[r + 2][c] == agent.get_disk() and self.__board[r + 3][c] == agent.get_disk():
                    self.__winner = agent
                    return True
                pass
            pass

        # check horizontal location
        for r in range(self.__dimension[0]):
            for c in range(self.__dimension[1] - 3):
                if self.__board[r][c] == agent.get_disk() and self.__board[r][c + 1] == agent.get_disk() \
                        and self.__board[r][c + 2] == agent.get_disk() and self.__board[r][c + 3] == agent.get_disk():
                    self.__winner = agent
                    return True
                pass
            pass

        # check negative diagonal
        for r in range(self.__dimension[0]):
            for c in range(self.__dimension[1] - 3):
                if self.__board[r][c] == agent.get_disk() and self.__board[r - 1][c + 1] == agent.get_disk() \
                        and self.__board[r - 2][c + 2] == agent.get_disk() and self.__board[r - 3][c + 3] == \
                        agent.get_disk():
                    self.__winner = agent
                    return True
                pass
            pass

        # check positive diagonal
        for r in range(self.__dimension[0] - 3):
            for c in range(self.__dimension[1] - 3):
                if self.__board[r][c] == agent.get_disk() and self.__board[r + 1][c + 1] == agent.get_disk() \
                        and self.__board[r + 2][c + 2] == agent.get_disk() and self.__board[r + 3][c + 3] == \
                        agent.get_disk():
                    self.__winner = agent
                    return True
                pass
            pass

    def play_round(self):
        """
        * we should set who play first randomly
        * As the first player goes first we should check if he won and then assign the score
        * If the first player didn't won in his turn then we check for the second player and we assign the score
        * we set max_turn to 21 because the maximum number of vacant places is 42 and we play twice
        :return:
        """

        first_player = np.random.choice([self.__agent1, self.__agent2])
        second_player = self.__agent2 if first_player == self.__agent1 else self.__agent1
        max_turn = 21  # finite states

        for turn in range(max_turn):

            row1, col1 = first_player.action(self.__board, self.__dimension)
            self.__drop_disk(row1, col1, first_player.get_disk())

            # self.display_board()
            # print("_"*50)

            if self.check_wining_move(first_player):
                break

            row2, col2 = second_player.action(self.__board, self.__dimension)
            self.__drop_disk(row2, col2, second_player.get_disk())

            if self.check_wining_move(second_player):
                break
            # self.display_board()

            # self.round_result(first_player.get_agent_name(), turn, row1, col1)
            # self.round_result(second_player.get_agent_name(), turn, row2, col2)
            # print("_"*50)

        if first_player == self.__agent2 and second_player == self.__agent1:
            first_player, second_player = self.__agent1, self.__agent2

        return first_player, second_player

    def run(self, rounds=1):
        """
        The Run function for abject to see how the agent will do when they play many times
        * the utility represent the total of the reward (not discounted)
        :param rounds:
        :return: 2 list of cumulative rewards
        """
        winning_rounds_agent1, winning_rounds_agent2 = 0, 0
        draws = 0

        for _ in range(rounds):
            self.reset_configuration()

            agent1, agent2 = self.play_round()

            winning_rounds_agent1 = self.winning_rate(agent1, winning_rounds_agent1)
            winning_rounds_agent2 = self.winning_rate(agent2, winning_rounds_agent2)

            draws += 1 if self.check_game_over() else 0

        # information to track the rounds
        self.battle_result(self.__agent1.get_agent_name(),  self.__agent2.get_agent_name(),
                           (winning_rounds_agent1/rounds)*100, (winning_rounds_agent2/rounds)*100)
        print("In the total there is {} draws".format(draws))
        print("_"*100)

    def reward_visualization(self, reward1, reward2):
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.suptitle('Cumulative reward for both agents in the {}'.format(self.__class__))
        ax1.plot(reward1, 'tab:red')
        ax1.set_title('agent 1')
        ax1.set(xlabel='round', ylabel='reward')

        ax2.plot(reward2, 'tab:green')
        ax2.set_title('agent 2')
        ax2.set(xlabel='round', ylabel='reward')
        plt.show()

    def get_dimension(self):
        return self.__dimension

    def get_state(self):
        return self.__board

    def get_winner(self):
        return self.__winner

    def count_disks_in_board(self):
        return np.count_nonzero(self.__board)

    def display_board(self):
        print(*self.__board, sep='\n')

    def winning_rate(self, agent, winning_round):
        if agent == self.__winner:
            winning_round += 1
        return winning_round

    @staticmethod
    def round_result(agent_name, turn, row, col):
        s = 'The {} in his {} turn drop a piece in row={}, col={}'.format(agent_name, turn, row, col)
        print(s)

    @staticmethod
    def battle_result(agent1_name, agent2_name, winning_rate1, winning_rate2):
        s = '{} won {} % of battles & {} won {} of battles'.format(agent1_name, round(winning_rate1, 2), agent2_name,
                                                                   round(winning_rate2, 2))
        print(s)

    @staticmethod
    def statistic_score(cumulative_reward):
        s = 'the max {}, the min {}, the mean {}'.format(max(cumulative_reward), min(cumulative_reward),
                                                         np.mean(cumulative_reward))
        print(s)


class PieceMisplaced(Exception):
    """The piece misplaced please choose a column between 0 and 6"""
    pass

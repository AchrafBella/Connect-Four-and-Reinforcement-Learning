import numpy as np
import matplotlib.pyplot as plt


class Env:
    def __init__(self, dimension=(6, 7)):
        """
        This class represent the game environment
        we have to respect that the first drop of peace should be in the bottom
        also the game is over when one player get 4 peaces or the board left with zero vacant column

        For an DRL we need 3 function that will help us to create the Environment
        * Dimension: which is the input of our neural network
        * next_step: which is the next step and the output of the neural network
        * reward function: a function that reward or punch the agent depending on their action
        * reset function: that reset the game
        * step function: which is the action taken by the agent

        :param dimension: the dimension represent the board limits
        """
        self.__dimension = dimension
        self.__board = np.zeros(self.__dimension)
        self.__winner = None

    def __reset_configuration(self):
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
        :return: valid row
        """
        for row in reversed(range(self.__dimension[0])):
            if self.__valid_location(row, column):
                return row

    def __drop_piece(self, row, column, piece):
        """ Action
        A specific function for the agents
        :param row:
        :param column:
        :param piece:
        :return:
        """
        if self.__board[row][column] != 0:
            row -= 1
        self.__board[row][column] = piece

    def drop_piece_manually(self, piece):
        """ Action
        A specific function designed for the human player
        :param piece:
        :param row:
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
                if self.__board[r][c] == agent.get_piece() and self.__board[r + 1][c] == agent.get_piece() \
                        and self.__board[r + 2][c] == agent.get_piece() and self.__board[r + 3][c] == agent.get_piece():
                    self.__winner = agent
                    return True
                pass
            pass

        # check horizontal location
        for r in range(self.__dimension[0]):
            for c in range(self.__dimension[1] - 3):
                if self.__board[r][c] == agent.get_piece() and self.__board[r][c + 1] == agent.get_piece() \
                        and self.__board[r][c + 2] == agent.get_piece() and self.__board[r][c + 3] == agent.get_piece():
                    self.__winner = agent
                    return True
                pass
            pass

        # check negative diagonal
        for r in range(self.__dimension[0]):
            for c in range(self.__dimension[1] - 3):
                if self.__board[r][c] == agent.get_piece() and self.__board[r - 1][c + 1] == agent.get_piece() \
                        and self.__board[r - 2][c + 2] == agent.get_piece() and self.__board[r - 3][c + 3] == \
                        agent.get_piece():
                    self.__winner = agent
                    return True
                pass
            pass

        # check positive diagonal
        for r in range(self.__dimension[0] - 3):
            for c in range(self.__dimension[1] - 3):
                if self.__board[r][c] == agent.get_piece() and self.__board[r + 1][c + 1] == agent.get_piece() \
                        and self.__board[r + 2][c + 2] == agent.get_piece() and self.__board[r + 3][c + 3] == \
                        agent.get_piece():
                    self.__winner = agent
                    return True
                pass
            pass

    def __reward(self, agent, other_agent):
        """
        this is the reward per turn
        :param agent:
        :param other_agent:
        :return:
        """
        reward = 0
        if self.check_wining_move(agent):
            reward += 1
        elif self.check_wining_move(other_agent):
            reward -= 1
        else:
            reward += 1/42
        return reward

    def play_round(self, agent1, agent2):
        """
        * we should set who play first randomly
        * As the first player goes first we should check if he won and then assign the score
        * If the first player didn't won in his turn then we check for the second player and we assign the score
        * we set max_turn to 21 because the maximum number of vacant places is 42 and we play twice
        :param agent1: the first agent
        :param agent2: the second agent
        :return: the winner, the score for the first player and the score of the second player
        """

        first_player = np.random.choice([agent1, agent2])
        second_player = agent2 if first_player == agent1 else agent1
        reward_agent1 = 0
        reward_agent2 = 0
        max_turn = 21

        for turn in range(max_turn):
            if self.check_game_over():
                break

            row1, col1 = first_player.action(self.__board, self.__dimension)
            self.__drop_piece(row1, col1, first_player.get_piece())
            reward_agent1 += self.__reward(first_player, second_player)

            if self.check_wining_move(first_player):
                break

            row2, col2 = second_player.action(self.__board, self.__dimension)
            self.__drop_piece(row2, col2, second_player.get_piece())
            reward_agent2 += self.__reward(second_player, first_player)

            if self.check_wining_move(second_player):
                break

            # self.round_result(turn, first_player.get_agent_name(), row1, col1, reward_agent1)
            # self.round_result(turn, second_player.get_agent_name(), row2, col2, reward_agent2)

        return self.__winner, first_player, second_player, reward_agent1, reward_agent2

    def run(self, agent1, agent2, rounds=3):
        """
        The Run function for abject to see how the agent will do when they play many times
        :param agent1:
        :param agent2:
        :param rounds:
        :return:
        """
        cumulative_reward_agent1 = list()
        cumulative_reward_agent2 = list()

        win_percentage_agent1 = 0
        win_percentage_agent2 = 0

        for _ in range(rounds):
            self.__reset_configuration()
            winner, first_player, second_player, reward_agent1, reward_agent2 = self.play_round(agent1, agent2)

            if winner == first_player:
                win_percentage_agent1 += 1
            elif winner == second_player:
                win_percentage_agent2 += 1

            cumulative_reward_agent1.append(reward_agent1)
            cumulative_reward_agent2.append(reward_agent2)

            # information to track the rounds
            self.battle_result(first_player.get_agent_name(), (win_percentage_agent1/rounds)*100,
                               sum(cumulative_reward_agent1))
            self.battle_result(second_player.get_agent_name(), (win_percentage_agent2/rounds)*100,
                               sum(cumulative_reward_agent2))
            self.attribute(winner, first_player, second_player)
            self.board_state()
            print("_"*100)

        return cumulative_reward_agent1, cumulative_reward_agent2

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

    def get_observation(self):
        return self.__board

    def get_winner(self):
        return self.__winner

    def count_piece_in_board(self):
        return np.count_nonzero(self.__board)

    def display_board(self):
        print(*self.__board, sep='\n')

    def board_state(self):
        s = 'The winner is {} and {} piece dropped'.format(self.__winner.get_agent_name(), self.count_piece_in_board())
        print(s)

    @staticmethod
    def attribute(winner, agent1, agent2):
        if winner == agent1:
            s = '{} won against {}'.format(agent1.get_agent_name(), agent2.get_agent_name())
        elif winner == agent2:
            s = '{} won against {}'.format(agent2.get_agent_name(), agent1.get_agent_name())
        print(s)

    @staticmethod
    def round_result(turn, agent,row, col, score):
        s = 'The {} in {} turn drop the piece in row={}, col={} with score: {}'.format(agent, turn, row, col, score)
        print(s)

    @staticmethod
    def battle_result(agent, winning_rate, cumulative_reward):
        s = '{} won {}% of rounds with {} cumulative of reward'.format(agent, winning_rate, cumulative_reward)
        print(s)


class PieceMisplaced(Exception):
    """The piece misplaced please choose a column between 0 and 6"""
    pass

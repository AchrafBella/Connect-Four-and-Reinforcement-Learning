import numpy as np
import matplotlib.pyplot as plt


class Env:
    def __init__(self, agents=dict(), dimension=(6, 7)):
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
        :param agents: a dict that contains the players/agents
        """
        self.__dimension = dimension
        self.__board = np.zeros(self.__dimension)

        self.__game_over = False
        self.__winner = None

        self.__agent1 = agents.get('agent1', None)
        self.__agent2 = agents.get('agent2', None)

    def reset_configuration(self):
        """
        :return:
        """
        self.__board = np.zeros(self.__dimension)
        self.__game_over = False
        self.__winner = None

    def get_agents(self):
        return {'agent1': self.__agent1, 'agent2': self.__agent2}

    def drop_piece(self, row, column, piece):
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
        :return:
        """
        row = 5
        column = int(input('Your turn: please choose a column: '))
        if column >= 7 or column < 0:
            raise PieceMisplaced
        if self.__board[row][column] != 0:
            row -= 1
        self.__board[row][column] = piece

    def check_game_over(self):
        """
         This function check if all the value are full, if it's the case then game is over.
        :return:
        """
        if not np.any(self.__board == 0):
            self.__game_over = True

    def check_wining_move(self, agent):
        """
        we are going to check if there is 4 peaces vertically then, game is over
        we are going to check if there is 4 peaces  horizontally sloped diagonals then, game is over
        we are going to check if there is 4 peaces  positively&negatively sloped diagonals then, game is over
        :param agent: the agent
        :return: the winner
        """
        # check vertical locations
        for r in range(self.__dimension[0] - 3):
            for c in range(self.__dimension[1]):
                if self.__board[r][c] == agent.get_piece() and self.__board[r + 1][c] == agent.get_piece() \
                        and self.__board[r + 2][c] == agent.get_piece() and self.__board[r + 3][c] == agent.get_piece():
                    self.__game_over = True
                    self.__winner = agent.get_agent_name()
                    pass
                pass
            pass

        # check horizontal location
        for r in range(self.__dimension[0]):
            for c in range(self.__dimension[1] - 3):
                if self.__board[r][c] == agent.get_piece() and self.__board[r][c + 1] == agent.get_piece() \
                        and self.__board[r][c + 2] == agent.get_piece() and self.__board[r][c + 3] == agent.get_piece():
                    self.__game_over = True
                    self.__winner = agent.get_agent_name()
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
                    self.__winner = agent.get_agent_name()
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
                    self.__winner = agent.get_agent_name()
                    pass
                pass
            pass

        return self.__game_over

    def reward(self, agent, other_agent):
        reward = 0
        if self.check_wining_move(agent):
            reward += 1
        elif self.check_wining_move(other_agent):
            reward -= 1
        elif self.check_game_over():
            reward -= 10
        else:
            reward += 1/42
        return reward

    def play_round(self):
        """
        To avoid any argument with the agents we are going to flip a coin to decide who goes first
        :return:
        """
        first_player = np.random.choice([self.__agent1, self.__agent2])
        second_player = self.__agent2 if first_player == self.__agent1 else self.__agent1

        reward_agent_1 = 0
        reward_agent_2 = 0

        while True:
            if self.check_game_over():
                break
            elif self.check_wining_move(self.__agent1):
                break
            elif self.check_wining_move(self.__agent2):
                break

            row1, col1 = first_player.action(self.__board, self.__dimension)
            row2, col2 = second_player.action(self.__board, self.__dimension)

            self.drop_piece(row1, col1, first_player.get_piece())
            self.drop_piece(row2, col2, second_player.get_piece())

            reward_agent_1 += self.reward(self.__agent1, self.__agent2)
            reward_agent_2 += self.reward(self.__agent2, self.__agent1)

        return self.__winner, reward_agent_1, reward_agent_2

    def run(self, rounds=50):
        """
        :param rounds:
        :return:
        """
        win_percentage_agent1 = 0
        win_percentage_agent2 = 0

        cumulative_reward_agent_1 = list()
        cumulative_reward_agent_2 = list()

        for _ in range(rounds):
            self.reset_configuration()
            winner, reward_agent_1, reward_agent_2 = self.play_round()

            # the cumulative reward per agent
            cumulative_reward_agent_1.append(reward_agent_1)
            cumulative_reward_agent_2.append(reward_agent_2)

            # the percentage win per agent
            if winner == self.__agent1.get_agent_name():
                win_percentage_agent1 += 1
            elif winner == self.__agent2.get_agent_name():
                win_percentage_agent2 += 1

        print("The cumulative reward for the agent {} is {}".format(self.__agent1.get_agent_name(),
                                                                    sum(cumulative_reward_agent_1)))
        print("The cumulative reward for the agent {} is {}".format(self.__agent2.get_agent_name(),
                                                                    sum(cumulative_reward_agent_2)))

        print("Agent: {}  percentage of winning {}%".format(self.__agent1.get_agent_name(),
                                                            (win_percentage_agent1/rounds)))
        print("Agent: {}  percentage of winning {}%".format(self.__agent2.get_agent_name(),
                                                            (win_percentage_agent2/rounds)))
        return cumulative_reward_agent_1, cumulative_reward_agent_2

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

    def get_game_state(self):
        return self.__game_over

    def get_winner(self):
        return self.__winner

    def display_env(self):
        print(*self.__board, sep='\n')


class PieceMisplaced(Exception):
    """The piece misplaced please choose a column between 0 and 6"""
    pass

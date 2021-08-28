import numpy as np
from agent_greedy import GreedyAgent


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
        self.__agent1 = agents.get('agent1', None)
        self.__agent2 = agents.get('agent2', None)

        self.__dimension = dimension
        self.__board = np.zeros(self.__dimension)
        self.__winner = None

    def reset_configuration(self):
        """
        :return:
        """
        self.__board = np.zeros(self.__dimension)
        self.__winner = None

    def is_valid_action(self, row, column):
        """
        :param row:
        :param column:
        :return:
        """
        return self.__board[row][column] == 0

    def get_next_valid_location(self, column):
        """
        :param column:
        :return:
        """
        for row in reversed(range(self.__dimension[0])):
            if self.is_valid_action(row, column):
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
            raise ValueError("Please check the column you want to put your piece in")
        elif self.is_valid_action(row, column):
            self.__board[row][column] = piece
        else:
            row = self.get_next_valid_location(column)
            self.__board[row][column] = piece

    def check_game_over(self):
        """
         This function check if all the value are full, if it's the case then game is over.
        :return:
        """
        return not np.any(self.__board == 0)

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

    def get_reward(self, agent):
        other_agent = self.__agent2 if agent == self.__agent1 else self.__agent1
        reward = 0
        if self.check_game_over():
            reward -= 10
        elif self.__winner == agent:
            reward += 1
        elif self.__winner == other_agent:
            reward -= 1
        else:
            reward += 1/42
        return reward

    def play_round(self):
        """
        play round is an episode
        * we should set who play first randomly
        * As the first player goes first we should check if he won and then assign the score
        * If the first player didn't won in his turn then we check for the second player and we assign the score
        * we set max_turn to 21 because the maximum number of vacant places is 42
        :return:
        """
        first_player = np.random.choice([self.__agent1, self.__agent2])
        second_player = self.__agent2 if first_player == self.__agent1 else self.__agent1
        reward1, reward2 = 0, 0
        first_player_disk, second_player_disk = first_player.get_disk(), second_player.get_disk()

        for _ in range(21):

            row1, col1 = first_player.action(self)
            self.__drop_disk(row1, col1, first_player_disk)
            reward1 += self.get_reward(first_player)

            if self.check_wining_move(first_player):
                reward1 += self.get_reward(first_player)
                reward2 += self.get_reward(second_player)
                break

            row2, col2 = second_player.action(self)
            self.__drop_disk(row2, col2, second_player_disk)
            reward2 += self.get_reward(second_player)

            if self.check_wining_move(second_player):
                reward1 += self.get_reward(first_player)
                reward2 += self.get_reward(second_player)
                break

        if first_player == self.__agent2 and second_player == self.__agent1:
            first_player, second_player = self.__agent1, self.__agent2
            reward1, reward2 = reward2, reward1

        return first_player, second_player, reward1, reward2

    def run(self, episodes):
        winning_rate1, winning_rate2 = 0, 0

        for _ in range(episodes):
            self.reset_configuration()

            agent1, agent2, reward1, reward2 = self.play_round()

            winning_rate1 = self.winning_rate(agent1, winning_rate1)
            winning_rate2 = self.winning_rate(agent2, winning_rate2)

            if isinstance(agent1, GreedyAgent):
                agent1.compute_action_values(agent1.get_last_action(), reward1)
                agent1.initialize_action_values(agent1.get_action_values())

        self.battle_result(self.__agent1.get_agent_name(), self.__agent2.get_agent_name(), winning_rate1, winning_rate2,
                           episodes)

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
        s = 'The {} in his {} turn drop a piece in row={}, col={}'.format(agent_name.get_agent_name(), turn, row, col)
        print(s)

    @staticmethod
    def battle_result(agent1_name, agent2_name, winning_rate1, winning_rate2, rounds):
        s = '{}: Win percentage: {} % \n{}: Win percentage: {} %'.format(agent1_name,
                                                                         round((winning_rate1/rounds)*100, 2),
                                                                         agent2_name,
                                                                         round((winning_rate2/rounds)*100, 2))
        print(s)

    @staticmethod
    def statistic_score(cumulative_reward):
        s = 'the max {}, the min {}, the mean {}'.format(max(cumulative_reward), min(cumulative_reward),
                                                         np.mean(cumulative_reward))
        print(s)

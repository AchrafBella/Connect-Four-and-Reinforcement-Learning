import numpy as np
from operator import itemgetter
import itertools as it


class Agent:
    def __init__(self, agent_name, disk):
        self._agent_name = agent_name
        self._disk = disk

    def get_disk(self):
        return self._disk

    def get_agent_name(self):
        return self._agent_name


class Human(Agent):
    def __init__(self, agent_name, disk):
        """
        This is class is built in order to allow agent vs human
        :param agent_name:
        :param disk:
        """
        super(Human, self).__init__(agent_name, disk)

    @staticmethod
    def action(env):
        col = int(input('Your turn choose a column: '))
        while col not in [0, 1, 2, 3, 4, 5, 6]:
            col = int(input('Your turn choose a column: '))
        row = env.get_next_valid_location(col)
        return row, col


class RandomAgent(Agent):
    """"
    this agent represent a simple approach that consist of exploring the all the option.
    """
    def __init__(self, agent_name, disk):
        super().__init__(agent_name, disk)

    @staticmethod
    def action(env):
        """
        env
        :return:
        """
        columns = list()
        for col_ in range(env.get_dimension()[1]):
            if env.get_state()[0][col_] == 0:
                columns.append(col_)

        col = np.random.choice(columns)
        row = env.get_next_valid_location(col)

        while row is None:
            col = np.random.choice(columns)
            row = env.get_next_valid_location(col)

        return row, col


class AgentLeftMost(Agent):
    """"
    this agent use a strategy that consists of playing the piece on the left.
    """
    def __init__(self, agent_name, disk):
        super().__init__(agent_name, disk)

    @staticmethod
    def action(env):
        """
        :param env
        :return:
        """
        for col_ in range(env.get_dimension()[1]):
            for row_ in reversed(range(env.get_dimension()[0])):
                if env.get_state()[row_][col_] == 0:
                    return row_, col_
                pass
            pass
        pass


class HeuristicAgent(Agent):
    """
    This agent use an heuristic that makes him choose wisely the place of piece by looking all the possible places
    he chooses the place with the high score
    """
    def __init__(self, agent_name, disk):
        super().__init__(agent_name, disk)

    def patterns(self, observation, pairs, dimension):
        """ deterministic way
        this function will get the patterns for the move for each move will assign a specific weight
        to weight my moves i choose a scale from 1 to 10
        :param observation:
        :param pairs:
        :param dimension:
        :return:
        """
        weights = list()
        last_row, last_col = dimension[0] - 1, dimension[1] - 1
        first_col = 0
        for pair in pairs:
            if pair[0] == last_row and pair[1] == last_col:
                # check the left
                if observation[pair[0]][pair[1] - 1] == self.get_disk():
                    weight = 4
                    weights.append((pair, weight))
                else:
                    weight = 0
                    weights.append((pair, weight))

            if pair[0] == last_row and pair[1] == first_col:
                # check only the right
                if observation[pair[0]][pair[1] + 1] == self.get_disk():
                    weight = 4
                    weights.append((pair, weight))
                else:
                    weight = 0
                    weights.append((pair, weight))

            if pair[0] == last_row and pair[1] != last_col and pair[1] != first_col:
                # check right, left and both diagonal
                if observation[pair[0]][pair[1] + 1] == self.get_disk():
                    weight = 5
                    weights.append((pair, weight))
                if observation[pair[0]][pair[1] - 1] == self.get_disk():
                    weight = 5
                    weights.append((pair, weight))
                if observation[pair[0] - 1][pair[1] + 1] == self.get_disk():
                    weight = 6
                    weights.append((pair, weight))
                if observation[pair[0] - 1][pair[1] - 1] == self.get_disk():
                    weight = 6
                    weights.append((pair, weight))
                else:
                    weight = 0
                    weights.append((pair, weight))

            if pair[1] == last_col and pair[0] != last_row:
                # check the down, left or diagonal
                if observation[pair[0]][pair[1] - 1] == self.get_disk():
                    weight = 3
                    weights.append((pair, weight))
                if observation[pair[0] + 1][pair[1]] == self.get_disk():
                    weight = 3
                    weights.append((pair, weight))
                if observation[pair[0] + 1][pair[1]] != self.get_disk() and observation[pair[0] + 1][pair[1]] != 0:
                    weight = 6
                    weights.append((pair, weight))
                if observation[pair[0] + 1][pair[1] - 1] == self.get_disk():
                    weight = 3
                    weights.append((pair, weight))
                else:
                    weight = 0
                    weights.append((pair, weight))

            if pair[1] == first_col and pair[0] != last_row:
                # check the down, left or diagonal
                if observation[pair[0]][pair[1] + 1] == self.get_disk():
                    weight = 3
                    weights.append((pair, weight))
                if observation[pair[0] + 1][pair[1]] == self.get_disk():
                    weight = 3
                    weights.append((pair, weight))
                if observation[pair[0] + 1][pair[1]] != self.get_disk() and observation[pair[0] + 1][pair[1]] != 0:
                    weight = 6
                    weights.append((pair, weight))
                if observation[pair[0] + 1][pair[1] + 1] == self.get_disk():
                    weight = 3
                    weights.append((pair, weight))
                else:
                    weight = 0
                    weights.append((pair, weight))
            else:
                weight = 0
                weights.append((pair, weight))

        return weights

    def action(self, env):
        """
        :param env:
        :return:
        """
        if np.all(env.get_state() == 0):
            row, col = 5, np.random.randint(0, 6)
            return row, col
        vacant_places = np.argwhere(env.get_state() == 0)
        vacant_places = sorted(vacant_places, key=itemgetter(1))
        gs = it.groupby(vacant_places, key=itemgetter(1))
        try:
            valid_moves = [max(v, key=itemgetter(0)) for k, v in gs]
            move = max(self.patterns(env.get_state(), valid_moves, env.get_dimension()), key=itemgetter(1))
            row, col = move[0]
            return row, col
        except Exception as e:
            print("Unable to choose a move because of {}".format(e))


class GreedyAgent(Agent):
    def __init__(self, agent_name, disk, epsilon=0.5, k=7):
        """
        :param agent_name:
        :param disk:
        :param epsilon:
        :param k:
        """
        super().__init__(agent_name, disk)
        self.__epsilon = epsilon                   # Epsilon-greedy policy
        self.__k = k                               # number of actions
        self.__count_actions = np.zeros(self.__k)  # the count of the previous actions
        self.__Q = np.zeros(self.__k)              # action values

    def get_action_values(self):
        return self.__Q

    def initialize_action_values(self, action_values):
        self.__Q = action_values

    def compute_action_values(self, action, reward):
        self.__count_actions[action] += 1
        self.__Q[action] += (reward - self.__Q[action])/self.__count_actions[action]

    def epsilon_greedy_policy(self):
        if np.random.random() < self.__epsilon:
            return np.random.randint(self.__k)
        else:
            return np.random.choice(np.flatnonzero(self.__Q == self.__Q.max()))

    def action(self, env):
        col = self.epsilon_greedy_policy()
        row = env.get_next_valid_location(col)

        while row is None:
            col = self.epsilon_greedy_policy()
            row = env.get_next_valid_location(col)

        reward = env.get_reward(self, row, col)
        self.compute_action_values(col, reward)

        return row, col

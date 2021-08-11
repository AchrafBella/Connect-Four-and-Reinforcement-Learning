import numpy as np
from operator import itemgetter
import itertools as it


class Agent(object):
    def __init__(self, agent_name, disk):
        self.__agent_name = agent_name
        self.__disk = disk

    def get_disk(self):
        return self.__disk

    def get_agent_name(self):
        return self.__agent_name


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
        try:
            col = np.random.choice(columns)
            for row in reversed(range(env.get_dimension()[0])):
                if env.get_state()[row][col] == 0:
                    return row, col
        except Exception as e:
            print("Unable to choose a move because of {}".format(e))


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
        gs = it.groupby(vacant_places, key=itemgetter(1))
        try:
            valid_moves = [max(v, key=itemgetter(0)) for k, v in gs]
            move = max(self.patterns(env.get_state(), valid_moves, env.get_dimension()), key=itemgetter(1))
            row, col = move[0]
            return row, col
        except Exception as e:
            print("Unable to choose a move because of {}".format(e))


class GreedyAgent(Agent):
    def __init__(self, agent_name, disk, epsilon=0.1, k=6, learning_rate=1):
        super().__init__(agent_name, disk)
        """
        to decide which action is the base
        we define Action-Values
        Q(a) = E[r | A=a] = sum(r*P(r | A=a)) a£ self.action
        our goal is to maximize the Q* = max( Q(a))
        the value of an action is the expected reward when an action is taken
        the reward is non stationary which make this a non stationary bandit problem
        :param epsilon:
        :param k:
        :param learning_rate:
        :param agent_name:
        :param disk:

        """
        self.__epsilon = epsilon                   # Epsilon-greedy policy
        self.__k = k                               # number of actions
        self.__Q = np.zeros(self.__k)               # action values
        self.__action = list(range(self.__k))      # the actions
        self.__count_actions = np.zeros(self.__k)  # the count of the previous actions
        self.learning_rate = learning_rate
        self.__last_action = None

        self.__rewards = list()                    # the total rewards

    def reset(self):
        self.__Q = np.ones(self.__k)
        self.__action = list(range(self.__k))
        self.__count_actions = np.zeros(self.__k)
        self.__last_action = None

    def get_last_action(self):
        return self.__last_action

    def set_last_action(self, last_action):
        self.__last_action = last_action

    def get_count_actions(self):
        return self.__count_actions

    def get_action_values(self):
        return self.__Q

    def initialize_action_values(self, action_values):
        self.__Q = action_values

    def get_total_reward(self):
        return sum(self.__rewards)

    def compute_action_values(self, reward):
        """
        The incremental update rule action-value Q for each (action a, reward r):
        n += 1
        Q(a) <- Q(a) + 1/n * (r - Q(a))
        where:
        n = number of times action "a" was performed
        Q(a) = value estimate of action "a"
        r(a) = reward of sampling action bandit (bandit) "a"
        :param reward:
        :return:
        """
        self.__count_actions[self.__last_action] += 1
        q_d = reward - self.__Q[self.__last_action]
        q_m = self.learning_rate * self.__count_actions[self.__last_action]
        self.__Q[self.__last_action] += q_d / q_m

    def epsilon_greedy_policy(self):
        """
        the agent has the ability to choose either a greedy action or non-greedy action
        :return:
        """
        if np.random.random() < self.__epsilon:
            action = np.random.choice(self.__action)
        else:
            action = np.argmax(self.__Q)
        self.__last_action = action
        return action

    def action(self, state, dimension):
        if self.__last_action is None:
            col = np.random.choice(self.__action)
        else:
            col = self.epsilon_greedy_policy()
        row = 0
        while row is None:
            try:
                for _row in reversed(range(dimension[0])):
                    if state[_row][col] == 0:
                        row = _row
                        break
                        pass
                    if row is None:
                        col = self.epsilon_greedy_policy()
                        pass
                    pass
                pass
            except Exception as e:
                print("Couldn't choose a row or column because of {}".format(e))
        self.__last_action = col
        reward = 5
        self.compute_action_values(reward)
        return row, col

import random
import numpy as np
from operator import itemgetter
import itertools as it


class RandomAgent:
    """"
    this agent represent a simple approach that consist of exploring the all the option.
    """
    def __init__(self, agent_name, disk):
        self.__agent_name = agent_name
        self.__disk = disk
        pass

    def get_disk(self):
        return self.__disk

    def get_agent_name(self):
        return self.__agent_name

    @staticmethod
    def action(state, dimension):
        """
        :param state:
        :param dimension
        :return:
        """
        columns = list()
        for col_ in range(dimension[1]):
            if state[0][col_] == 0:
                columns.append(col_)
        try:
            col = random.choice(columns)
            for row in reversed(range(dimension[0])):
                if state[row][col] == 0:
                    return row, col
        except Exception as e:
            print("Unable to choose a move because of {}".format(e))


class AgentLeftMost:
    """"
    this agent use a strategy that consists of playing the piece on the left.
    """
    def __init__(self, agent_name, disk):
        self.__agent_name = agent_name
        self.__disk = disk
        pass

    def get_disk(self):
        return self.__disk

    def get_agent_name(self):
        return self.__agent_name

    @staticmethod
    def action(state, dimension):
        """
        :param state:
        :param dimension
        :return:
        """
        for col_ in range(dimension[1]):
            for row_ in reversed(range(dimension[0])):
                if state[row_][col_] == 0:
                    return row_, col_
                pass
            pass
        pass


class HeuristicAgent:
    """
    This agent use an heuristic that makes him choose wisely the place of piece by looking all the possible places
    he chooses the place with the high score
    """
    def __init__(self, agent_name, disk):
        self.__agent_name = agent_name
        self.__disk = disk
        pass

    def get_disk(self):
        return self.__disk

    def get_agent_name(self):
        return self.__agent_name

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
        last_row, last_col = dimension[0]-1, dimension[1]-1
        first_col = 0
        for pair in pairs:
            if pair[0] == last_row and pair[1] == last_col:
                # check the left
                if observation[pair[0]][pair[1]-1] == self.get_disk():
                    weight = 5
                    weights.append((pair, weight))
                else:
                    weight = 1
                    weights.append((pair, weight))

            elif pair[0] == last_row and pair[1] == first_col:
                # check only the right
                if observation[pair[0]][pair[1]+1] == self.get_disk():
                    weight = 5
                    weights.append((pair, weight))
                else:
                    weight = 1
                    weights.append((pair, weight))

            elif pair[0] == last_row:
                # check right, left and both diagonal
                if observation[pair[0]][pair[1]+1] == self.get_disk():
                    weight = 6
                    weights.append((pair, weight))
                elif observation[pair[0]][pair[1]-1] == self.get_disk():
                    weight = 6
                    weights.append((pair, weight))
                elif observation[pair[0]-1][pair[1]+1] == self.get_disk():
                    weight = 7
                    weights.append((pair, weight))
                elif observation[pair[0]-1][pair[1]-1] == self.get_disk():
                    weight = 7
                    weights.append((pair, weight))
                else:
                    weight = 7
                    weights.append((pair, weight))

            elif pair[1] == last_col:
                # check the down, left or diagonal
                if observation[pair[0]][pair[1]-1] == self.get_disk():
                    weight = 5
                    weights.append((pair, weight))
                elif observation[pair[0]+1][pair[1]] == self.get_disk():
                    weight = 8
                    weights.append((pair, weight))
                elif observation[pair[0]+1][pair[1]-1] == self.get_disk():
                    weight = 7
                    weights.append((pair, weight))
                else:
                    weight = 4
                    weights.append((pair, weight))

            elif pair[1] == first_col:
                # check only the right, diagonal, the down and the opponent piece
                if observation[pair[0]][pair[1]+1] == self.get_disk():
                    weight = 5
                    weights.append((pair, weight))
                elif observation[pair[0]+1][pair[1]] == self.get_disk():
                    weight = 8
                    weights.append((pair, weight))
                elif observation[pair[0]+1][pair[1]+1] == self.get_disk():
                    weight = 7
                    weights.append((pair, weight))
                else:
                    weight = 4
                    weights.append((pair, weight))

            else:
                # check only the right, diagonal, the down and the opponent piece
                if observation[pair[0]][pair[1] + 1] == self.get_disk():
                    weight = 5.5
                    weights.append((pair, weight))
                elif observation[pair[0]][pair[1]-1] == self.get_disk():
                    weight = 5.5
                    weights.append((pair, weight))
                elif observation[pair[0]+1][pair[1]] == self.get_disk():
                    weight = 8
                    weights.append((pair, weight))
                elif observation[pair[0]+1][pair[1]+1] == self.get_disk():
                    weight = 7.5
                    weights.append((pair, weight))
                elif observation[pair[0]+1][pair[1]-1] == self.get_disk():
                    weight = 7.5
                    weights.append((pair, weight))
                else:
                    weight = 5
                    weights.append((pair, weight))
        return weights

    def action(self, state, dimension):
        if np.all(state == 0):
            row, col = 5, random.randint(0, 6)
            return row, col
        vacant_places = np.argwhere(state == 0)
        gs = it.groupby(vacant_places, key=itemgetter(1))
        try:
            valid_moves = [max(v, key=itemgetter(0)) for k, v in gs]
            move = max(self.patterns(state, valid_moves, dimension), key=itemgetter(1))
            row, col = move[0]
            return row, col
        except Exception as e:
            print("Unable to choose a move because of {}".format(e))


class GreedyAgent:
    def __init__(self, agent_name, disk, epsilon=0.1, k=6):
        """
        to decide which action is the base
        we define Action-Values
        Q(a) = E[r | A=a] = sum(r*P(r | A=a)) a£ self.action
        our goal is to maximize the Q* = max( Q(a))
        the value of an action is the expected reward when an action is taken
        the reward is non stationary which make this a non stationary bandit problem
        :param epsilon:
        :param k:
        :param agent_name:
        :param disk:

        """
        self.__epsilon = epsilon                   # Epsilon-greedy policy
        self.__k = k                               # number of actions
        self.__Q = np.zeros(self.__k)              # action values
        self.__action = list(range(self.__k))      # the actions
        self.__count_actions = np.zeros(self.__k)  # the count of the previous actions
        self.__rewards = list()                    # the total rewards

        self.__agent_name = agent_name
        self.__disk = disk

    def get_agent_name(self):
        return self.__agent_name

    def get_disk(self):
        return self.__disk

    def get_count_actions(self):
        return self.__count_actions

    def get_action_values(self):
        return self.__Q

    def initialize_action_values(self, action_values):
        self.__Q = action_values

    def get_total_reward(self):
        return sum(self.__rewards)

    def compute_action_values(self, action, reward):
        """
        The incremental update rule action-value Q for each (action a, reward r):
        n += 1
        Q(a) <- Q(a) + 1/n * (r - Q(a))
        where:
        n = number of times action "a" was performed
        Q(a) = value estimate of action "a"
        r(a) = reward of sampling action bandit (bandit) "a"
        :param action:
        :param reward:
        :return:
        """
        self.__count_actions[action] += 1
        self.__Q[action] += (reward - self.__Q[action]) / 2*(self.__count_actions[action])

    def choose_action(self):
        """
        the agent has the ability to choose either a greedy action or non-greedy action
        :return:
        """
        # explore
        if np.random.random() < self.__epsilon:
            action = np.random.choice(self.__action)
        # exploit
        else:
            action = np.argmax(self.__Q)
        return action

    def reward_system(self, state, dimension, row, col):
        last_row, last_col = dimension[0] - 1, dimension[1] - 1
        first_col = 0

        # checking for the left
        if row == last_row and col == first_col:
            if state[row][col+1] == self.get_disk():
                return 2
            elif state[row][col+1] == self.get_disk() and state[row][col+2] == self.get_disk():
                return 3
            elif state[row][col+1] == self.get_disk() and state[row][col+2] == self.get_disk() and \
                    state[row][col+3] == self.get_disk():
                return 5
            elif state[row][col+1] == self.get_disk() and state[row][col+2] == self.get_disk() and \
                    state[row][col+3] == self.get_disk() and state[row][col+4] == self.get_disk():
                return 10
            else:
                return 1/42

        # checking for the right
        elif row == last_row and col == last_col:
            if state[row][col - 1] == self.get_disk():
                return 2
            elif state[row][col - 1] == self.get_disk() and state[row][col - 2] == self.get_disk():
                return 3
            elif state[row][col - 1] == self.get_disk() and state[row][col - 2] == self.get_disk() and \
                    state[row][col + 3] == self.get_disk():
                return 5
            elif state[row][col - 1] == self.get_disk() and state[row][col - 2] == self.get_disk() and \
                    state[row][col - 3] == self.get_disk() and state[row][col - 4] == self.get_disk():
                return 10
            else:
                return 1/42
        # checking by the column
        elif row == last_row:
            if state[row-1][col] == self.get_disk():
                return 2
            elif state[row - 1][col] == self.get_disk() and state[row - 2][col] == self.get_disk():
                return 3
            elif state[row - 1][col] == self.get_disk() and state[row - 2][col] == self.get_disk() and \
                    state[row - 3][col] == self.get_disk():
                return 5
            elif state[row - 1][col] == self.get_disk() and state[row - 2][col] == self.get_disk() and \
                    state[row - 3][col] == self.get_disk() and state[row - 4][col] == self.get_disk():
                return 10
            else:
                return 1/42
        else:
            return 1/42

    def action(self, state, dimension):
        row = None
        col = self.choose_action()

        while row is None:
            try:
                for _row in reversed(range(dimension[0])):
                    if state[_row][col] == 0:
                        row = _row
                        break
                        pass
                    pass
                if row is None:
                    col = self.choose_action()
            except Exception as e:
                print("Couldn't choose a row or column because of {}".format(e))
        reward = self.reward_system(state, dimension, row, col)
        self.__rewards.append(reward)
        self.compute_action_values(col, reward)
        return row, col

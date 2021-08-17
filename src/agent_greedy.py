from agents import Agent
import numpy as np


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

        self.__last_action = None

    def get_last_action(self):
        return self.__last_action

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
            t = np.random.choice(np.flatnonzero(self.__Q == self.__Q.max()))
            return t

    def action(self, env):
        col = self.epsilon_greedy_policy()
        row = env.get_next_valid_location(col)
        while row is None:
            col = self.epsilon_greedy_policy()
            row = env.get_next_valid_location(col)
        self.__last_action = col
        return row, col

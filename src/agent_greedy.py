from agents import Agent
import numpy as np


class GreedyAgent(Agent):
    def __init__(self, disk, agent_name="Greedy agent", step_size=None, epsilon=1, k=7):
        """
        I applied the k-armed bandit problem in the context of the game connect4
        i solved this problem using epsilon-greedy where we exploit with a rate of epsilon
        the environment is very deterministic:
        +1 when you win
        -1 when you lost
        -10 when the game is over
        and 1/42 to help the agent to converge
        :param agent_name:
        :param disk:
        :param epsilon:
        :param k:
        """
        super().__init__(agent_name, disk)
        self.step_size = step_size                 # step size
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
        if self.step_size is None:
            self.step_size = (1 / self.__count_actions[action])
        self.__Q[action] += self.step_size * (reward - self.__Q[action])

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
        self.__last_action = col
        return row, col

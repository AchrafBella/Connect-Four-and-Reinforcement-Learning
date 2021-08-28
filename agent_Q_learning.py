import numpy as np
from agents import Agent


class QAgent(Agent):
    def __init__(self, disk, agent_name="Q learning agent", learning_rate=1, epsilon=1):
        """
        The model will initialize a Q table where the columns are the actions and the rows are the states.

        :param agent_name:
        :param disk:
        """
        super().__init__(agent_name, disk)
        self.actions = 7                                  # number of actions
        self.states = 7                                   # number of states
        self.lr = learning_rate                           # step size/learning rate
        self.__epsilon = epsilon                          # Epsilon-greedy policy
        self.__Q = np.zeros((self.states, self.actions))  # Q table

    def get_q_table(self):
        return self.__Q

    def initialize_q_table(self, q_table):
        self.__Q = q_table

    def compute_q_function(self, new_state, state, reward, action):
        self.__Q[state, action] += self.lr * (reward + np.max(self.__Q[new_state]) - self.__Q[state, action])

    def epsilon_greedy_policy(self):
        if np.random.random() < self.__epsilon:
            return np.random.randint(self.actions)
        else:
            return np.random.choice(np.flatnonzero(self.__Q == self.__Q.max()))

    def action(self):
        pass

import numpy as np
from agents import Agent


class QAgent(Agent):
    def __init__(self, disk, agent_name="Q learning agent"):
        """

        :param agent_name:
        :param disk:
        """
        super().__init__(agent_name, disk)
        self.num_of_states = 7
        self.num_of_actions = 7
        self.Q_table = np.zeros(())




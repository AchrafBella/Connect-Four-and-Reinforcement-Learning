from agents import Agent
import numpy as np


class RandomAgent(Agent):
    """"
    this agent represent a simple approach that consist of exploring the all the option.
    """
    def __init__(self, disk, agent_name="Random agent"):
        super().__init__(agent_name, disk)

    @staticmethod
    def action(env):
        """
        env
        :return:
        """
        columns = []
        for col_ in range(env.get_dimension()[1]):
            if env.get_state()[0][col_] == 0:
                columns.append(col_)

        col = np.random.choice(columns)
        row = env.get_next_valid_location(col)

        while row is None:
            col = np.random.choice(columns)
            row = env.get_next_valid_location(col)

        return row, col

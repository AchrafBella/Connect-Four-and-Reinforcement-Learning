import random


class Agent:
    """"
    this agent represent a simple a approach that consist of using the hazard
    i call this the random agent
    """
    def __init__(self, agent_name, piece):
        self.agent_name = agent_name
        self.piece = piece

    def get_piece(self):
        return self.piece

    def get_agent_name(self):
        return self.agent_name

    def action(self, observation, dimension):
        """
        :param observation:
        :param dimension
        :return:
        """
        columns = list()
        for col_ in range(dimension[1]):
            if observation[0][col_] == 0:
                columns.append(col_)
        col = random.choice(columns)
        for row in reversed(range(dimension[0])):
            if observation[row][col] == 0:
                print("row:", row, "col:", col, self.piece)
                return row, col

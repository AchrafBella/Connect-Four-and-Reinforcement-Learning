from agents import Agent


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
        actions = [0, 1, 2, 3, 4, 5, 6]
        while col not in actions:
            col = int(input('Your turn choose a column: '))
        row = env.get_next_valid_location(col)
        return row, col

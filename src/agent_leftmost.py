from agents import Agent


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

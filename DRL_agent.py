from environment import Env


class EnvGym(Env):
    def __init__(self, configuration, dimension=(6, 7)):
        super().__init__(dimension=dimension)

        self.agent1 = configuration.get('agent1', None)
        self.agent2 = configuration.get('agent2', None)
        self.board = self.get_observation()
        self.reward_range = (-10, 1)

    def battle(self, agent1, agent2):
        """
        :param agent1:
        :param agent2:
        :return:
        """
        epochs = 42
        for i in range(epochs):
            if self.check_game_over():
                break
            if self.check_wining_move(agent1):
                break
            if self.check_wining_move(agent2):
                break

            row1, col1 = agent1.action(self.__board, self.__dimension)
            row2, col2 = agent2.action(self.__board, self.__dimension)
            X
            self.drop_piece(row1, col1, agent1.get_piece())
            self.drop_piece(row2, col2, agent2.get_piece())
        return self.__winner

    def reset(self):
        self.reset_configuration()

    def reward(self, agent1, agent2):
        """
        for each action done by the agent he receive a reward based on the result
        :param agent1:
        :param agent2:
        :return:
        """
        reward = 0
        if agent1.get_agent_name() == self.get_winner():
            reward += 1
        elif agent2.get_agent_name() == self.get_winner():
            reward -= 1
        elif self.check_game_over():
            reward -= 10
        else:
            reward += 1/42
        return reward

    def step(self, action=None, reward=None):
        """
        this step take an action
        :param action:
        :param reward:
        :return: next step and reward
        """
        reward_agent1 = 0
        reward_agent2 = 0
        self.battle(agent1=self.agent1, agent2=self.agent2)
        reward_agent1 += self.reward(self.agent1, self.agent2)
        reward_agent2 += self.reward(self.agent1, self.agent2)
        print(reward_agent1, reward_agent2)

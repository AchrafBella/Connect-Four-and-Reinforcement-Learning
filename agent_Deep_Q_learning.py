from agents import Agent
from keras.models import Sequential
from keras.layers import Dense, Flatten


def deep_neural_network_model():
    model = Sequential()
    model.add(Flatten())
    model.add(Dense(50, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(7))
    return model


class DeepQAgent(Agent):
    def __init__(self, disk, learning_rate, gamma, epsilon, agent_name="Deep Q learning agent"):
        """
        :param agent_name:
        :param disk:
        """
        super().__init__(agent_name, disk)
        self.learning_rate = learning_rate
        self.gamma = gamma
        self.epsilon = epsilon
        self.model = deep_neural_network_model()

    def action(self):
        pass

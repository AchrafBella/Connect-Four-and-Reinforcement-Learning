from environment import Env
from agents import RandomAgent, AgentLeftMost, HeuristicAgent, GreedyAgent, Human
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    randomAgent = RandomAgent("RandomAgent", 1)
    greedyAgent = Human("Achraf", 2)

    env1 = Env(agents={'agent1': randomAgent, 'agent2': greedyAgent})
    env1.play_round()
    print(env1.get_winner())
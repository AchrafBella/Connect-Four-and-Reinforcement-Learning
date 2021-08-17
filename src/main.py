from environment import Env
from agent_greedy import GreedyAgent
from agent_random import RandomAgent

if __name__ == "__main__":
    randomAgent = RandomAgent("RandomAgent", 1)
    greedyAgent = GreedyAgent("greedyAgent", 2)

    env1 = Env(agents={'agent1': randomAgent, 'agent2': greedyAgent})
    env1.play_round()
    print(env1.get_winner())
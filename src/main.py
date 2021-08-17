from environment import Env
from agent_greedy import GreedyAgent
from agent_random import RandomAgent
from agent_hur import HeuristicAgent
from agent_leftmost import AgentLeftMost
import matplotlib.pyplot as plt

if __name__ == "__main__":
    GreedyAgent1 = GreedyAgent("GreedyAgent 1", 1)
    RandomAgent2 = AgentLeftMost("HeuristicAgent 2", 2)

    env1 = Env(agents={'agent1': GreedyAgent1, 'agent2': RandomAgent2})
    total_reward, total_action_count = env1.__run__(rounds=5000)


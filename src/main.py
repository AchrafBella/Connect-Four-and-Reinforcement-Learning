from environment import Env
from agents import RandomAgent, AgentLeftMost, HeuristicAgent, GreedyAgent
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

if __name__ == "__main__":

    randomAgent = RandomAgent("RandomAgent", 1)
    leftAgent = AgentLeftMost("AgentLeftMost", 2)
    hurAgent = HeuristicAgent("HeuristicAgent", 3)
    greedyAgent = GreedyAgent("GreedyAgent", 4)

    env1 = Env(agents={'agent1': randomAgent, 'agent2': leftAgent})
    env1.run(rounds=500)

    env2 = Env(agents={'agent1': hurAgent, 'agent2': leftAgent})
    env2.run(rounds=500)

    env3 = Env(agents={'agent1': hurAgent, 'agent2': randomAgent})
    env3.run(rounds=500)

    """
    episodes = 1

    agent1 = GreedyAgent('GreedyAgent1', 1)
    agent2 = HeuristicAgent('HeuristicAgent', 2)
    env1 = Env(agents={'agent1': agent1, 'agent2': agent2})
    num_battle_agent1_, num_battle_agent2_ = 0, 0

    for episode in range(episodes):
        env1.reset_configuration()
        first_player, second_player = env1.play_round()
        Q = agent1.get_action_values()
        last_action = agent1.get_last_action()
        print(Q)
        print(last_action)
        agent1.initialize_action_values(Q)
        agent1.set_last_action(last_action)

        if env1.get_winner() == first_player:
            num_battle_agent1_ += 1
        elif env1.get_winner() == second_player:
            num_battle_agent2_ += 1

    print("the {} won {} round".format(agent1.get_agent_name(), num_battle_agent1_))
    print("the {} won {} round".format(agent2.get_agent_name(), num_battle_agent2_))

    plt.figure(figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
    plt.title("Average Reward of Greedy Agent vs. Epsilon-Greedy Agent")
    plt.xlabel("Steps")
    plt.ylabel("Average reward")
    plt.show()

    """

from environment import Env
from agents import RandomAgent, AgentLeftMost, HeuristicAgent, GreedyAgent
import matplotlib.pyplot as plt
import numpy as np


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
    agent1 = GreedyAgent('GreedyAgent1', 1, 0.5, learning_rate=1)
    agent2 = HeuristicAgent('HeuristicAgent', 2)
    env1 = Env(agents={'agent1': agent1, 'agent2': agent2})
    reward = list()
    num_battle_agent1, num_battle_agent2 = 0, 0
    episodes = 52
    for episode in range(episodes):
        try:
            env1.reset_configuration()
            first_player, second_player, _, _ = env1.play_round()
            q = agent1.get_action_values()
            agent1.initialize_action_values(q)
            reward.append(agent1.get_total_reward())
        except Exception as e:
            print(e)

        if env1.get_winner() == first_player:
            num_battle_agent1 += 1
        elif env1.get_winner() == second_player:
            num_battle_agent2 += 2

    print("the {} won {} round".format(agent1.get_agent_name(), num_battle_agent1))
    print("the {} won {} round".format(agent2.get_agent_name(), num_battle_agent2))
    
    episodes = 50
    All_reward = list()
    # alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001, 0.0001]
    alphas = [1]
    for alpha in alphas:
        print(alpha)
        agent1_ = GreedyAgent('GreedyAgent1', 1, 0.5, learning_rate=alpha)
        agent2 = RandomAgent('RandomAgent', 2)
        env1_ = Env(agents={'agent1': agent1_, 'agent2': agent2})
        reward_ = list()
        num_battle_agent1_, num_battle_agent2_ = 0, 0
        for episode in range(episodes):
            try:
                env1_.reset_configuration()
                first_player, second_player, _, _ = env1_.play_round()
                q_ = agent1_.get_action_values()
                agent1_.initialize_action_values(q_)
                reward_.append(agent1_.get_total_reward())
            except Exception as e:
                print(e)
            print("the winner is ",env1_.get_winner().get_agent_name())

            if env1_.get_winner() == first_player:
                num_battle_agent1_ += 1
            elif env1_.get_winner() == second_player:
                num_battle_agent2_ += 2
        All_reward.append(reward_)
        print("the {} won {} round".format(agent1_.get_agent_name(), num_battle_agent1_))
        print("the {} won {} round".format(agent2.get_agent_name(), num_battle_agent2_))

    plt.figure(figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
    s = ''
    for elm, alpha in zip(All_reward, alphas):
        plt.plot(elm)
        s += "{} ".format(str(alpha))
    plt.title("Average Reward of Greedy Agent vs. Epsilon-Greedy Agent")
    plt.legend(s.split(' '))
    plt.xlabel("Steps")
    plt.ylabel("Average reward")
    plt.show()
    """




from environment import Env
from agents import RandomAgent, AgentLeftMost, HeuristicAgent, GreedyAgent

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

    total_reward = list()
    for episode in range(20):
        env = Env(agents={'agent1': greedyAgent, 'agent2': randomAgent})
        env.run(rounds=1)
        q_values = greedyAgent.get_action_values()
        greedyAgent.initialize_action_values(q_values)
        total_reward.append(greedyAgent.get_total_reward())

    print(total_reward)






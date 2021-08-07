from environment import Env

from agents import Agent, HeuristicAgent, AgentLeftMost

if __name__ == "__main__":
    agent1 = HeuristicAgent('hur agent 1', 1)
    agent1_ = AgentLeftMost('hur agent 2', 2)

    env = Env(agents={'agent1': agent1, 'agent2': agent1_})
    cumulative_reward_agent_1, cumulative_reward_agent_2 = env.run(rounds=500)
    env.reward_visualization(cumulative_reward_agent_1, cumulative_reward_agent_2)
    env.statistic_score(cumulative_reward_agent_1)
    env.statistic_score(cumulative_reward_agent_2)

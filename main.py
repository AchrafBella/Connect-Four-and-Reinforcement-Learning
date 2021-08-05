from environment import Env

from agents import Agent, HeuristicAgent, AgentLeftMost

if __name__ == "__main__":
    agent1 = Agent('agent 1', 1)
    agent1_ = Agent('agent 2', 2)

    env = Env({'agent1': agent1, 'agent2': agent1_})
    cumulative_reward_agent_1, cumulative_reward_agent_2 = env.run()
    # env.reward_visualization(cumulative_reward_agent_1, cumulative_reward_agent_2)
    env.display_board()
    print("_"*50)

    agent2 = HeuristicAgent('hur agent 1', 1)
    agent2_ = HeuristicAgent('hur agent 2', 2)

    env1 = Env({'agent1': agent2, 'agent2': agent2_})
    cumulative_reward_agent_1, cumulative_reward_agent_2 = env1.run()
    # env1.reward_visualization(cumulative_reward_agent_1, cumulative_reward_agent_2)
    print("_"*50)

    agent3 = AgentLeftMost('left agent 1', 1)
    agent3_ = AgentLeftMost('left agent 2', 2)

    env3 = Env({'agent1': agent3, 'agent2': agent3_})
    cumulative_reward_agent_1, cumulative_reward_agent_2 = env3.run()
    # env3.reward_visualization(cumulative_reward_agent_1, cumulative_reward_agent_2)
    print("_"*50)

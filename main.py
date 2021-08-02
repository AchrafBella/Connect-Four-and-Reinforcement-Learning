from environment import Env
from agent import Agent, HeuristicAgent, AgentLeftMost

if __name__ == "__main__":

    agent1 = Agent('agent 1', 1)
    agent1_ = Agent('agent 2', 2)
    Env1 = Env()
    Env1.run(agent1, agent1_)
    print("_"*50)
    agent2 = HeuristicAgent('hur agent 1', 1)
    agent2_ = HeuristicAgent('hur agent 2', 2)
    Env2 = Env()
    Env2.run(agent2, agent2_)
    print("_"*50)
    agent3 = AgentLeftMost('left agent 1', 1)
    agent3_ = AgentLeftMost('left agent 2', 2)
    Env3 = Env()
    Env3.run(agent3, agent3_)


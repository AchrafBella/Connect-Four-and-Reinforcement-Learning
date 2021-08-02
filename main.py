from environment import Env
from agent import Agent, HeuristicAgent, AgentLeftMost

if __name__ == "__main__":

    Env = Env()

    agent1 = Agent('agent1', 1)
    agent2 = HeuristicAgent('hur agent', 2)
    agent3 = AgentLeftMost('left agent', 3)

    winner = Env.battle(agent1, agent3)

    print(winner)
    Env.display_env()

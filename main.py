from environment import Env
from agent import Agent, HeuristicAgent

if __name__ == "__main__":

    Env = Env()

    agent1 = Agent('agent1', 1)
    agent2 = HeuristicAgent('hur agent2', 2)

    winner = Env.battle(agent1, agent2)

    print(winner)
    Env.display_env()

from environment import Env
from agent import Agent, HeuristicAgent

if __name__ == "__main__":

    Env = Env()
    agent1 = Agent('agent1', 1)
    agent2 = HeuristicAgent('hur agent', 2)

    # the maximum number of places
    epochs = 42
    for i in range(epochs):
        if Env.check_game_over():
            break
        if Env.check_wining_move(agent1):
            break
        if Env.check_wining_move(agent2):
            break
        row1, col1 = agent1.action(Env.get_observation(), Env.get_dimension())
        row2, col2 = agent2.action(Env.get_observation(), Env.get_dimension())

        Env.drop_piece(row1, col1, agent1.get_piece())
        Env.drop_piece(row2, col2, agent2.get_piece())
        pass
    pass
    print(Env.get_message())
    Env.display_env()

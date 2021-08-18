import numpy as np

from environment import Env
from agent_greedy import GreedyAgent
from agent_random import RandomAgent
from agent_hur import HeuristicAgent
from agent_leftmost import AgentLeftMost
import pandas as pd


if __name__ == "__main__":
    HeuristicAgent2 = HeuristicAgent("HeuristicAgent", 2)
    AgentLeftMost3 = AgentLeftMost("AgentLeftMost", 3)
    RandomAgent4 = RandomAgent("RandomAgent", 4)

    agents = [HeuristicAgent2, AgentLeftMost3, RandomAgent4]
    step_sizes = [0.001, 0.01, 0.1, 1]
    epsilons = [0.001, 0.01, 0.1, 1.0]

    cols = pd.MultiIndex.from_tuples([('HeuristicAgent', '0.001'), ('HeuristicAgent', '0.01'), ('HeuristicAgent', '0.1'),
                                      ('HeuristicAgent', '1'), ('AgentLeftMost', '0.001'), ('AgentLeftMost', '0.01'),
                                      ('AgentLeftMost', '0.1'),  ('AgentLeftMost', '1'),
                                      ('RandomAgent', '0.001'),
                                      ('RandomAgent', '0.01'), ('RandomAgent', '0.1'), ('RandomAgent', '1')])

    data = pd.DataFrame(np.zeros((4, 12)), index=epsilons, columns=cols)

    def data_manip(data, agent, epsilon, step_size, win):
        df_ = data[agent.get_agent_name()]
        df_.at[epsilon, str(step_size)] = win
        data[agent.get_agent_name()] = df_

    graphs = dict()

    for agent in agents:
        for epsilon in epsilons:
            for step_size in step_sizes:
                GreedyAgent1 = GreedyAgent("GreedyAgent", 1, epsilon=epsilon, step_size=step_size)
                env1 = Env(agents={'agent1': GreedyAgent1, 'agent2': agent})
                winning_rounds_agent1, _, utility, actions = env1.__run__(rounds=1500)
                data_manip(data, agent, epsilon, step_size, winning_rounds_agent1)

    data.set_axis(['epsilon: 0.01', 'epsilon: 0.1', 'epsilon: 1'], axis='index', inplace=True)
    data.to_html("greed agent tuning.html")
    print(data)

from environment import Env
from agent_random import RandomAgent
from agent_hur import HeuristicAgent
from agent_leftmost import AgentLeftMost


agent1 = HeuristicAgent('hur agent 1', 1)
agent1_ = AgentLeftMost('AgentLeftMost', 2)
env1 = Env(agents={'agent1': agent1, 'agent2': agent1_})
env1.run(rounds=500)

agent2 = HeuristicAgent('hur agent 1', 1)
agent2_ = RandomAgent('random agent 2', 2)
env2 = Env(agents={'agent1': agent2, 'agent2': agent2_})
env2.run(rounds=500)

agent3 = RandomAgent('random agent 1', 1)
agent3_ = AgentLeftMost('leftmost agent 2', 2)
env3 = Env(agents={'agent1': agent3, 'agent2': agent3_})
env3.run(rounds=500)



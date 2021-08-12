# Game-AI-and-Reinforcement-Learning
-------------------------------------

Motivation
-----------
Recently, I started reading more & more about Reinforcement Learning and then, I found a kaggle course that explain a bit ML, DL & RL. the course come with his specific framework all the concepts like Environment and agent were implemented in such a way to simplify the learning process. It's very interesting if you are a beginner.
I didn't like that because it was like a black box for me, so I decided to implement my own framework for connect4.
Later I found myself reading articles, seeing implementation not only for connect4 but for RL concepts, Markov decision process, k-armed bandit ...etc
I struggled to understand how people implemented these concepts because not all of them stick with the mathematical notation, and they were not all documented
So I decided to create this API to simplify the use of these concept and even help the student to understand the concepts.


Concepts
-----------
This project contains 2 main classes, Environment and Agents.
The Environment represents the well-known game Connect4 (aka  Four in a Row)

Running the Environment you could shape the game, run battles between an agent or you and an agent, visualize the rewards, get statistics about the winner, the percentage of win and the number of dropped disks.
![image](https://user-images.githubusercontent.com/52492864/128045136-8107d272-0b02-454a-bb0f-932d1079ec9f.png)

The class Agents contain: 
- Random Agent: as the name implies, randomly choose a move based on uniform distribution 
- Heuristic Agent: using a specific heuristic I create, he chooses the move with high score. In Version2 the agent is able to block opponent attack
- Left Agent: this agent use a strategy that consists of playing the piece on the left
- Greedy Agent: this agent use the concept of Multi-Armed Bandit, he learns by playing and getting a reward
- DRL Agent: using RL

For all these agents i build a reward system
The reward system is as the following:
- Each time the agent win a game, he will receive a reward of +1.
- Each time the agent lost a game, he will punch by -1.
- And -10 in case of draw / game over
- he will get +1/42 for simple move

Concerning the environment of the game connect4 I modeling it using an array (Python object) that represent the field. Also, I updated the design environment for all the agents.

Coding
-----------
During the coding I took into consideration all the case that could block the game either if the board is full or when we left with no vacant place and I used exception handling for that to pursuit the battle and I delete the score for this failed battle.
The code is also optimized using all the possible means in python.

Requirements
-----------
```python
pip3 install -r requirements.txt (Python 3)
```

Exemple to run: 
-----------
```python
gent1 = HeuristicAgent('hur agent 1', 1)
agent1_ = AgentLeftMost('hur agent 2', 2)

env = Env(agents={'agent1': agent1, 'agent2': agent1_})
    
cumulative_reward_agent_1, cumulative_reward_agent_2 = env.run(rounds=500)

env.reward_visualization(cumulative_reward_agent_1, cumulative_reward_agent_2)
env.statistic_score(cumulative_reward_agent_1)
env.statistic_score(cumulative_reward_agent_2)
```

Results
-----------
This figure represents the result of the battle between the agents, the percentage of winning is the result of 500 play.

![image](https://user-images.githubusercontent.com/52492864/128951936-59f8204c-71a9-4c0a-8399-3deaeb97c0c9.png)

The figure below represent the total reward after battle between the Greedy agent and the Heuristic agent. For the Greedy agent, with used the Exploratory approach with epsilon: 0 and both Exploratory and greedy action with epsilon 0.9

![image](https://user-images.githubusercontent.com/52492864/128686295-b594159b-9848-488e-a9a3-614486c02546.png)

And here I fixed epsilon and I let the agent play with different learning rate. You should know that the environment is static, so I set a seed to get the best learning rate for this battle and against this specific agent.

![image](https://user-images.githubusercontent.com/52492864/128849348-0b86a84c-771c-4661-94b9-9f27ed8cbeef.png)

License
-----------
You are free to use or extend this project for
educational purposes provided that (1) you do not distribute or publish solutions (2) you retain this notice and (3) you provide clear attribution to Achraf BELLA, including a link to this repository.

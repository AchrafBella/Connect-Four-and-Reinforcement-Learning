# Game-AI-and-Reinforcement-Learning
-------------------------------------

Motivation
-----------
Recently, i started reading more & more about Reinforcement Learning and then, i found a kaggle course that explain a little bit ML, DL & RL. the course come with his specific frameword all the concepts like Environment and agent were implemented in such a way to simplify the learning process. It's very interesting if you are beginner.
I didn't like that because it was like a black box for me so i decided to implement my own framework for connect4.
Later i found myself reading articles, seeing implementation not only for connect4 but for RL concepts, markov decision process, k-armed bandit ...ect
I struggled to understand how people implementated these concepts because not all of them stick with the matematical notation and they were not all documented
So i decided to create this API the simplify the use of these concept and even help the student to understand the concepts.

Concepts
-----------
This project contains 2 main classes Environment and Agents.
the Environment represent the well-known game Connect4 (aka  Four in a Row)

Running the Environment you could shape the game, run battles btween agent or you and an agent, visualize the rewards, get statics about the winner, the percentage of win and the number of dropped disks.
![image](https://user-images.githubusercontent.com/52492864/128045136-8107d272-0b02-454a-bb0f-932d1079ec9f.png)

the class Agents contains: 
- Random Agent: as the name implies randomly choose a move based on uniform distrubition 
- Heuristic Agent: using a specific heuristic i create he choose the move with high score
- Left Agent: this agent use a strategy that consists of playing the piece on the left
- Greedy Agent: this agent use the concept of e Multi-Armed Bandit he learn by playing and getting a reward
- DRL Agent: using RL

For all these agent i build a reward system
The reward system is as the following:
- Each time the agent win a game he will recieve a reward of +1.
- Each time the agent lost a game he will punch by -1.
- And -10 in case of draw / game over
- he will get +1/42 for simple move

Concerning the environment of the game connect4 i modeling it using an array (Python object) that represent the field. Also i updated the design environement for all the agents.

Coding
-----------
During the coding i took into consideration all the case that could block the game either if the board is full or when we left with no vacant place and i used exception handling for that to pursuit the battle and i delete the score for this failed battle.
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
This figure represent the result of the battle between the agents, the percentage of winning is the result of 500 play.

![image](https://user-images.githubusercontent.com/52492864/128653317-b5b3dc8e-463f-4fce-b536-d73964c4faf0.png)


Licensing
-----------
You are free to use or extend this project for
educational purposes provided that (1) you do not distribute or publish solutions (2) you retain this notice and (3) you provide clear attribution to Achraf BELLA, including a link to this repository.

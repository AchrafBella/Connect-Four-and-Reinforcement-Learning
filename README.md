# Game-AI-and-Reinforcement-Learning
-------------------------------------

Motivation
-----------
Recently, I started reading more & more about Reinforcement Learning and then, I found MOOC in kaggle that explain data science. The course come with his specific framework for example for RL all the concepts like Environment and Agent were implemented in such a way to simplify the learning process. It's very interesting if you are a beginner.
I didn't like that because it was like a black box for me, so I decided to implement my own framework.
Later I found myself reading articles, seeing implementation not only for connect4 but for RL concepts, Markov decision process, k-armed bandit ...etc
I struggled to understand how people implemented these concepts because not all of them stick with the mathematical notation, and they were not all documented.
So I decided to create this API to simplify the use of these concept and even help the student to understand the concepts.


Concepts
-----------
This project contains 2 main categories, Environment and Agents.
The Environment represents the well-known game Connect4 (aka  Four in a Row)

![image](https://user-images.githubusercontent.com/52492864/128045136-8107d272-0b02-454a-bb0f-932d1079ec9f.png)

The Agents: 
- Random Agent: as the name implies, randomly choose a move based on uniform distribution 
- Heuristic Agent: using a specific heuristic I create, he chooses the move with high score. In Version2 the agent is able to block opponent attack
- Left Agent: this agent use a strategy that consists of playing the piece on the left
- Greedy Agent: this agent use the concept of Multi-Armed Bandit, he learns by playing and getting a reward
- DRL Agent: using RL

The reward system is as the following:
- Each time the agent win a game, he will receive a reward of +1.
- Each time the agent lost a game, he will punch by -1.
- And -10 in case of draw.
- And +1/42 for simple move.


challenges
-----------
During the programming of the game, I aim to build a robust program that do not bug and able to handle exceptions to ensure  continuously the work of the program.
Also, I optimized the program as much as the possible and that is shown by the way the variable is declared, the using of list with o(1) complexity for inserting, using POO paradigm especially with inheritance & polymorphism.
I adapted the environment to all the agents which is not all easy task especially for the agents that use the learning methods.


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
 
env.run(rounds=500)
```

Results
-----------
This figure represents the result of the battle between the agents, the percentage of winning is the result of 500 play.

![image](https://user-images.githubusercontent.com/52492864/128951936-59f8204c-71a9-4c0a-8399-3deaeb97c0c9.png)



License
-----------
You are free to use or extend this project for
educational purposes provided that (1) you do not distribute or publish solutions (2) you retain this notice and (3) you provide clear attribution to Achraf BELLA, including a link to this repository.

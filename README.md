# Game-AI-and-Reinforcement-Learning
-------------------------------------

Motivation (why i'm creating this API)
-----------
I was like every day searching in the net for new technologies or new courses related to Data Science, and then i find a very interesting courses in Kaggle related to Reinforcement Learning. Actually it was good except the fact that they implemented all the framework i didn't like that because it was like a black box for me so i decided to implement all the framework myself.
And then reading lot of article ethier in kaggle, meduim or other websites i find out that the implementation is far to be close to the mathematical concepts so i decided to implement an API that based shape the theoretical concept and help the student to understand the mathematics behind just reading the code and the description of the functions. 


Concepts
-----------
In this project i tired to implement the well-known game Connect 4  (aka  Four in a Row) and includ Reinforcement Learning concepts. Also, i provided the following agents:
- Random Agent
- Heuristic Agent
- Left Agent
- DRL Agent

For all these agent i build a reward system but specifically for the DRL Agent.
The reward system is as the following:
- Each time the agent win a game he will recieve a reward of +1.
- Each time the agent lost a game he will punch by -1.
- And -10 in case of draw / game over
- he will get +1/42 for simple move


This API contains 2 main classes: Env this class represent the environment of the the agent which means the bpard, and another class agents as the name implies it contains all the agents including the DRL agent.

![image](https://user-images.githubusercontent.com/52492864/128045136-8107d272-0b02-454a-bb0f-932d1079ec9f.png)

Concerning the environment of the game connect4 i modeling it using an array (Python object) that represent the field. Also i updated the design environement for all the agents.

the class agent contains 4 types of the agents for the moment.
- agent: this is the naive agent that use a uniform distrubition to choose the next vacant place to drop the piece.
- agent leftmost: this is use a strategy that consists of play the piece on the left.
- HeuristicAgent: i considre this agent as the most intelligent one because he uses a Heuristic that find patters that helps him to win easily against them (i didn't include the possibility to lame the attack of the opponent in the version=1.0)
- The DRL agent


Main Components Needed by the DRL Agent:
-----------
First we need to calculate the number of states for the DRL Agent.

Number of states that the input array has = (number of different values every item in the array can take) ^ (width*height)

Already the number of state for 1 vacant place is 3 (empty, 1, 2)
Then the number of states is 3^(6*7) = 3^42 = 109418989131512359209

As we use Q-learning the Q-table size would be the number of actions * 109418989131512359209 where the action is the choice of the column


Coding
-----------
During the coding i took into consideration all the case that could block the game either the full bord or the no vacant place and i used exception handling for that to pursuit the battle and i delete the score for this failed battle.

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

The result for a battle between random agents
-----------
![image](https://user-images.githubusercontent.com/52492864/128442802-7c39ff96-b09b-40e8-847e-01d80aafa0bb.png)

The result for a 3 rounds between random agents
-----------
![image](https://user-images.githubusercontent.com/52492864/128442954-77a97ec5-d4d0-43bb-911b-37e6d4771052.png)

The plot of reward per round
-----------
![image](https://user-images.githubusercontent.com/52492864/128442625-3b41b3fb-a1a6-45eb-ba57-257010d59748.png)

- left agents
- heuristic agents


Licensing
-----------
You are free to use or extend this project for
educational purposes provided that (1) you do not distribute or publish solutions (2) you retain this notice and (3) you provide clear attribution to Achraf BELLA, including a link to this repository.

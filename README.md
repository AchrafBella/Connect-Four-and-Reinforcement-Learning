# Game-AI-and-Reinforcement-Learning
-------------------------------------
In this project i tired to implement the well-known game Connect 4  (aka  Four in a Row) using Reinforcement Learning concepts. Also, i provided some agents with specific properties.

The reward system is as the following:
- Each time the agent win a game he will recieve a reward of +1  
- Each time the agent lost a game he will punch by -1
- he will get +1/42 for simple move
- he will punch by -10 if the game is over by filling all the vacant place in the board 

Requirements
-----------
Run pip install -r requirements.txt (Python 2)
pip3 install -r requirements.txt (Python 3)

Concepts
-----------
This project contains 2 main classes: Env this classe represent the environment of the the agent which means the game, and another class agents as the name implies it contains the agents.

Concerning the environment of the game connect for modeling it, i used an array (Python object) that represent the field. Also i updated the environement is design for all the simple agents, the heuristic agents and the RL agents


![image](https://user-images.githubusercontent.com/52492864/128045136-8107d272-0b02-454a-bb0f-932d1079ec9f.png)


the class agent contains 3 types of the agents for the moment (it could be more in the futur)
* agent: this is the naive agent that use a uniform distrubition to choose the next vacant place to drop the piece
* agent leftmost: this is use a strategy that consists of play the piece on the left 
* HeuristicAgent: i considre this agent as the most intelligent one because he uses a Heuristic that find patters that helps him to win easily against them (i didn't include the possibility to lame the attack of the opponent in this version=0.5)
* The DRL agent


Main Components Needed by the RL Agent:
-----------
For that we should upgrad the environment


Result
-----------
Simple battle result between:
- random agents
- left agents
- heuristic agents


![image](https://user-images.githubusercontent.com/52492864/128024170-b75ccee1-f253-4464-8a95-d635a98e4a56.png)

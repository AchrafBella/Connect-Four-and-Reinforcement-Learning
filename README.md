# Game-AI-and-Reinforcement-Learning
-------------------------------------
In this project i tired to implement the well-known game Connect Four  (aka  Four in a Row) using Reinforcement Learning concepts. Also, i provided some agents with specific properties.

Requirements
-----------
Run pip install -r requirements.txt (Python 2), or pip3 install -r requirements.txt (Python 3)

Concepts
-----------
This project contains 2 main classes: Env this classe represent the environment of the the agent which means the game, and another class agent as the name implies it contains the agents.
the class agent contains 3 types of the agents for the moment (it could be more in the futur)
* agent: this is the naive agent that use a uniform distrubition to choose the next vacant place to drop the piece
* agent leftmost: this is use a strategy that consists of play the piece on the left 
* HeuristicAgent: i considre this agent as the most intelligent one because he uses a Heuristic that find patters that helps him to win easily against them (i didn't include the possibility to lame the attack of the opponent in this version=0.5)
* The next agent will use deep reinforcement learning


Result
-----------
Simple battle result between:
- random agents
- left agents
- heuristic agents
![image](https://user-images.githubusercontent.com/52492864/128024170-b75ccee1-f253-4464-8a95-d635a98e4a56.png)

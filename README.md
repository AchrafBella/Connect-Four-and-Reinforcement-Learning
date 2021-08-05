# Game-AI-and-Reinforcement-Learning
-------------------------------------
In this project i tired to implement the well-known game Connect 4  (aka  Four in a Row) and includ Reinforcement Learning concepts. Also, i provided the following agents:
- Random Agent
- Heuristic Agent
- Left Agent
- DRL Agent

For all these agent i build a reward system but specifically for the DRL Agent.
The reward system is as the following:
- Each time the agent win a game he will recieve a reward of +1.
- Each time the agent lost a game he will punch by -1.
- he will get +1/42 for simple move


Concepts
-----------
This project contains 2 main classes: Env this class represent the environment of the the agent which means the bpard, and another class agents as the name implies it contains all the agents including the DRL agent.

![image](https://user-images.githubusercontent.com/52492864/128045136-8107d272-0b02-454a-bb0f-932d1079ec9f.png)

Concerning the environment of the game connect4 i modeling it using an array (Python object) that represent the field. Also i updated the design environement for all the agents.

the class agent contains 4 types of the agents for the moment.
* agent: this is the naive agent that use a uniform distrubition to choose the next vacant place to drop the piece.
* agent leftmost: this is use a strategy that consists of play the piece on the left.
* HeuristicAgent: i considre this agent as the most intelligent one because he uses a Heuristic that find patters that helps him to win easily against them (i didn't include the possibility to lame the attack of the opponent in the version=1.0)
* The DRL agent


Main Components Needed by the DRL Agent:
-----------
For that we should upgrad the environment


Requirements
-----------
Run pip install -r requirements.txt (Python 2)
pip3 install -r requirements.txt (Python 3)


Results
-----------

The result for a battle between random agents
-----------
![image](https://user-images.githubusercontent.com/52492864/128414016-696e6246-ac46-4da5-a041-236009633cd0.png)

The result for a 3 rounds between random agents
-----------
![image](https://user-images.githubusercontent.com/52492864/128414104-a161818d-3ccd-41bd-942f-3ef12ef893db.png)


- left agents
- heuristic agents


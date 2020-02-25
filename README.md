# Intelligent Targetting System
Targeting system based on Q-Learning designed to focus on a specific object.  In the
video game world, targeting systems exist in order to aid the player during game play by
putting the focus onto a specific object or enemy within the game. From there, it is much
easier to interact with that object or enemy as the players focus stays on it despite what is
happening around them. This interaction could range anywhere from pressing a button to
shooting at an enemy. It is these video game targeting systems that this project is based
upon. 

# Creating Environment
Blob class (blob.py) defines the environment. The environment consists of 3 blobs: Food (Green), User (Blue) and Enemy (Red). The goal state is when the user is able to reach the food blob. We utilise q learning to solve such a task. There are 4 defined actions in this environment, which are the diagonal direction movements. 
![](assets/env.jpg)

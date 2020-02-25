# Intelligent Targetting System
Targeting system based on Reinforcement Learning (Q-Learning to be more precise) designed to focus on a specific object.  In the
video game world, targeting systems exist in order to aid the player during game play by
putting the focus onto a specific object or enemy within the game. From there, it is much
easier to interact with that object or enemy as the players focus stays on it despite what is
happening around them. This interaction could range anywhere from pressing a button to
shooting at an enemy. It is these video game targeting systems that this project is based
upon. 

# Creating Environment
Blob class (blob.py) defines the environment. The environment consists of 3 blobs: Food (Green), User (Blue) and Enemy (Red). The goal state is when the user is able to reach the food blob. We utilise q learning to solve such a task. There are 4 defined actions in this environment, which are the diagonal direction movements. These directions can be thought of as the moves of a knight in chess.

<img src="https://github.com/arjunmann73/intelligent-targetting-qlearning/blob/master/assets/env.png" width="400" height="400" />

# Rewards 
* Movement: -1
* Hitting the enemy blob: -300
* Hitting the food blob: +25

# Initial Simulations (First 4000-5000 episodes)
<img src="https://github.com/arjunmann73/intelligent-targetting-qlearning/blob/master/assets/initially.gif" width="400" height="400" />

Not so great, let's train it more!

# Well trained agent?: 75,000 simulations to learn from.
<img src="https://github.com/arjunmann73/intelligent-targetting-qlearning/blob/master/assets/finally.gif" width="400" height="400" />

# Analysing

Let us first look at the reward over a range of simulations. Note that in the graph, the episode (simulation) number ranges from 0 - 50000, because we use a pre-trained q table which was created from the first 25,000 simulations. Overall, this represents the reward mean average over 3000 episodes (simulations). 

<img src="https://github.com/arjunmann73/intelligent-targetting-qlearning/blob/master/assets/75kepisodes.png" width="600" height="400" />

# Changing the environment

Before, only the user blob could move in different directions. Now, let us change this by adding random movements to the food and enemy blobs as well. Let's see how our trained agent (using the 75k episode q-table) does in this environment, we will analyse using the mean average of 50,000 episodes. 

<img src="https://github.com/arjunmann73/Intelligent-Targetting-QLearning/blob/master/run.gif" width="600" height="400" />

Analysing this with a graph, we see that the agent initially learns at a very good rate and then flatlines.

<img src="https://github.com/arjunmann73/Intelligent-Targetting-QLearning/blob/master/50k_new.png" width="600" height="400" />

# Tweaks for fun
We can learn a lot about q-learning by tweaking with the parameters (epsilon, epsilon_day, episodes, rewards etc.) which we set, running more episodes and changing the environment itself. We can add new actions such as moving horizontally or vertically, add more enemies and create multiple food blobs and see how fast we can train agents for such environments. It would be interesting to see how DQN's can be used and how it performs for such an environment. 

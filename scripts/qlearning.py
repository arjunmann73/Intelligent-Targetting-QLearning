import gym
import numpy as np
import matplotlib.pyplot as plt
env = gym.make('MountainCar-v0')

'''
print(env.observation_space.high) # These values might not be known in some environments [+0.6 _ +0.07]
print(env.observation_space.low)  # These values might not be known in some environments [-1.2 _ -0.07]
print(env.action_space.n)    # Number of actions available
'''

# Q-Learning settings
LEARNING_RATE = 0.1
DISCOUNT = 0.95
EPISODES = 5000
SHOW_EVERY = 1000
discrete_os_size = [20] * len(env.observation_space.high) # Dividing the range into 20 chunks or buckets
discrete_os_win_size = (env.observation_space.high - env.observation_space.low) / discrete_os_size
q_table = np.random.uniform(low=-2, high=0, size=(discrete_os_size + [env.action_space.n]))

epsilon = 0.25
START_EPSILON_DECAYING = 1
END_EPSILON_DECAYING = EPISODES // 2

epsilon_decaying_value = epsilon / (END_EPSILON_DECAYING - START_EPSILON_DECAYING)
ep_rewards = []
agg_ep_rewards = {'ep': [], 'avg': [], 'min': [], 'max': []}

def get_discrete_state(state):
    discrete_state = (state - env.observation_space.low)/discrete_os_win_size
    return tuple(discrete_state.astype(np.int))

for episode in range(EPISODES):
    episode_reward = 0
    discrete_state = get_discrete_state(env.reset())
    done = False

    if episode % SHOW_EVERY == 0:
        render = True
    else:
        render = False
    while not done:
        if np.random.random() > epsilon:
            action = np.argmax(q_table[discrete_state])
        else:
            action = np.random.randint(0, env.action_space.n)
        new_state, reward, done, _ = env.step(action)
        episode_reward += reward
        new_discrete_state = get_discrete_state(new_state)
        #print(new_state, reward, done)
        if render == True:
            env.render()
        if not done:
            max_future_q = np.max(q_table[new_discrete_state])
            current_q = q_table[discrete_state + (action, )]
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)  # Annoying part
            q_table[discrete_state + (action,)] = new_q
        elif new_state[0] >= env.goal_position:
            print("We made it on attempt: {}".format(episode))
            q_table[discrete_state + (action,)] = 0 # 0 is the reward in this case

        discrete_state = new_discrete_state

    if END_EPSILON_DECAYING >= episode >= START_EPSILON_DECAYING:
        epsilon -= epsilon_decaying_value

    ep_rewards.append(episode_reward)

    if not episode % SHOW_EVERY:
        average_reward = sum(ep_rewards[-SHOW_EVERY:]) / SHOW_EVERY
        agg_ep_rewards['ep'].append(episode)
        agg_ep_rewards['avg'].append(average_reward)
        agg_ep_rewards['max'].append(max(ep_rewards[-SHOW_EVERY:]))
        agg_ep_rewards['min'].append(min(ep_rewards[-SHOW_EVERY:]))
        print(f'Episode: {episode:>5d}, average reward: {average_reward:>4.1f}, current epsilon: {epsilon:>1.2f}')


env.close()
# Statistically determine the parameters
plt.plot(agg_ep_rewards['ep'], agg_ep_rewards['avg'], label="average rewards")
plt.plot(agg_ep_rewards['ep'], agg_ep_rewards['max'], label="max rewards")
plt.plot(agg_ep_rewards['ep'], agg_ep_rewards['min'], label="min rewards")
plt.legend(loc=4)
plt.show()


import gym
import cupy as cp  # Using CuPy instead of NumPy
import numpy as np

# Initialize environment
env = gym.make('FrozenLake-v1', is_slippery=False)
state_space_size = env.observation_space.n
action_space_size = env.action_space.n

# Hyperparameters
alpha = 0.8
gamma = 0.95
epsilon = 1.0
epsilon_decay = 0.995
epsilon_min = 0.01
num_episodes = 5000

# Q-table initialized on GPU
Q = cp.zeros((state_space_size, action_space_size))

for episode in range(num_episodes):
    state = env.reset()[0]
    done = False

    while not done:
        if np.random.rand() < epsilon:
            action = env.action_space.sample()
        else:
            action = int(cp.argmax(Q[state, :]).get())

        next_state, reward, done, truncated, info = env.step(action)

        # GPU update
        best_next_action = cp.max(Q[next_state, :])
        Q[state, action] = Q[state, action] + alpha * (reward + gamma * best_next_action - Q[state, action])

        state = next_state

    # Decay epsilon
    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

# Move Q-table back to CPU if needed
Q_final = cp.asnumpy(Q)





import gymnasium as gym
import numpy as np


def run(
    episodes, seed, a, g, decay_rate, render=False, verbose=True
):
    env = gym.make(
        "FrozenLake-v1",
        map_name="8x8",
        is_slippery=True,
        render_mode="human" if render else None,
    )

    q = np.zeros((env.observation_space.n, env.action_space.n))
    epsilon = 1.0
    epsilon_decay_rate = decay_rate

    rng = np.random.default_rng(seed)
    reward_per_episode = np.zeros(episodes)

    for episode in range(episodes):
        observation, _ = env.reset(seed=seed)
        terminated = False
        truncated = False

        while not terminated and not truncated:
            if rng.random() < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(q[observation, :])

            new_observation, reward, terminated, truncated, _ = env.step(
                action
            )

            q[observation, action] = q[
                observation, action
            ] + a * (
                reward
                + g * np.max(q[new_observation, :])
                - q[observation, action]
            )

            observation = new_observation

        epsilon = max(epsilon - epsilon_decay_rate, 0)
        reward_per_episode[episode] = reward

        if verbose:
            print(f'Episode {episode}, Reward: {reward}')

    env.close()

    if verbose:
        print(f'Finished run for seed={seed}')

    return reward_per_episode, q

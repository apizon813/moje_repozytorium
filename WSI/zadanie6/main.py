import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def experiment_a():
    pass


def experiment_g():
    pass


def experiment_e():
    pass


def run(
    episodes, seed, a, g, decay_rate, path, is_training=True, render=False
):

    env = gym.make(
        "FrozenLake-v1",
        map_name="8x8",
        is_slippery=False,
        render_mode="human" if render else None,
    )

    q = np.zeros((env.observation_space.n, env.action_space.n))

    learning_rate_a = a
    discount_factor_g = g
    epsilon = 1
    epsilon_decay_rate = decay_rate

    rng = np.random.default_rng()
    reward_per_episode = np.zeros(episodes)

    for i in range(episodes):
        observation, _ = env.reset(seed=1)
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
            ] + learning_rate_a * (
                reward
                + discount_factor_g * np.max(q[new_observation, :])
                - q[observation, action]
            )

            observation = new_observation

        epsilon = max(epsilon - epsilon_decay_rate, 0)

        if epsilon == 0:
            learning_rate_a = 0.0001

        if reward == 1:
            reward_per_episode[i] = 1

    env.close()

    sum_rewards = np.zeros(episodes)
    for t in range(episodes):
        start = max(0, t - 100)
        end = t + 1
        sum_rewards[t] = np.sum(reward_per_episode[start:end])

    plt.plot(sum_rewards)
    plt.savefig(f"{path}.png")

    df = pd.DataFrame(q)
    df.to_csv(f"{path}.csv")


if __name__ == "__main__":
    run(15000)

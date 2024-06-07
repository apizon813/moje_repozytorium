import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yaml


def experiment_a(args, seed):
    episodes = args['exp_a_episodes']
    a_values = args['a_values']
    g_value = args['exp_a_g_value']
    decay_rate = args['exp_a_e_value']
    path = args['results_path']
    path += f'seed_{str(seed)}"/"'

    for a_value in a_values:

        path += f"a_{str(a_value).replace('.', '')}"
        run(
            episodes=episodes,
            seed=seed,
            a=a_value,
            g=g_value,
            decay_rate=decay_rate,
            path=path
        )


def experiment_g():
    pass


def experiment_e():
    pass


def save_plot(path, size, rewards):
    episodes = len(rewards)
    sum_rewards = np.zeros(episodes)
    for t in range(episodes):
        start = max(0, t - size + 1)
        end = t + 1
        sum_rewards[t] = np.sum(rewards[start:end])
    plt.plot(sum_rewards)
    plt.savefig(f"{path}.png")


def save_q(path, q):
    df = pd.DataFrame(q)
    df.to_csv(f"{path}.csv")


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

    save_plot(
        path=path,
        size=100,
        rewards=reward_per_episode
        )

    save_q(path, q)


def main():
    with open('arguments.yaml', 'r') as file:
        args = yaml.safe_load(file)
    seeds = args['seeds']

    for seed in seeds:
        experiment_a(args, seed)
        experiment_g(args, seed)
        experiment_e(args, seed)


if __name__ == "__main__":
    main()

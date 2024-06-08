import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def get_mean_rewards(results, episodes):
    seeds_num = len(results)

    mean_rewards = np.zeros(episodes)
    stds = np.zeros(episodes)

    for episode in range(episodes):
        rewards = list()
        for seed in results:
            rewards.append(results[seed][episode])

        mean_reward = sum(rewards) / seeds_num
        mean_rewards[episode] = mean_reward

        std = np.std(rewards)
        stds[episode] = std

    return mean_rewards, stds


def get_moving_mean(rewards, stds, t_size, episodes):

    moving_mean = np.zeros(episodes)
    moving_stds = np.zeros(episodes)

    for episode in range(episodes):
        start = max(0, episode - t_size + 1)
        end = episode + 1
        moving_mean[episode] = np.sum(rewards[start:end])
        moving_stds[episode] = np.sum(stds[start:end])

    return moving_mean, moving_stds


def get_results(args, data_path, par_values):
    seeds = args['seeds']

    results = dict()
    for value in par_values:
        str_val = str(value).replace('.', '')
        path = data_path + str_val
        results[str_val] = dict()

        for seed in seeds:
            seed_path = path + f'/seed_{seed}_rewards'
            rewards = pd.read_csv(seed_path)
            results[str_val][str(seed)] = rewards

    return results


def save_group_plot(args, data_path, save_path, par_values):

    t_size = args['t_size']

    results = get_results(args, data_path, par_values)
    episodes = len(results[next(iter(results))]['rewards'])

    for value in par_values:
        value_results = results[value]

        rewards, stds = get_mean_rewards(value_results, episodes)
        moving_mean, moving_stds = get_moving_mean(
            rewards,
            stds,
            t_size,
            episodes
            )

        plt.plot(moving_mean)
    plt.savefig(save_path)
    plt.cla()


def save_to_csv(path, q):
    df = pd.DataFrame(q)
    df.to_csv(f"{path}.csv")

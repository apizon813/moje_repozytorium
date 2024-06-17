import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def compute_mean_rewards(data, episodes):

    mean_rewards = np.zeros(episodes)
    stds = np.zeros(episodes)

    for episode in range(episodes):
        rewards = [data[seed][episode] for seed in data]
        mean_rewards[episode] = np.mean(rewards)
        stds[episode] = np.std(rewards)

    return mean_rewards, stds


def get_moving_mean(rewards, stds, t_size, episodes):
    moving_mean = np.convolve(rewards, np.ones(t_size) / t_size, mode="same")
    moving_stds = np.convolve(stds, np.ones(t_size) / t_size, mode="same")
    return moving_mean, moving_stds


def get_results(args, data_path, param_key, par_values):
    seeds = args["seeds"]

    results = {}
    for value in par_values:
        str_val = str(value).replace(".", "")
        path = f"{data_path}{str_val}/"
        results[str_val] = {}

        for seed in seeds:
            seed_path = f"{path}seed_{seed}_rewards.csv"
            rewards = pd.read_csv(seed_path)
            rewards = pd.read_csv(seed_path, header=None).values.flatten()
            results[str_val][str(seed)] = rewards

    return results


def save_group_plot(args, data_path, save_path, par_values, param_key):
    t_size = args["t_size"]
    episodes = args["episodes"]
    results = get_results(args, data_path, param_key, par_values)
    plt.figure(figsize=(12, 6))

    for value in par_values:
        str_val = str(value).replace(".", "")
        value_results = results[str_val]

        rewards, stds = compute_mean_rewards(value_results, episodes)
        moving_mean, moving_stds = get_moving_mean(
            rewards, stds, t_size, episodes
        )

        x = np.arange(episodes)
        plt.plot(x, moving_mean, label=f"Parametr {param_key}={value}")
        plt.fill_between(
            x, moving_mean - moving_stds, moving_mean + moving_stds, alpha=0.2
        )
    plt.xlabel("Epizod")
    plt.ylabel("Średnia nagroda")
    plt.title(
        "Średnia nagroda w zależności od epizodu"
    )
    plt.legend()

    save_dir = os.path.dirname(save_path)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    plt.savefig(save_path)
    plt.clf()


def save_to_csv(path, q):
    df = pd.DataFrame(q)
    df.to_csv(f"{path}.csv", index=False)

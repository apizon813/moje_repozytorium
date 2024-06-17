import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def format_param_value(value):
    """Formatuje wartość parametru do użytku w nazwach plików."""
    return str(value).replace(".", "_").replace("-", "m").replace("e-", "e")


def compute_mean_rewards(data, episodes):
    seeds_num = len(data)

    mean_rewards = np.zeros(episodes)
    stds = np.zeros(episodes)

    for episode in range(episodes):
        rewards = []
        for seed in data:
            reward = data[seed]
            rewards.append(reward[episode])

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
        moving_mean[episode] = np.mean(rewards[start:end])
        moving_stds[episode] = np.mean(stds[start:end])

    return moving_mean, moving_stds


def get_results(args, data_path, par_values):
    seeds = args["seeds"]

    results = dict()
    for value in par_values:
        str_val = format_param_value(value)
        path = data_path + str_val + "/"
        results[str_val] = dict()

        for seed in seeds:
            seed_path = path + f"seed_{seed}_rewards.csv"
            print(f"Reading file: {seed_path}")  # Debug
            try:
                rewards = pd.read_csv(seed_path)
                rewards = rewards.drop(rewards.columns[0], axis=1).T
                results[str_val][str(seed)] = rewards
            except FileNotFoundError:
                print(f"File not found: {seed_path}")
                continue

    return results


def save_group_plot(args, data_path, save_path, par_values, param_key):
    t_size = args["t_size"]

    results = get_results(args, data_path, par_values)
    episodes = args["episodes"]

    for value in par_values:
        str_val = format_param_value(value)
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
    plt.title("Średnia nagroda w zależności od epizodu")
    plt.legend()
    plt.savefig(save_path)
    plt.cla()


def save_to_csv(path, data):
    """Zapisuje dane do pliku CSV."""
    df = pd.DataFrame(data)
    df.to_csv(f"{path}.csv")

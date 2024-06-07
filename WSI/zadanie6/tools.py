import pandas as pd
# import matplotlib.pyplot as plt


# def save_plot(path, size, rewards):
#     episodes = len(rewards)
#     sum_rewards = np.zeros(episodes)
#     for t in range(episodes):
#         start = max(0, t - size + 1)
#         end = t + 1
#         sum_rewards[t] = np.sum(rewards[start:end])
#     plt.plot(sum_rewards)
#     plt.savefig(f"{path}.png")


def save_q(path, q):
    df = pd.DataFrame(q)
    df.to_csv(f"{path}.csv")

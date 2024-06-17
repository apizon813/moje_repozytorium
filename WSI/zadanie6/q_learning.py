import gymnasium as gym
import numpy as np


def run(
    episodes,
    seed,
    a,
    g,
    decay_rate,
    T=None,
    strategy="epsilon_greedy",
    render=False,
    verbose=False,
):
    env = gym.make(
        "FrozenLake-v1",
        map_name="8x8",
        is_slippery=True,
        render_mode="human" if render else None,
    )

    q = np.zeros((env.observation_space.n, env.action_space.n))
    epsilon = 1.0
    rng = np.random.default_rng(seed)
    reward_per_episode = np.zeros(episodes)

    for episode in range(episodes):
        observation, _ = env.reset(seed=seed)
        terminated = False
        truncated = False
        total_reward = 0

        while not terminated and not truncated:
            if strategy == "epsilon_greedy":
                if rng.random() < epsilon:
                    action = env.action_space.sample()
                else:
                    action = np.argmax(q[observation, :])
                epsilon = max(epsilon - decay_rate, 0)
            elif strategy == "boltzmann" and T is not None:
                q_values = q[observation, :]
                max_q = np.max(q_values)
                exp_q = np.exp((q_values - max_q) / T)
                probabilities = exp_q / np.sum(exp_q)
                action = rng.choice(env.action_space.n, p=probabilities)
            else:
                raise ValueError(f"Unknown strategy: {strategy}")

            new_observation, reward, terminated, truncated, _ = env.step(
                action
            )

            q[observation, action] = q[observation, action] + a * (
                reward
                + g * np.max(q[new_observation, :])
                - q[observation, action]
            )

            observation = new_observation
            total_reward += reward

        reward_per_episode[episode] = total_reward

        if verbose:
            print(f"Episode {episode}, Total Reward: {total_reward}")

    env.close()

    if verbose:
        print(f"Finished run for seed={seed} with strategy={strategy}")

    return reward_per_episode, q

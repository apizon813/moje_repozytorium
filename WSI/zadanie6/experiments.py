from pathlib import Path
from tools import save_to_csv
from q_learning import run


def experiment_a(args):
    episodes = args['exp_a_episodes']
    seeds = args['seeds']
    a_values = args['a_values']
    g_value = args['exp_a_g_value']
    decay_rate = args['exp_a_e_value']
    path = args['results_path']
    path += 'exp_a/'

    for a_value in a_values:
        path_a_value = path + f"a_{str(a_value).replace('.', '')}/"
        Path(path_a_value).mkdir(parents=True, exist_ok=True)

        for seed in seeds:

            rewards, q = run(
                episodes=episodes,
                seed=seed,
                a=a_value,
                g=g_value,
                decay_rate=decay_rate,
            )

            rewards_path = path_a_value + f'seed_{seed}_rewards'
            q_path = path_a_value + f'seed_{seed}_q'
            save_to_csv(rewards_path, rewards)
            save_to_csv(q_path, q)
    print('success')


def experiment_g(args):
    episodes = args['exp_g_episodes']
    seeds = args['seeds']
    g_values = args['g_values']
    a_value = args['exp_g_a_value']
    decay_rate = args['exp_g_e_value']
    path = args['results_path']
    path += 'exp_g/'

    for g_value in g_values:
        path_g_value = path + f"g_{str(g_value).replace('.', '')}"
        Path(path_g_value).mkdir(parents=True, exist_ok=True)

        for seed in seeds:

            rewards, q = run(
                episodes=episodes,
                seed=seed,
                a=a_value,
                g=g_value,
                decay_rate=decay_rate,
            )

            rewards_path = path_g_value + f'/seed_{seed}_rewards'
            q_path = path_g_value + f'/seed_{seed}_q'
            save_to_csv(rewards_path, rewards)
            save_to_csv(q_path, q)
    print('success')


def experiment_e(args):
    pass

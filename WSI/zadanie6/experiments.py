from pathlib import Path
from tools import save_q, save_plot
from q_learning import run


def experiment_a(args, seed):
    episodes = args['exp_a_episodes']
    a_values = args['a_values']
    g_value = args['exp_a_g_value']
    decay_rate = args['exp_a_e_value']
    path = args['results_path']
    path += f'seed_{str(seed)}/'
    t_size = args['t_size']

    Path(path).mkdir(parents=True, exist_ok=True)

    for a_value in a_values:

        rewards, q = run(
            episodes=episodes,
            seed=seed,
            a=a_value,
            g=g_value,
            decay_rate=decay_rate,
        )

        results_path = path + f"a_{str(a_value).replace('.', '')}"

        save_q(results_path, q)
        save_plot(results_path, t_size, rewards)


def experiment_g(args, seed):
    pass


def experiment_e(args, seed):
    pass

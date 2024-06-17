from pathlib import Path
from tools import (
    save_to_csv,
    format_param_value,
)
from q_learning import run


def experiment_a(args):
    run_experiment(
        args,
        "exp_a",
        args["a_values"],
        "a",
        args["exp_a_g_value"],
        args["exp_a_e_value"],
    )


def experiment_g(args):
    run_experiment(
        args,
        "exp_g",
        args["g_values"],
        "g",
        args["exp_g_a_value"],
        args["exp_g_e_value"],
    )


def experiment_e(args):
    run_experiment(
        args,
        "exp_e",
        args["e_values"],
        "e",
        args["exp_e_a_value"],
        args["exp_e_g_value"],
    )


def experiment_t(args):
    run_experiment(
        args,
        "exp_t",
        args["t_values"],
        "t",
        args["exp_t_a_value"],
        args["exp_t_g_value"],
        decay_rate=None,
    )


def run_experiment(
    args, exp_name, param_values, param_key, fixed_a, fixed_g, decay_rate
):
    episodes = args[f"{exp_name}_episodes"]
    seeds = args["seeds"]
    path = f"{args['results_path']}{exp_name}/"

    for value in param_values:
        formatted_value = format_param_value(value)
        path_value = f"{path}{param_key}_{formatted_value}/"
        Path(path_value).mkdir(parents=True, exist_ok=True)

        for seed in seeds:
            print(
                f"Running {exp_name} with {param_key}={value}, seed={seed}"
            )

            rewards, q = run(
                episodes=episodes,
                seed=seed,
                a=value if param_key == "a" else fixed_a,
                g=value if param_key == "g" else fixed_g,
                decay_rate=value if param_key == "e" else decay_rate,
                T=value if param_key == "t" else None,
                strategy="boltzmann" if param_key == "t" else "epsilon_greedy",
                verbose=True,
            )

            rewards_path = f"{path_value}seed_{seed}_rewards"
            q_path = f"{path_value}seed_{seed}_q"
            print(f"Saving rewards to: {rewards_path}")
            save_to_csv(rewards_path, rewards)
            print(f"Saving Q-table to: {q_path}")
            save_to_csv(q_path, q)

    print(f"Experiment {exp_name} completed")

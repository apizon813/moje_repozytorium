from pathlib import Path
from tools import save_to_csv
from q_learning import run


def experiment_a(args):
    run_experiment(
        args,
        "exp_a",
        args["a_values"],
        "a",
        args["exp_a_g_value"],
        args["exp_a_e_value"],
        args["exp_e_e_value"],
    )


def experiment_g(args):
    run_experiment(
        args,
        "exp_g",
        args["g_values"],
        "g",
        args["exp_g_a_value"],
        args["exp_g_e_value"],
        args["exp_e_e_value"],
    )


def experiment_e(args):
    run_experiment(
        args=args,
        exp_name="exp_e",
        param_values=args["e_values"],
        param_key="e",
        fixed_a=args["exp_e_a_value"],
        fixed_g=args["exp_e_g_value"],
    )


def run_experiment(
    args,
    exp_name,
    param_values,
    param_key,
    fixed_a=None,
    fixed_g=None,
    fixed_e=None,
):
    episodes = args[f"{exp_name}_episodes"]
    seeds = args["seeds"]
    path = f"{args['results_path']}{exp_name}/"

    for value in param_values:
        str_val = str(value).replace(".", "")
        path_value = f"{path}{param_key}_{str_val}/"
        Path(path_value).mkdir(parents=True, exist_ok=True)

        for seed in seeds:
            rewards, q = run(
                episodes=episodes,
                seed=seed,
                a=value if param_key == "a" else fixed_a,
                g=value if param_key == "g" else fixed_g,
                decay_rate=value if param_key == "e" else fixed_e,
            )

            rewards_path = f"{path_value}seed_{seed}_rewards"
            q_path = f"{path_value}seed_{seed}_q"
            save_to_csv(rewards_path, rewards)
            save_to_csv(q_path, q)
    print(f"Experiment {exp_name} completed")

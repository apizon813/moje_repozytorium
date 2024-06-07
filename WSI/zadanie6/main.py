import yaml
from experiments import (
    experiment_a,
    experiment_g,
    experiment_e
    )


def main():
    with open('arguments.yaml', 'r') as file:
        args = yaml.safe_load(file)
    seeds = args['seeds']

    run_exp_a = args['run_exp_a']
    run_exp_g = args['run_exp_a']
    run_exp_e = args['run_exp_a']

    for seed in seeds:
        if run_exp_a:
            experiment_a(args, seed)
        if run_exp_g:
            experiment_g(args, seed)
        if run_exp_e:
            experiment_e(args, seed)


if __name__ == "__main__":
    main()

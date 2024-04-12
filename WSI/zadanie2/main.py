from parameters import (
    get_exp1_params,
    get_exp2_params,
    get_exp3_params,
    get_exp4_params,
    get_exp5_params,
    get_exp6_params
)
from solver import Evolution
from tools import save_data
from plots import (
    plotter,
    fitness_plot,
    plot_end_populations
)


def experiment(params_set):

    solutions = []
    for args in params_set:

        solution = Evolution(args)

        for i in range(args.max_generations):
            solution.evolve()
            var = args.variable
            var_val = getattr(args, var)
            print(f'{var}={var_val} gen={i+1}')

        solutions.append(solution)
        plotter(solution, args)
    save_data(solutions, args)

    fitness_plot(solutions, args)
    plot_end_populations(solutions, params_set)


def main():
    exp1_params = get_exp1_params()
    experiment(exp1_params)

    exp2_params = get_exp2_params()
    experiment(exp2_params)

    exp3_params = get_exp3_params()
    experiment(exp3_params)

    exp4_params = get_exp4_params()
    experiment(exp4_params)

    exp5_params = get_exp5_params()
    experiment(exp5_params)

    exp6_params = get_exp6_params()
    experiment(exp6_params)


if __name__ == '__main__':
    main()

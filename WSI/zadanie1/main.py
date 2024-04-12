from solver import Solver
from parameters import (
    EXP1_PARAMETERS,
    EXP2_PARAMETERS,
    EXP3_PARAMETERS
)
from save_results import (
    exp1_save_results,
    save_results_2d_function
)
from functions import (
    quadratic,
    rastrigin,
    griewank
)
from plots import (
    quadratic_plot,
    rastrigin_plot,
    griewank_plot
)


def experiment_quadratic(args):
    start_point = args['start_point']
    beta = args['beta']
    steps = args['steps']
    trsh = args['trsh']
    results_path = args['results_path']
    plot_path = args['plot_path']

    fun = quadratic()
    solution = Solver(fun, 1, start_point, beta)
    solution.step_till_stop(steps, trsh)
    exp1_save_results(results_path, solution)
    quadratic_plot(plot_path, solution)

    return solution


def experiment_2d_function(args, function):
    start_points = args['start_points']
    betas = args['betas']
    dimension = args['dimension']
    steps = args['steps']
    trsh = args['trsh']

    solutions = []
    for start_point in start_points:
        print(f'Start point: {start_point}')
        for beta in betas:
            print(f'Beta: {beta}')
            solution = Solver(
                function,
                dimension,
                start_point,
                beta
            )
            solution.step_till_stop(steps, trsh)
            solutions.append(solution)
    return solutions


def main():
    experiment_quadratic(EXP1_PARAMETERS)

    function = rastrigin(2)
    solutions = experiment_2d_function(EXP2_PARAMETERS, function)
    results_path = EXP2_PARAMETERS['results_path']
    plot_path = EXP2_PARAMETERS['plot_path']
    save_results_2d_function(results_path, solutions)
    rastrigin_plot(results_path, plot_path)

    function = griewank()
    solutions = experiment_2d_function(EXP3_PARAMETERS, function)
    results_path = EXP3_PARAMETERS['results_path']
    plot_path = EXP3_PARAMETERS['plot_path']
    save_results_2d_function(results_path, solutions)
    griewank_plot(results_path, plot_path)


if __name__ == '__main__':
    main()

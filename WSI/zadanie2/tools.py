from dataclasses import dataclass
import numpy as np
from math import sqrt


@dataclass
class ExpParams():
    function: str
    start_points_mean: tuple[float]
    start_points_sigma: float
    size: int
    pc: float
    pm: float
    mutation_sigma: float
    max_generations: int
    data_path: str
    plot_path: str
    fit_path: str
    plot_end_path: str
    plot_generations: list[int]
    variable: str


def get_start_points(mean, sigma, size):
    x_mean = mean[0]
    y_mean = mean[1]

    x = np.random.normal(x_mean, sigma, size)
    y = np.random.normal(y_mean, sigma, size)

    points = []
    for i in range(size):
        point = (x[i], y[i])
        points.append(point)
    return points


def save_data(solutions, args):
    path = args.data_path

    with open(path, 'w') as output:
        output.write(f'{args.variable},champ_x1,champ_x2,champ_cost,MSE\n')
        for solution in solutions:
            data = solution.data
            var_val = getattr(solution, args.variable)
            champ_x1 = data[args.max_generations][2][0]
            champ_x2 = data[args.max_generations][2][1]
            champ_cost = data[args.max_generations][3]
            mse = sqrt(champ_x1 ** 2 + champ_x2 ** 2)

            line = [
                str(var_val),
                str(champ_x1),
                str(champ_x2),
                str(champ_cost),
                str(mse)
            ]
            line = ','.join(line)
            output.write(line + '\n')

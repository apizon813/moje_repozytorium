EXP1_PARAMETERS = {
    'start_point': (8,),
    'beta': 0.9,
    'steps': 30,
    'trsh': 0,
    'results_path': './results/exp1_results.txt',
    'plot_path': './plots/exp1_plot.png'
}

EXP2_START_POINTS = [
    (0.6, 0.5),
    (0.25, -0.3),
    (-3.5, -0.5),
    (-4.4, 4.4),
    (0, 2.5),
    (2.5, -4.5),
    (-1.7, -2.3),
    (2., -1.8),
    (3.2, 3.8),
    (-1.6, -0.6)
]

EXP2_BETAS = [
    0.05,
    0.001,
    0.0001,
    0.00001,
    1.,
]

EXP2_PARAMETERS = {
    'start_points': EXP2_START_POINTS,
    'betas': EXP2_BETAS,
    'dimension': 2,
    'steps': 200,
    'trsh': 0,
    'results_path': './results/exp2_results.txt',
    'plot_path': './plots/exp2_plot.png'
}

EXP3_START_POINTS = [
    (0.25, -0.3),
    (2.8, 0.5),
    (-4.4, 4.4),
    (0, 2.5),
    (-2.3, 3.4),
    (2.5, -4.5),
    (-2.1, -2.),
    (3., -0.5),
    (1., 4.),
    (-4., 2.)
]

EXP3_BETAS = [
    5.,
    1.,
    0.1,
    0.01
]

EXP3_PARAMETERS = {
    'start_points': EXP3_START_POINTS,
    'betas': EXP3_BETAS,
    'dimension': 2,
    'steps': 200,
    'trsh': 0,
    'results_path': './results/exp3_results.txt',
    'plot_path': './plots/exp3_plot.png'
}

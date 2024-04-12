
from tools import ExpParams
import copy


RASTR_EXP_PARAMS = ExpParams(
    function='rastrigin',
    start_points_mean=(2.5, 2.5),
    start_points_sigma=1.,
    size=20,
    pc=0.5,
    pm=0.5,
    mutation_sigma=1.,
    max_generations=100,
    data_path='./rastrigin_tests/results/exp{}/results{}.txt',
    plot_path='./rastrigin_tests/plots/exp{}/plot{}.png',
    fit_path='./rastrigin_tests/plots/exp{}/plot_fit.png',
    plot_end_path='./rastrigin_tests/plots/exp{}/plot_end_pops.png',
    plot_generations=[0, 20, 40, 60, 80, 100],
    variable=None

)

PC_VALUES = [0., 0.1, 0.3, 0.5, 0.7, 1.]
PM_VALUES = [0., 0.1, 0.3, 0.5, 0.7, 1.]
SIZES = [10, 20, 40, 60, 80, 100]


def get_exp1_params():
    params_set = []
    for pc in PC_VALUES:
        params = copy.deepcopy(RASTR_EXP_PARAMS)
        params.pc = pc
        str_pc = str(pc).replace('.', '')
        params.data_path = params.data_path.format('1', '_pc')
        params.plot_path = params.plot_path.format('1', f'_pc{str_pc}')
        params.fit_path = params.fit_path.format('1')
        params.plot_end_path = params.plot_end_path.format('1')
        params.variable = 'pc'
        params_set.append(params)
    return params_set


def get_exp2_params():
    params_set = []
    for pm in PM_VALUES:
        params = copy.deepcopy(RASTR_EXP_PARAMS)
        params.pm = pm
        str_pm = str(pm).replace('.', '')
        params.data_path = params.data_path.format('2', '_pm')
        params.plot_path = params.plot_path.format('2', f'_pm{str_pm}')
        params.fit_path = params.fit_path.format('2')
        params.plot_end_path = params.plot_end_path.format('2')

        params.variable = 'pm'
        params_set.append(params)
    return params_set


def get_exp3_params():
    params_set = []
    for size in SIZES:
        params = copy.deepcopy(RASTR_EXP_PARAMS)
        params.size = size
        params.data_path = params.data_path.format('3', '_size')
        params.plot_path = params.plot_path.format('3', f'_size{size}')
        params.fit_path = params.fit_path.format('3')
        params.plot_end_path = params.plot_end_path.format('3')

        params.variable = 'size'
        params_set.append(params)
    return params_set


GRIEW_EXP_PARAMS = ExpParams(
    function='griewank',
    start_points_mean=(25, 25),
    start_points_sigma=5.,
    size=40,
    pc=0.5,
    pm=0.5,
    mutation_sigma=10.,
    max_generations=150,
    data_path='./griewank_tests/results/exp{}/results{}.txt',
    plot_path='./griewank_tests/plots/exp{}/plot{}.png',
    fit_path='./griewank_tests/plots/exp{}/plot_fit.png',
    plot_end_path='./griewank_tests/plots/exp{}/plot_end_pops.png',

    plot_generations=[0, 30, 60, 90, 120, 150],
    variable=None

)

PC_VALUES = [0., 0.1, 0.3, 0.5, 0.7, 1.]
PM_VALUES = [0., 0.1, 0.3, 0.5, 0.7, 1.]
SIZES = [10, 20, 40, 60, 80, 100]

# PC_VALUES = [0.5]
# PM_VALUES = [0.5]
# SIZES = [10, 20, 40, 100]


def get_exp4_params():
    params_set = []
    for pc in PC_VALUES:
        params = copy.deepcopy(GRIEW_EXP_PARAMS)
        params.pc = pc
        str_pc = str(pc).replace('.', '')
        params.data_path = params.data_path.format('4', '_pc')
        params.plot_path = params.plot_path.format('4', f'_pc{str_pc}')
        params.fit_path = params.fit_path.format('4')
        params.plot_end_path = params.plot_end_path.format('4')

        params.variable = 'pc'
        params_set.append(params)
    return params_set


def get_exp5_params():
    params_set = []
    for pm in PM_VALUES:
        params = copy.deepcopy(GRIEW_EXP_PARAMS)
        params.pm = pm
        str_pm = str(pm).replace('.', '')
        params.data_path = params.data_path.format('5', '_pm')
        params.plot_path = params.plot_path.format('5', f'_pm{str_pm}')
        params.fit_path = params.fit_path.format('5')
        params.plot_end_path = params.plot_end_path.format('5')

        params.variable = 'pm'
        params_set.append(params)
    return params_set


def get_exp6_params():
    params_set = []
    for size in SIZES:
        params = copy.deepcopy(GRIEW_EXP_PARAMS)
        params.size = size
        params.data_path = params.data_path.format('6', '_size')
        params.plot_path = params.plot_path.format('6', f'_size{size}')
        params.fit_path = params.fit_path.format('6')
        params.plot_end_path = params.plot_end_path.format('6')

        params.variable = 'size'
        params_set.append(params)
    return params_set

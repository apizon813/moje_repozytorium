from game import TicTacToe
from players import (
    Oponent,
    Player
)
from minmax import MiniMax
import matplotlib.pyplot as plt
from tools import (
    measure_depth,
    time_measure,
    save_starting_moves,
    measure_times_no_pruning,
    mean_values,
    save_progress_times
)


def play_game(parameters):
    dimension = parameters[0]
    player_max = parameters[1]
    player_min = parameters[2]

    if player_max:
        player_max = Player()
    else:
        player_max = Oponent(pruning=True, max=True)

    if player_min:
        player_min = Player()
    else:
        player_min = Oponent(pruning=True, max=False)

    game = TicTacToe(
        dimension,
        player_max,
        player_min
    )

    game.print_board()

    while not game.finished:
        game.ask_for_move()
        game.print_board()
    game.print_winner()


def measure_starting_moves(parameters):
    dimension = parameters[0]
    measure_number = parameters[1]
    path = parameters[2]

    game = TicTacToe(dimension)
    data = {}
    for move in game.possible_moves():
        data[move] = {}
        minmax = MiniMax()
        data_depth = measure_depth(game, minmax, move)
        data_time = time_measure(game, minmax, move, measure_number)
        data[move].update(data_depth)
        data[move]['time'] = data_time
    save_starting_moves(data, path)

    game = TicTacToe(dimension)
    data = {}
    alpha = -2
    beta = 2
    for move in game.possible_moves():
        data[move] = {}
        minmax = MiniMax(True)
        data_depth = measure_depth(game, minmax, move, alpha, beta)
        data_time = time_measure(
            game,
            minmax,
            move,
            measure_number,
            alpha,
            beta
            )
        data[move].update(data_depth)
        data[move]['time'] = data_time
    path = path[:-4] + '_pruning' + path[-4:]
    save_starting_moves(data, path)


def measure_progress(parameters):
    dimension = parameters[0]
    plot_path = parameters[1]
    number = parameters[2]
    results_path = parameters[3]

    data_set = []
    for i in range(number):
        player_max = Oponent(max=True)
        player_min = Oponent(max=False)
        game = TicTacToe(
            dimension,
            player_max,
            player_min
        )
        data_set.append(measure_times_no_pruning(game))
    save_progress_times(data_set, results_path)
    data_no_pruning = mean_values(data_set)

    data_set = []
    for i in range(number):
        player_max = Oponent(pruning=True, max=True)
        player_min = Oponent(pruning=True, max=False)
        game = TicTacToe(
            dimension,
            player_max,
            player_min
        )
        data_set.append(measure_times_no_pruning(game))

    results_path = results_path[:-4] + '_pruning' + results_path[-4:]
    save_progress_times(data_set, results_path)
    data_with_pruning = mean_values(data_set)

    plot_times(plot_path, data_no_pruning, data_with_pruning)


def plot_times(path, data_no_pruning, data_with_pruning):
    print('test1')
    fig, ax = plt.subplots()
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ax.plot(x, data_no_pruning, label='no pruning')
    ax.plot(x, data_with_pruning, label='with pruning')
    plt.xlabel('progress [move]')
    plt.ylabel('time [s]')
    ax.legend()
    ax.set_yscale('log')
    print('test2')
    fig.savefig(path)

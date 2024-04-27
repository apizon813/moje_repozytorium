from game import TicTacToe
from players import (
    Oponent,
    Player
)
from minmax import MinMax
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
    path_nopr = parameters[2]
    path_pr = path_nopr[:-4] + '_pruning' + path_nopr[-4:]

    game = TicTacToe(dimension)
    data_nopr = {}
    data_pr = {}
    for move in game.possible_moves():
        data_nopr[move] = {}
        data_pr[move] = {}

        minmax_nopr = MinMax()
        minmax_pr = MinMax(True)

        data_nopr_depth = measure_depth(game, minmax_nopr, move)
        data_pr_depth = measure_depth(game, minmax_nopr, move, -2, 2)

        data_nopr_time, data_nopr_dev = time_measure(
            game,
            minmax_nopr,
            move,
            measure_number
            )
        data_pr_time, data_pr_dev = time_measure(
            game,
            minmax_pr,
            move,
            measure_number
            )

        data_nopr[move].update(data_nopr_depth)
        data_nopr[move]['time'] = data_nopr_time
        data_nopr[move]['stdev'] = data_nopr_dev

        data_pr[move].update(data_pr_depth)
        data_pr[move]['time'] = data_pr_time
        data_pr[move]['stdev'] = data_pr_dev

    save_starting_moves(data_nopr, path_nopr)
    save_starting_moves(data_pr, path_pr)


def measure_middle_game(parameters):
    dimension = parameters[0]
    measure_number = parameters[1]
    path_nopr = parameters[2]
    path_pr = path_nopr[:-4] + '_pruning' + path_nopr[-4:]
    states = [
        parameters[3],
        parameters[4],
        parameters[5]
    ]

    game = TicTacToe(dimension)
    data_nopr = {}
    data_pr = {}
    for index, state in enumerate(states):
        data_nopr[index] = {}
        data_pr[index] = {}

        game.board = state['board']
        game.who_moves = state['who_moves']
        move = state['move']

        minmax_nopr = MinMax()
        minmax_pr = MinMax(True)

        data_nopr_depth = measure_depth(game, minmax_nopr, move)
        data_pr_depth = measure_depth(game, minmax_nopr, move, -2, 2)

        data_nopr_time, data_nopr_dev = time_measure(
            game,
            minmax_nopr,
            move,
            measure_number
            )
        data_pr_time, data_pr_dev = time_measure(
            game,
            minmax_pr,
            move,
            measure_number,
            -2,
            2
            )

        data_nopr[index].update(data_nopr_depth)
        data_nopr[index]['time'] = data_nopr_time
        data_nopr[index]['stdev'] = data_nopr_dev

        data_pr[index].update(data_pr_depth)
        data_pr[index]['time'] = data_pr_time
        data_pr[index]['stdev'] = data_pr_dev

    save_starting_moves(data_nopr, path_nopr)
    save_starting_moves(data_pr, path_pr)


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
    fig, ax = plt.subplots()
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ax.plot(x, data_no_pruning, label='no pruning')
    ax.plot(x, data_with_pruning, label='with pruning')
    plt.xlabel('progress [move]')
    plt.ylabel('time [s]')
    ax.legend()
    ax.set_yscale('log')
    fig.savefig(path)

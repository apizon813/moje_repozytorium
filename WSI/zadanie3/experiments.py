from game import TicTacToe
from players import (
    Oponent,
    Player
)
from minmax import MiniMax
from timeit import default_timer as timer
# import matplotlib.pyplot as plt


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


def save_measures(data, path):
    with open(path, 'w') as file:
        file.write('move,time,nodes,mean_depth\n')
        for move in data:
            time = data[move]['time']
            nodes = data[move]['nodes']
            mean_depth = data[move]['mean_depth']
            row = f'{move},{time},{nodes},{mean_depth}\n'
            file.write(row)


def time_measure(game, minmax, move, n, alpha=None, beta=None):
    data = []
    for i in range(n):
        start = timer()
        minmax.eval(game, move, alpha, beta)
        end = timer()
        minmax.reset()
        data.append(end - start)
        print(f'{i}: {end - start}')
    mean_time = sum(data) / len(data)
    return mean_time


def measure_depth(game, minmax, move, alpha=None, beta=None):
    data = {}
    minmax.eval(game, move, alpha, beta)
    data['mean_depth'] = minmax.mean_depth()
    data['nodes'] = minmax.nodes
    minmax.reset()
    return data


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
    save_measures(data, path)

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
    save_measures(data, path)


def measure_progress(parameters):
    dimension = parameters[0]
    path = parameters[1]

    player_max = Oponent(max=True)
    player_min = Oponent(max=False)
    game = TicTacToe(
        dimension,
        player_max,
        player_min
    )

    data_no_pruning = []
    while not game.finished:
        start = timer()
        game.ask_for_move()
        end = timer()
        data_no_pruning.append(end - start)

    player_max = Oponent(pruning=True, max=True)
    player_min = Oponent(pruning=True, max=False)
    game = TicTacToe(
        dimension,
        player_max,
        player_min
    )

    data_with_pruning = []
    while not game.finished:
        start = timer()
        game.ask_for_move()
        end = timer()
        data_with_pruning.append(end - start)
    print('to koniec')

    # plot_times(path, data_no_pruning, data_with_pruning)


# def plot_times(path, data_no_pruning, data_with_pruning):
#     print('test1')
#     fig, ax = plt.subplots()
#     x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     ax.plot(x, data_no_pruning, label='no pruning')
#     ax.plot(x, data_with_pruning, label='with pruning')
#     plt.xlabel('progress [move]')
#     plt.ylabel('time [s]')
#     ax.legend()
#     print('test2')
#     fig.savefig(path)

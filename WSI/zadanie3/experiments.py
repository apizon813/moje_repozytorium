from game import TicTacToe
from players import (
    Oponent,
    Player
)
from minmax import MiniMax
from timeit import default_timer as timer


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
            time = data[move]['ex_time']
            nodes = data[move]['nodes']
            mean_depth = data[move]['mean_depth']
            row = f'{move},{time},{nodes},{mean_depth}\n'
            file.write(row)


def time_measure(game, minmax, move, n):
    data = []
    for i in range(n):
        start = timer()
        minmax.eval(game, move)
        end = timer()
        minmax.reset()
        data.append(end - start)
        print(f'{i}: {end - start}')
    mean_time = sum(data) / len(data)
    return mean_time


def measure_depth(game, minmax, move):
    data = {}
    minmax.eval(game, move)
    data['mean_depth'] = minmax.mean_depth()
    data['nodes'] = minmax.nodes
    minmax.reset()
    return data


# move czas srednia_gl nodes

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
        data[move]['ex_time'] = data_time
    save_measures(data, path)


def measure_time(parameters):
    dimension = parameters[0]
    board = parameters[1]
    move = parameters[2]
    who_starts = parameters[3]
    measure_number = parameters[4]
    path = parameters[5]
    pruning = parameters[6]

    game = TicTacToe(dimension)
    game.board = board
    game.who_moves = who_starts
    minmax = MiniMax(pruning)

    data = []
    for i in range(measure_number):
        start = timer()
        minmax.eval(game, move, -2, 2)
        end = timer()
        data.append(end - start)

    with open(path, 'w') as file:
        for time in data:
            file.write(f'{time}\n')

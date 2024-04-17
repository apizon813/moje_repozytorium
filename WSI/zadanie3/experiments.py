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


def measure_depth(parameters):
    dimension = parameters[0]
    board = parameters[1]
    move = parameters[2]
    who_starts = parameters[3]
    path = parameters[4]
    pruning = parameters[5]

    game = TicTacToe(dimension)
    game.board = board
    game.who_moves = who_starts
    minmax = MiniMax(pruning)

    minmax.eval(game, move, -2, 2)
    data = minmax.mean_depth()
    with open(path, 'w') as file:
        file.write(str(data))

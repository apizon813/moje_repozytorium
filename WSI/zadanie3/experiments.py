from game import TicTacToe
from players import (
    Oponent,
    Player
)
from minmax import minmax
from timeit import default_timer as timer


def play_game(parameters):
    dimension = parameters[0]
    player_max = parameters[1]
    player_min = parameters[2]

    if player_max:
        player_max = Player()
    else:
        player_max = Oponent(max=True)

    if player_min:
        player_min = Player()
    else:
        player_min = Oponent(max=False)

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

    game = TicTacToe(dimension)
    game.board = board
    game.who_moves = who_starts

    data = []
    for i in range(measure_number):
        start = timer()
        minmax(game, move)
        end = timer()
        data.append(end - start)

    with open(path, 'w') as file:
        for time in data:
            file.write(f'{time}\n')

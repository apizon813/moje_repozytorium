import copy


def minmax(game, move, depth):
    stop_depth = 6
    board = copy.deepcopy(game)
    board.change_board(move)

    if board.finished:
        if depth == stop_depth:
            pass
        return board.state

    maxim = board.who_moves

    if maxim:
        values = []
        for move in board.possible_moves():
            value = minmax(board, move, depth + 1)
            values.append(value)
        if depth == stop_depth:
            pass
        return max(values)

    else:
        values = []
        for move in board.possible_moves():
            value = minmax(board, move, depth + 1)
            values.append(value)
        if depth == stop_depth:
            pass
        return min(values)

def minmax(game, move, depth):
    # stop_depth = 6
    game.change_board(move)

    if game.finished:
        # if depth == stop_depth:
        #     pass
        state = game.state
        game.undo()
        return state

    max_moves: bool = game.who_moves

    values = []
    possible_moves = game.possible_moves()
    for move in possible_moves:
        value = minmax(game, move, depth + 1)
        values.append(value)
    # if depth == stop_depth:
    #     pass
    if max_moves:
        game.undo()
        return max(values)
    else:
        game.undo()
        return min(values)

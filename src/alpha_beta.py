from src.state import Turn


def alpha_beta(state, depth, a, b, max_player):
    """
    Minimax with alpha–beta pruning implementation
    """

    if depth == 0 or state.is_terminal_state():
        return heuristic_value(state)

    if max_player is True:
        value = -10000
        for s in state.get_states():
            value = max(value, alpha_beta(s, depth - 1, a, b, False))
            a = max(a, value)
            if a >= b:
                break
        return value

    else:
        value = 10000
        for s in state.get_states():
            value = min(value, alpha_beta(s, depth - 1, a, b, True))
            b = min(b, value)
            if b <= a:
                break
        return value


def heuristic_value(state):
    """"
    :param state (State): model stanja na tabli
    :return: broj poena (heuristic value) za "state" odnosno stanje na tabli

    Nacin bodovanja:
        Dama - 10
        Obicna figura - 5
        Figura na protivnickoj polovini table - 7
        Figura u cosku - +2

    Bodovi se dele brojem protivnickih figura
    """

    board = state.board
    turn = state.turn
    black, white = 0, 0
    b_counter = 0
    w_counter = 0
    angle_positions = [0, 1, 3, 5, 57, 59, 61, 63, 48, 32, 16, 47, 31, 15]

    for i in range(64):
        if board[i] == 'b':
            black += 1
        elif board[i] == 'B':
            black += 1.5
        elif board[i] == 'w':
            white += 1
        elif board[i] == 'W':
            white += 1.5

        # if board[i] == "B":
        #     if i in angle_positions:
        #         black = black + 2
        #     black = black + 10
        #     b_counter += 1
        # if board[i] == "b" and i > 3:
        #     if i in angle_positions:
        #         black = black + 2
        #     black = black + 7
        #     b_counter += 1
        # if board[i] == "b" and i <= 3:
        #     if i in angle_positions:
        #         black = black + 2
        #     black = black + 5
        #     b_counter += 1
        #
        # if board[i] == "W":
        #     if i in angle_positions:
        #          white = white + 2
        #     white = white + 10
        #     w_counter += 1
        # if board[i] == "w" and i < 3:
        #     if i in angle_positions:
        #         white = white + 2
        #     white = white + 7
        #     w_counter += 1
        # if board[i] == "w" and i >= 3:
        #     if i in angle_positions:
        #         white = white + 2
        #     white = white + 5
        #     w_counter += 1

    # black = black / w_counter
    # white = white / b_counter
    return black - white if turn == Turn.BLACK else white - black

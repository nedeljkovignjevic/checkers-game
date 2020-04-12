from src.board import init_board, print_board, game_over
from src.evaluation import alpha_beta
from src.state import State, Turn


def game_loop():
    """
    Checkers console game loop
    """

    board = init_board()
    print_board(board)
    print()

    while True:

        if game_over(board):
            break

        while True:
            coordinates_input = input("\nPlayer 1 input coordinates (what to move and where eg. 16 25): ")
            move = validate_move(coordinates_input, board)
            if move is not None:
                play_move(board, move, Turn.WHITE)
                print_board(board)
                break

        computer_move(board, Turn.BLACK)


def self_play():
    """
    AI vs AI loop
    """

    board = init_board()
    print_board(board)
    print()

    while True:

        if game_over(board):
            break

        computer_move(board, Turn.WHITE)
        computer_move(board, Turn.BLACK)


def computer_move(board: list, turn: Turn):
    """
    Play the computer move
    """

    state = State(board, turn, [])
    print(f"\n{str(turn)} thinking...")
    move = move_function(state)
    jump_move = play_move(board, move, turn)
    print(move)
    print_board(board)
    while jump_move is not None:
        temp = board
        state = State(board, turn, [])
        move = move_function(state)
        jump_move = play_move(board, move, turn)
        if jump_move is None:
            board = temp
        else:
            print(move)
            print_board(board)


def move_function(state: State):
    """
    Return best computer move
    """

    best_move = None
    val = -10000
    depth = 5
    for state in state.get_states():
        score = alpha_beta(state, depth, -10000, 10000, True)
        if score > val:
            val, best_move = score, state.move

    return best_move


def play_move(board: list, move: list, turn: Turn):
    """
    Update values on board
    """

    piece = board[move[0]]
    board[move[0]] = '-'

    if turn == turn.BLACK:
        board[move[1]] = piece if move[1] > 8 else piece.upper()
    elif turn == turn.WHITE:
        board[move[1]] = piece if move[1] < 56 else piece.upper()

    if abs(move[0] - move[1]) > 9:
        x = move[1] - move[0]
        mid_i = move[0] + int(x / 2)
        board[mid_i] = '-'
        return mid_i

    return None


def validate_move(coordinates_input: str, board: list):
    # noinspection PyBroadException
    try:
        tokens = coordinates_input.split()
        src, dest = int(tokens[0]), int(tokens[1])
    except Exception:
        return None

    move = [src, dest]
    state = State(board, Turn.WHITE, [])
    legal_moves = [el.move for el in state.get_states()]
    print(f'Available moves: {legal_moves}')
    if move in legal_moves:
        return move
    else:
        return None

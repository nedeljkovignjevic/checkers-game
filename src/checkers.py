from src.board import init_board, print_board, game_over
from src.alpha_beta import alpha_beta
from src.state import State, Turn
from time import time


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

    if turn.BLACK:
        board[move[1]] = piece if move[1] < 56 else piece.upper()
    if turn.WHITE:
        board[move[1]] = piece if move[1] > 7 else piece.upper()

    if abs(move[0] - move[1]) > 9:
        x = move[1] - move[0]
        mid_i = move[0] + int(x/2)
        board[mid_i] = '-'
        return mid_i

    return None


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

        coordinates_input = input("\nPlayer 1 input coordinates (what to move and where eg. 16 25): ")
        token = coordinates_input.split()
        src, dest = int(token[0]), int(token[1])
        play_move(board, [src, dest], Turn.WHITE)
        print_board(board)

        state = State(board, Turn.BLACK, [])

        print("\nThinking...")
        start = time()
        move = move_function(state)
        play_move(board, move, Turn.BLACK)
        print(time() - start)
        print(move)
        print_board(board)


# def valid_move(coordinates_input: str, board: dict):
#     """
#     Check if the inputed player move is valid
#         Move valid -> play the move, return True
#         Move not valid -> return False
#     """
#
#     tokens = coordinates_input.split()
#     first, second = tokens[0].split('-'), tokens[1].split('-')
#     sx, sy, dx, dy = int(first[0]), int(first[1]), int(second[0]), int(second[1])
#     t_first, t_second = (sx, sy), (dx, dy)
#     move = [t_first, t_second]
#     state = State(board, Turn.WHITE, [])
#     gen_states = [s.move for s in state.get_states()]
#     if move in gen_states:
#         play_move(board, move, Turn.WHITE)
#         return True
#     else:
#         return False

from src.state import State, Turn
import chess


def init_board():
    """
    Initialize checkers board (8x8)
    """

    board = ['w', '-', 'w', '-', 'w', '-', 'w', '-',
             '-', 'w', '-', 'w', '-', 'w', '-', 'w',
             'w', '-', 'w', '-', 'w', '-', 'w', '-',
             '-', '-', '-', '-', '-', '-', '-', '-',
             '-', '-', '-', '-', '-', '-', '-', '-',
             '-', 'b', '-', 'b', '-', 'b', '-', 'b',
             'b', '-', 'b', '-', 'b', '-', 'b', '-',
             '-', 'b', '-', 'b', '-', 'b', '-', 'b']

    return board


def print_board(board):
    for i in range(56, -1, -8):
        for j in range(8):
            print(board[i+j], end=' ')
        print()


def game_over(board):
    """
    1: num_pieces >=4
    2: num_pieces = 1 -> 1 wins
    """

    b_counter = 0
    w_counter = 0
    for i in range(64):
        if board[i] == "b" or board[i] == "B":
            b_counter += 1
        elif board[i] == "w" or [i] == "W":
            w_counter += 1

    state = State(board, Turn.WHITE, [])

    if w_counter == 0 or (b_counter > 3 and w_counter < 2) or len(state.get_states()) == 0:
        print("GAME OVER! You lost!")
        return True

    if b_counter == 0 or (w_counter > 3 and b_counter < 2):
        print("CONGRATS! You won!")
        return True

    return False


def init_gui_board(board):
    board.set_piece_at(chess.B8, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.D8, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.F8, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.H8, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.A7, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.C7, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.E7, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.G7, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.B6, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.D6, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.F6, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.H6, chess.Piece.from_symbol('k'), chess.KING)

    board.set_piece_at(chess.A3, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.C3, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.E3, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.G3, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.B2, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.D2, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.F2, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.H2, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.A1, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.C1, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.E1, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.G1, chess.Piece.from_symbol('K'), chess.KING)
    return board

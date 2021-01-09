from board import Board
from utils import assert_every, str_to_int_list


class TicTacToe:
    def __init__(self):
        self.board: Board = Board()
        self.play()

    coordinates: list[int]
    player = 'X'

    def switch_player(self):
        self.player = 'O' if self.player == 'X' else 'X'

    def to_index(self) -> int:
        [y, x] = self.coordinates  # vertical-first
        return (y - 1) * 3 + x - 1

    def are_all_in_range(self):
        if not assert_every(self.coordinates, lambda c: 0 < c <= 3):
            raise AssertionError

    def input_safely(self) -> int:
        user_coordinates = input("Enter the coordinates:")
        self.coordinates = str_to_int_list(user_coordinates)
        self.are_all_in_range()
        return self.to_index()

    def play(self):
        try:
            move = self.input_safely()
            self.board.update(move, self.player)
            self.switch_player()
        except ValueError:
            print('You should enter numbers!')
        except AssertionError:
            print('Coordinates should be from 1 to 3!')
        except LookupError:
            print('This cell is occupied! Choose another one!')
        finally:
            if self.board.is_finished():
                self.board.set_game_result()
            else:
                self.play()


TicTacToe()
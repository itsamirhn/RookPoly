import unittest
from rookpoly import Board
from rookpoly import Polynomial


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.empty_square_boards = [Board(['0' * i for _ in range(i)]) for i in range(6)]
        self.board_1 = Board(["110", "100", "000", "001"])
        self.board_2 = Board(["00111", "00111", "11100", "11100", "11000"])

    def test_rotate(self):
        for (i, board) in enumerate(self.empty_square_boards):
            board.rotate()
            self.assertEqual(board, ['0' * i for _ in range(i)])

        self.board_1.rotate()
        self.assertEqual(self.board_1, ["0011", "0001", "1000"])

    def test_rtrim(self):
        for (i, board) in enumerate(self.empty_square_boards):
            board.rtrim()
            self.assertEqual(board, ['0' * i for _ in range(i)])

        self.board_1.rtrim()
        self.assertEqual(self.board_1, ["110", "100", "000", "001"])

        self.board_2.rtrim()
        self.assertEqual(self.board_2, ["00111", "00111", "11100", "11100", "11000"])

    def test_simplify(self):
        for (i, board) in enumerate(self.empty_square_boards):
            board.simplify()
            self.assertEqual(board, ['0' * i for _ in range(i)])

        self.board_1.simplify()
        self.assertEqual(self.board_1, ["110", "100", "000", "001"])

        self.board_2.simplify()
        self.assertEqual(self.board_2, ["00111", "00111", "11100", "11100", "11000"])

    def test_get_sub_board(self):
        self.assertEqual(self.board_1.get_sub_board(2, 0, 4, 3), ["000", "001"])

    def test_get_poly(self):
        self.assertEqual(self.empty_square_boards[0].get_poly(), Polynomial(1))
        self.assertEqual(self.empty_square_boards[1].get_poly(), Polynomial(1, 1))
        self.assertEqual(self.empty_square_boards[2].get_poly(), Polynomial(1, 4, 2))
        self.assertEqual(self.empty_square_boards[3].get_poly(), Polynomial(1, 9, 18, 6))
        self.assertEqual(self.empty_square_boards[4].get_poly(), Polynomial(1, 16, 72, 96, 24))
        self.assertEqual(self.empty_square_boards[5].get_poly(), Polynomial(1, 25, 200, 600, 600, 120))
        self.assertEqual(self.board_1.get_poly(), Polynomial(1, 8, 16, 7))
        self.assertEqual(self.board_2.get_poly(), Polynomial(1, 11, 40, 56, 28, 4))


if __name__ == '__main__':
    unittest.main()

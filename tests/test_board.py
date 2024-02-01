import unittest

from rookpoly import Board
from rookpoly.polynomial import Polynomial


class TestBoard(unittest.TestCase):
    empty_boards_limit = 7

    def setUp(self):
        self.empty_boards = [Board(['0' * i for _ in range(i)]) for i in range(self.empty_boards_limit)]
        self.board_1 = Board(["110", "100", "000", "001"])
        self.board_2 = Board(["00111", "00111", "11100", "11100", "11000"])

    def test_init(self):
        # Testing proper board initialization
        board = Board(["100", "010"])
        self.assertEqual(board.n, 2)
        self.assertEqual(board.m, 3)

    def test_n(self):
        # Testing the n property, which returns the number of rows
        self.assertEqual(self.board_1.n, 4)
        self.assertEqual(self.board_2.n, 5)

    def test_m(self):
        # Testing the m property, which returns the number of columns
        self.assertEqual(self.board_1.m, 3)
        self.assertEqual(self.board_2.m, 5)

    def test_is_empty(self):
        # Testing if the board is identified as empty correctly
        empty_board = Board([])
        self.assertTrue(empty_board.is_empty())

        non_empty_board = Board(["100", "000"])
        self.assertFalse(non_empty_board.is_empty())

    # Test for get method
    def test_get(self):
        # Testing retrieving value from the board
        self.assertEqual(self.board_1.get(0, 0), '1')
        self.assertEqual(self.board_1.get(1, 1), '0')

    # Test for set method
    def test_set(self):
        # Testing setting value on the board
        self.board_1.set(0, 0, '0')
        self.assertEqual(self.board_1.get(0, 0), '0')

        self.board_1.set(1, 1, '1')
        self.assertEqual(self.board_1.get(1, 1), '1')

    def test_flip(self):
        # Testing flipping the board
        board = Board(["100", "010", "001"])
        board.flip()
        self.assertEqual(board, Board(["001", "010", "100"]))

    def test_rotate(self):
        # Testing board rotation
        for (i, board) in enumerate(self.empty_boards):
            board.rotate()
            self.assertEqual(board, ['0' * i for _ in range(i)])

        self.board_1.rotate()
        self.assertEqual(self.board_1, ["0011", "0001", "1000"])

        self.board_2.rotate()
        self.assertEqual(self.board_2, ["11100", "11100", "01111", "00011", "00011"])

    def test_rtrim(self):
        # Testing trimming empty spaces on the right side of the board
        for (i, board) in enumerate(self.empty_boards):
            board.rtrim()
            self.assertEqual(board, ['0' * i for _ in range(i)])

        self.board_1.rtrim()
        self.assertEqual(self.board_1, ["110", "100", "000", "001"])

        self.board_2.rtrim()
        self.assertEqual(self.board_2, ["00111", "00111", "11100", "11100", "11000"])

    def test_remove_filled_rows(self):
        # Testing removing filled rows from the board
        board = Board(["111", "000", "010"])
        board.remove_filled_rows()
        self.assertEqual(board, Board(["000", "010"]))

    def test_simplify(self):
        # Testing simplifying the board
        for (i, board) in enumerate(self.empty_boards):
            board.simplify()
            self.assertEqual(board, ['0' * i for _ in range(i)])

        self.board_1.simplify()
        self.assertEqual(self.board_1, ["0011", "0001", "1000"])

        self.board_2.simplify()
        self.assertEqual(self.board_2, ["00111", "00111", "11100", "11100", "11000"])

    def test_get_empty_squares(self):
        # Testing identifying empty squares on the board
        board = Board(["100", "001", "010"])
        empty_squares = list(board.get_empty_squares())
        self.assertEqual(empty_squares, [(0, 1), (0, 2), (1, 0), (1, 1), (2, 0), (2, 2)])

    def test_get_set(self):
        # Testing reading and writing values in specific board cells
        board = Board(["010", "001", "100"])

        # Set new values and check if they are correctly updated
        board.set(0, 0, '1')
        board.set(1, 1, '0')
        board.set(2, 2, '1')

        self.assertEqual(board.get(0, 0), '1')
        self.assertEqual(board.get(1, 1), '0')
        self.assertEqual(board.get(2, 2), '1')

        # Ensure a cell that wasn't set remains unchanged
        self.assertEqual(board.get(0, 1), '1')

    def test_is_valid_cut_column(self):
        # Testing if a column can be cut
        board = Board(["1001", "1111", "1001"])
        self.assertTrue(board.is_valid_cut_column(1))
        self.assertFalse(board.is_valid_cut_column(2))

    def test_get_cuttable_columns(self):
        # Testing identifying columns that can be cut
        board = Board(["1001", "1111", "1001"])
        cuttable_columns = list(board.get_cuttable_columns())
        self.assertEqual(cuttable_columns, [1, 3])

    def test_cut_columns(self):
        # Testing cutting columns from the board
        board = Board(["100", "110", "100"])
        sub_boards = list(board.cut_columns())
        self.assertEqual(len(sub_boards), 2)
        self.assertEqual(sub_boards[0], Board(["1", "1", "1"]))
        self.assertEqual(sub_boards[1], Board(["00", "10", "00"]))

    def test_get_sub_board(self):
        # Testing getting a sub-board
        self.assertEqual(self.board_1.get_sub_board(2, 0, 4, 3), ["000", "001"])

    def test_get_poly(self):
        # Testing generating a polynomial based on the board
        self.assertEqual(self.empty_boards[0].get_poly(), Polynomial(1))
        self.assertEqual(self.empty_boards[1].get_poly(), Polynomial(1, 1))
        self.assertEqual(self.empty_boards[2].get_poly(), Polynomial(1, 4, 2))
        self.assertEqual(self.empty_boards[3].get_poly(), Polynomial(1, 9, 18, 6))
        self.assertEqual(self.empty_boards[4].get_poly(), Polynomial(1, 16, 72, 96, 24))
        self.assertEqual(self.empty_boards[5].get_poly(), Polynomial(1, 25, 200, 600, 600, 120))
        self.assertEqual(self.empty_boards[6].get_poly(), Polynomial(1, 36, 450, 2400, 5400, 4320, 720))
        self.assertEqual(self.board_1.get_poly(), Polynomial(1, 8, 16, 7))
        self.assertEqual(self.board_2.get_poly(), Polynomial(1, 11, 40, 56, 28, 4))

    def test_eq(self):
        # Testing comparing two boards
        board_1 = Board(["100", "010", "001"])
        board_2 = Board(["100", "010", "001"])
        board_3 = Board(["101", "010", "001"])
        self.assertTrue(board_1 == board_2)
        self.assertFalse(board_1 == board_3)

    def test_repr(self):
        # Testing the __repr__ method for object representation
        board = Board(["100", "010", "001"])
        self.assertEqual(repr(board), "[['1', '0', '0'], ['0', '1', '0'], ['0', '0', '1']]")

    def test_str(self):
        # Testing the __str__ method for string representation
        board = Board(["100", "010", "001"])
        self.assertEqual(str(board), "100\n010\n001")


if __name__ == '__main__':
    unittest.main()

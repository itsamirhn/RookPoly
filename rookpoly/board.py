import collections.abc
import random

from rookpoly.polynomial import Polynomial


class Board:

    def __init__(self, board):
        self.rotated_times = 0
        self.board = [list(row) for row in board]

    @property
    def n(self):
        return len(self.board)

    @property
    def m(self):
        if self.n == 0:
            return 0
        return len(self.board[0])

    def flip(self):
        self.board = [list(reversed(row)) for row in self.board]

    def rotate(self):
        self.rotated_times = (self.rotated_times + 1) % 4
        self.board = [list(r) for r in zip(*self.board[::-1])]

    def rtrim(self):
        if self.is_empty():
            return
        self.board = [list(''.join(row).rstrip('1')) for row in self.board]
        mx = max([len(row) for row in self.board])
        self.board = [row + list('1' * (mx - len(row))) for row in self.board]

    def remove_filled_rows(self):
        self.board = [row for row in self.board if len(''.join(row).rstrip('1')) > 0]

    def simplify(self):
        for i in range(4):
            self.rtrim()
            self.rotate()
        for i in range(4):
            self.remove_filled_rows()
            self.rotate()
        if self.n > self.m:
            self.rotate()

    def get_empty_squares(self):
        for (row, i) in enumerate(self.board):
            for (column, j) in enumerate(i):
                if j == '0':
                    yield row, column

    def get(self, i, j):
        return self.board[i][j]

    def is_valid_cut_column(self, j):
        for row in self.board:
            l, r = row[:j], row[j:]
            if '0' in l and '0' in r:
                return False
        return True

    def get_sub_board(self, x, y, z, w):
        return Board([row[y:w] for row in self.board[x:z]])

    def fill_row_and_column(self, i, j):
        for k in range(len(self.board)):
            self.board[k][j] = '1'
        for k in range(len(self.board[i])):
            self.board[i][k] = '1'

    def is_empty(self):
        return self.n == 0 or self.m == 0

    def set(self, i, j, value):
        self.board[i][j] = value

    def get_cuttable_columns(self):
        for i in range(1, self.m):
            if self.is_valid_cut_column(i):
                yield i

    def cut_columns(self):
        last = 0
        for j in self.get_cuttable_columns():
            yield self.get_sub_board(0, last, self.n, j)
            last = j
        yield self.get_sub_board(0, last, self.n, self.m)

    def get_poly(self):
        self.simplify()
        if self.is_empty():
            return Polynomial(1)

        sub_boards = list(self.cut_columns())
        if len(sub_boards) > 1:
            poly = Polynomial(1)
            for sub_board in sub_boards:
                poly *= sub_board.get_poly()
            return poly

        x, y = random.choice(list(self.get_empty_squares()))
        s, e = Board(self.board), Board(self.board)
        s.set(x, y, '1')
        e.fill_row_and_column(x, y)

        return Polynomial(0, 1) * e.get_poly() + s.get_poly()

    def __eq__(self, other):
        if isinstance(other, Board):
            return self.board == other.board
        if isinstance(other, collections.abc.Iterable):
            return self.board == [list(row) for row in other]
        return False

    def __repr__(self):
        return self.board.__repr__()

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.board])

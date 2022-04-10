import collections.abc
import random

from rookpoly.polynomial import Polynomial


class Board:

    def __init__(self, board):
        self.rotated_times = 0
        self.board = board[:]

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

    def get_empty_squares(self):
        for (row, i) in enumerate(self.board):
            for (column, j) in enumerate(i):
                if j == '0':
                    yield row, column

    def get(self, i, j):
        return self.board[i][j]

    def is_valid_cut_row(self, i):
        for j in range(len(self.board[0])):
            u, d = [row[j] for row in self.board[:i]], [row[j] for row in self.board[i:]]
            if '0' in u and '0' in d:
                return False
        return True

    def is_valid_cut_column(self, j):
        for row in self.board:
            l, r = row[:j], row[j:]
            if '0' in l and '0' in r:
                return False
        return True

    def get_sub_board(self, x, y, z, w):
        return Board([row[y:w] for row in self.board[x:z]])

    def cut_row(self, i):
        return self.get_sub_board(0, 0, i, len(self.board[i])), self.get_sub_board(i, 0, len(self.board), len(self.board[i]))

    def cut_column(self, j):
        return self.get_sub_board(0, 0, len(self.board), j), self.get_sub_board(0, j, len(self.board), len(self.board[0]))

    def fill_row_and_column(self, i, j):
        for k in range(len(self.board)):
            self.board[k][j] = '1'
        for k in range(len(self.board[i])):
            self.board[i][k] = '1'

    def is_empty(self):
        if len(self.board) == 0:
            return True
        if len(self.board[0]) == 0:
            return True
        return False

    def set(self, i, j, value):
        self.board[i][j] = value
        self.simplify()

    def get_cuttable_rows(self):
        for i in range(1, len(self.board)):
            if self.is_valid_cut_row(i):
                yield i

    def get_cuttable_columns(self):
        for i in range(1, len(self.board[0])):
            if self.is_valid_cut_column(i):
                yield i

    def get_efficient_row_cut(self):
        best_minimum_count = None
        best_row = None
        for i in self.get_cuttable_rows():
            u, d = self.cut_row(i)
            count = len(list(u.get_empty_squares())) + len(list(d.get_empty_squares()))
            if best_row is None or count < best_minimum_count:
                best_minimum_count = count
                best_row = i
        return best_row, best_minimum_count

    def get_efficient_column_cut(self):
        best_minimum_count = None
        best_column = None
        for i in self.get_cuttable_columns():
            l, r = self.cut_column(i)
            count = len(list(l.get_empty_squares())) + len(list(r.get_empty_squares()))
            if best_column is None or count < best_minimum_count:
                best_minimum_count = count
                best_column = i
        return best_column, best_minimum_count

    def get_most_efficient_cut(self):
        best_row, row_value = self.get_efficient_row_cut()
        best_column, column_value = self.get_efficient_column_cut()
        n = len(self.board)
        m = len(self.board[0])
        if best_column is None:
            return 'R', best_row
        if best_row is None:
            return 'C', best_column
        if row_value < column_value:
            return 'R', best_row
        return 'C', best_column

    def get_poly(self):
        self.simplify()
        if self.is_empty():
            return Polynomial(1)

        dir, cut = self.get_most_efficient_cut()
        if dir == 'R' and cut is not None:
            u, d = self.cut_row(cut)
            return u.get_poly() * d.get_poly()
        elif dir == 'C' and cut is not None:
            l, r = self.cut_column(cut)
            return l.get_poly() * r.get_poly()
        else:
            x, y = random.choice(list(self.get_empty_squares()))
            s, e = Board(self.board), Board(self.board)
            s.set(x, y, '1')
            e.fill_row_and_column(x, y)

            return Polynomial(0, 1) * e.get_poly() + s.get_poly()

    def get_str_board(self):
        return [''.join(row) for row in self.board]

    def __eq__(self, other):
        if isinstance(other, Board):
            return self.board == other.board
        if isinstance(other, collections.abc.Iterable):
            return self.board == [list(row) for row in other]
        return False

    def __str__(self):
        return 'Board:\n' + '\n'.join(self.get_str_board())

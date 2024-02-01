import collections.abc
import random

from rookpoly.polynomial import Polynomial


class Board:

    def __init__(self, board):
        """Initialize the Board with a given board layout."""
        self.rotated_times = 0
        self.board = [list(row) for row in board]

    @property
    def n(self):
        """Return the number of rows in the board."""
        return len(self.board)

    @property
    def m(self):
        """Return the number of columns in the board."""
        if self.n == 0:
            return 0
        return len(self.board[0])

    def is_empty(self):
        """Check if the board is empty."""
        return self.n == 0 or self.m == 0

    def get(self, i, j):
        """Get the value at the specified position on the board."""
        return self.board[i][j]

    def set(self, i, j, value):
        """Set the value at the specified position on the board."""
        self.board[i][j] = value

    def flip(self):
        """Flip the board horizontally."""
        self.board = [list(reversed(row)) for row in self.board]

    def rotate(self):
        """Rotate the board 90 degrees clockwise."""
        self.rotated_times = (self.rotated_times + 1) % 4
        self.board = [list(r) for r in zip(*self.board[::-1])]

    def rtrim(self):
        """Trim empty spaces from the right side of the board."""
        if self.is_empty():
            return
        self.board = [list(''.join(row).rstrip('1')) for row in self.board]
        mx = max(len(row) for row in self.board)
        self.board = [row + list('1' * (mx - len(row))) for row in self.board]

    def remove_filled_rows(self):
        """Remove rows that are completely filled."""
        self.board = [row for row in self.board if len(''.join(row).rstrip('1')) > 0]

    def simplify(self):
        """Simplify the board by trimming and removing filled rows."""
        for _ in range(4):
            self.rtrim()
            self.rotate()
        for _ in range(4):
            self.remove_filled_rows()
            self.rotate()
        if self.n > self.m:
            self.rotate()

    def get_empty_squares(self):
        """Yield the positions of empty squares on the board."""
        for row_idx, row in enumerate(self.board):
            for col_idx, val in enumerate(row):
                if val == '0':
                    yield row_idx, col_idx

    def is_valid_cut_column(self, j):
        """Check if a column can be cut without dividing empty squares."""
        for row in self.board:
            l, r = row[:j], row[j:]
            if '0' in l and '0' in r:
                return False
        return True

    def get_sub_board(self, x, y, z, w):
        """Get a sub-board from the current board."""
        return Board([row[y:w] for row in self.board[x:z]])

    def fill_row_and_column(self, i, j):
        """Fill the specified row and column with '1's."""
        for k in range(self.n):
            self.board[k][j] = '1'
        for k in range(self.m):
            self.board[i][k] = '1'

    def get_cuttable_columns(self):
        """Yield indices of columns that can be cut."""
        for i in range(1, self.m):
            if self.is_valid_cut_column(i):
                yield i

    def cut_columns(self):
        """Yield sub-boards created by cutting the board along cuttable columns."""
        last = 0
        for j in self.get_cuttable_columns():
            yield self.get_sub_board(0, last, self.n, j)
            last = j
        yield self.get_sub_board(0, last, self.n, self.m)

    def get_poly(self):
        """Get the polynomial representation of the board."""
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
        """Check if two boards are equal."""
        if isinstance(other, Board):
            return self.board == other.board
        if isinstance(other, collections.abc.Iterable):
            return self.board == [list(row) for row in other]
        return False

    def __repr__(self):
        """Return a string representation of the board for debugging."""
        return self.board.__repr__()

    def __str__(self):
        """Return a string representation of the board for display."""
        return '\n'.join(''.join(row) for row in self.board)

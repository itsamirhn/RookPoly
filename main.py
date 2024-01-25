import time

from rookpoly import Board


def main():
    n = int(input("Enter number of rows: "))
    board = []
    for i in range(n):
        board.append(input().rstrip())
    board = Board(board)
    print("Calculating...")
    start = time.time()
    print(board.get_poly())
    end = time.time()
    print("Time: ", end - start)


if __name__ == '__main__':
    main()

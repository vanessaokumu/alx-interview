#!/usr/bin/python3
"""
0-nqueens.py
Solves the N Queens puzzle.
Usage: ./0-nqueens.py N
"""
import sys


def is_valid(board, row, col):
    """Check if placing a queen at (row, col) is valid."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """Solve the N Queens problem using backtracking."""
    def backtrack(row, board):
        if row == N:
            solutions.append([[i, board[i]] for i in range(N)])
        else:
            for col in range(N):
                if is_valid(board, row, col):
                    board[row] = col
                    backtrack(row + 1, board)
                    board[row] = -1

    solutions = []
    board = [-1] * N
    backtrack(0, board)
    return solutions


def main():
    # Validate command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N Queens problem and print solutions
    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()

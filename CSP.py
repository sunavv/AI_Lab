def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def solve_n_queens(n, row=0, board=[]):
    if row == n:
        print(board)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board.append(col)
            solve_n_queens(n, row + 1, board)
            board.pop()

solve_n_queens(4)

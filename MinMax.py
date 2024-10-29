import math

def minimax(board, depth, is_maximizing):
    scores = {'X': 1, 'O': -1, 'Tie': 0}
    
    result = check_winner(board)
    if result:
        return scores[result]

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def check_winner(board):
    win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6)]
    for (x, y, z) in win_patterns:
        if board[x] == board[y] == board[z] and board[x] != " ":
            return board[x]
    if " " not in board:
        return "Tie"
    return None

import random

def count_attacks(board):
    attacks = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j]:
                attacks += 1
            if abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    return attacks

def hill_climbing(n):
    board = []
    for i in range(n):
        board.append(random.randint(0, n - 1))

    while True:
        current_attacks = count_attacks(board)
        if current_attacks == 0:
            return board

        best_board = board
        best_attacks = current_attacks

        for row in range(n):
            for col in range(n):
                if col != board[row]:
                    temp = board.copy()
                    temp[row] = col
                    attacks = count_attacks(temp)

                    if attacks < best_attacks:
                        best_attacks = attacks
                        best_board = temp

        if best_attacks == current_attacks:
            return None

        board = best_board


n = 8
result = hill_climbing(n)

if result is None:
    print("No solution found")
else:
    print("Solution:", result)

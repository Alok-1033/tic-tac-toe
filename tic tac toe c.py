def printboard(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
            if j < 2:
                print('|', end=' ')
        print()
        if i < 2:
            print("--+---+--")

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def restart_game():
    return [[' ' for _ in range(3)] for _ in range(3)]

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    while True:
        board = restart_game()
        player = 'X'
        game_over = False

        while not game_over:
            printboard(board)
            move = input(f"Player {player}, enter your move (row column): ").split()
            if len(move) != 2 or not move[0].isdigit() or not move[1].isdigit():
                print("Invalid input! Please enter row and column numbers.")
                continue
            row, col = map(int, move)
            if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != ' ':
                print("Invalid move! Please select an empty cell.")
                continue

            board[row][col] = player
            if check_win(board, player):
                printboard(board)
                print(f"Player {player} wins!")
                game_over = True
            elif check_draw(board):
                printboard(board)
                print("It's a draw!")
                game_over = True
            else:
                player = 'O' if player == 'X' else 'X'

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

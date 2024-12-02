def tic_tac_toe():
    board = [' ' for _ in range(9)]
    current_player = 'X'

    def print_board():
        print(f" {board[0]} | {board[1]} | {board[2]} ")
        print("---+---+---")
        print(f" {board[3]} | {board[4]} | {board[5]} ")
        print("---+---+---")
        print(f" {board[6]} | {board[7]} | {board[8]} ")

    def check_win(player):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                          (0, 4, 8), (2, 4, 6)]  # Diagonals
        for condition in win_conditions:
            if all(board[i] == player for i in condition):
                return True
        return False

    def is_board_full():
        return ' ' not in board

    while True:
        print_board()
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

        if board[move] == ' ':
            board[move] = current_player

            if check_win(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                break

            if is_board_full():
                print_board()
                print("It's a draw!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That space is already taken. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
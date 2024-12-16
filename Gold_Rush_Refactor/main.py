from game import GoldRush
from Matrix import Matrix


def play_game():
    print("Welcome to Gold Rush!")
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    players = ["player1", "player2"]
    matrix = Matrix(rows,cols)
    game = GoldRush(rows, cols,players)
    game.load_board()
    game.print()

    while not game.win:
        for player in players:
            direction = input(f"{player}, enter your move (up, down, left, right): ").strip().lower()
            game.move_player(player, direction)
            game.print()
            if game._check_win(player):
                print(f"{player} wins!")
                break

if __name__ == "__main__":
    play_game()


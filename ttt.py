# tic_tac_toe.py
# Object-Oriented Tic-Tac-Toe with Score Tracking and Replay Loop

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

class EnhancedPlayer(Player):
    def __init__(self, name, symbol):
        super().__init__(name, symbol)
        self.wins = 0

    def add_win(self):
        self.wins += 1
        print(f"{self.name} now has {self.wins} wins!")

class Board:
    def __init__(self):
        self.grid = [" "] * 9
        self.move_count = 0

    def display(self):
        print(f"\n {self.grid[0]} | {self.grid[1]} | {self.grid[2]}")
        print("---+---+---")
        print(f" {self.grid[3]} | {self.grid[4]} | {self.grid[5]}")
        print("---+---+---")
        print(f" {self.grid[6]} | {self.grid[7]} | {self.grid[8]}\n")

    def display_reference(self):
        reference = [str(i) for i in range(1, 10)]
        print("Board positions:")
        print(f" {reference[0]} | {reference[1]} | {reference[2]}")
        print("---+---+---")
        print(f" {reference[3]} | {reference[4]} | {reference[5]}")
        print("---+---+---")
        print(f" {reference[6]} | {reference[7]} | {reference[8]}\n")

    def reset(self):
        self.grid = [" "] * 9
        self.move_count = 0

    def is_full(self):
        return " " not in self.grid

    def make_move(self, position, symbol):
        index = position - 1
        if index < 0 or index > 8:
            print("Invalid position. Choose 1–9.")
            return False
        if self.grid[index] != " ":
            print("Spot already taken. Try again.")
            return False
        self.grid[index] = symbol
        self.move_count += 1
        return True

    def check_winner(self, symbol):
        win_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        return any(
            all(self.grid[i] == symbol for i in combo)
            for combo in win_combos
        )

class TicTacToe:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_player = player1

    def switch_player(self):
        self.current_player = (
            self.players[1] if self.current_player == self.players[0]
            else self.players[0]
        )

    def play_game(self):
        self.board.reset()
        self.board.display_reference()

        while True:
            print(f"{self.current_player.name}'s turn ({self.current_player.symbol})")
            try:
                pos = int(input("Choose position (1-9): "))
            except ValueError:
                print("Enter a number!")
                continue

            if self.board.make_move(pos, self.current_player.symbol):
                self.board.display()
                if self.board.check_winner(self.current_player.symbol):
                    print(f"🎉 {self.current_player.name} wins!")
                    if isinstance(self.current_player, EnhancedPlayer):
                        self.current_player.add_win()
                    break
                if self.board.is_full():
                    print("It's a tie!")
                    break
                self.switch_player()

def main():
    print("Welcome to Tic-Tac-Toe!\n")
    player1 = EnhancedPlayer("Alice", "X")
    player2 = EnhancedPlayer("Bob", "O")
    game = TicTacToe(player1, player2)

    while True:
        game.play_game()
        print(f"Score: {player1.name} ({player1.wins}) - {player2.name} ({player2.wins})")
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
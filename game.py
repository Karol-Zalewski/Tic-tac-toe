from player import ComputerPlayer, HumanPlayer


class Tic_Tac_Toe:
    def __init__(self):
        self.board = [
            [
                "_"
                for _ in range(3)
            ]
            for _ in range(3)
        ]
        self.winner = None

    def __str__(self):
        text = ' '
        for col in range(3):
            text += f" {col} "
        for row in range(3):
            text += f"\n{row}"
            for col in range(3):
                text += f"|{self.board[row][col]}|"
        return text

    def get_possible_moves(self):
        possible_moves = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '_':
                    possible_moves.append((row, col))
        return possible_moves

    def make_move(self, letter, row, col):
        self.board[row][col] = letter
        if self.win_if(letter, row, col):
            self.winner = letter

    def win_if(self, letter, row, col):
        if all(self.board[row][c] == letter for c in range(3)):
            return True

        if all(self.board[r][col] == letter for r in range(3)):
            return True

        dia_1 = [(0, 0), (1, 1), (2, 2)]
        dia_2 = [(0, 2), (1, 1), (2, 0)]

        if (row, col) in dia_1:
            if all(self.board[r][c] == letter for (r, c) in dia_1):
                return True

        if (row, col) in dia_2:
            if all(self.board[r][c] == letter for (r, c) in dia_2):
                return True

        return False


if __name__ == "__main__":
    game = Tic_Tac_Toe()
    player_x = HumanPlayer('X')
    player_o = ComputerPlayer('O')
    letter = 'X'
    moves_made = 0
    while moves_made < 9:
        print(game)
        if letter == 'X':
            row, col = player_x.get_move(game.get_possible_moves())
        elif letter == 'O':
            row, col = player_o.get_move(game.get_possible_moves())

        game.make_move(letter, row, col)
        moves_made += 1

        if game.winner is not None:
            print(game)
            print(f"The player {game.winner} has won")
            break

        if letter == "X":
            letter = "O"
        else:
            letter = "X"

    if game.winner is None:
        print(game)
        print('Its a draw. ')

import random


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, possible_moves):
        row, col = None, None
        while True:
            print(f"Chose one of the free squares to put {self.letter} into.")
            try:
                row = int(input('Row: '))
                col = int(input('Col: '))
                if (row, col) not in possible_moves:
                    raise ValueError
            except ValueError:
                print("Wrong choice. Try again. ")
                continue
            print(f'Player {self.letter} has chosen square {row, col}')
            return row, col


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, possible_moves):
        row, col = random.choice(possible_moves)
        print(f'Player {self.letter} has chosen square {row, col}')
        return row, col

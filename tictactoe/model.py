class Board:
    def __init__(self):
        self.cells = [[None, None, None], [None, None, None], [None, None, None]]

    def make_move(self, row, col, player):
        if self.cells[row][col] is None:
            self.cells[row][col] = player
            return True
        return False

    def check_winner(self):
        # Проверка строк
        for row in range(3):
            if self.cells[row][0] == self.cells[row][1] == self.cells[row][2] and self.cells[row][0] is not None:
                return self.cells[row][0]

        # Проверка столбцов
        for col in range(3):
            if self.cells[0][col] == self.cells[1][col] == self.cells[2][col] and self.cells[0][col] is not None:
                return self.cells[0][col]

        # Проверка диагоналей
        if self.cells[0][0] == self.cells[1][1] == self.cells[2][2] and self.cells[0][0] is not None:
            return self.cells[0][0]
        if self.cells[0][2] == self.cells[1][1] == self.cells[2][0] and self.cells[0][2] is not None:
            return self.cells[0][2]

        return None

    def is_draw(self):
        for row in self.cells:
            for cell in row:
                if cell is None:
                    return False
        return True

    def reset(self):
        self.cells = [[None, None, None], [None, None, None], [None, None, None]]


class GameModel:
    def __init__(self):
        self.board = Board()
        self.current_player = "X"
        self.game_over = False
        self.winner = None

    def make_move(self, row, col):
        if self.game_over:
            return False

        if not self.board.make_move(row, col, self.current_player):
            return False

        self.winner = self.board.check_winner()
        if self.winner is not None:
            self.game_over = True
        elif self.board.is_draw():
            self.game_over = True
        else:
            self.current_player = "O" if self.current_player == "X" else "X"

        return True

    def reset_game(self):
        self.board.reset()
        self.current_player = "X"
        self.game_over = False
        self.winner = None

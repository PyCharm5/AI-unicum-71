from typing import List, Optional, Tuple


class Board:
    """Класс доски, отвечающий за хранение состояния игры"""

    def __init__(self):
        self.cells: List[List[Optional[str]]] = [[None for _ in range(3)] for _ in range(3)]

    def make_move(self, row: int, col: int, player: str) -> bool:
        """Сделать ход, возвращает True если ход был выполнен успешно"""
        if self.cells[row][col] is None:
            self.cells[row][col] = player
            return True
        return False

    def check_winner(self) -> Optional[str]:
        """Проверить есть ли победитель, возвращает символ победителя или None"""
        # Проверка строк и столбцов
        for i in range(3):
            if self.cells[i][0] == self.cells[i][1] == self.cells[i][2] is not None:
                return self.cells[i][0]
            if self.cells[0][i] == self.cells[1][i] == self.cells[2][i] is not None:
                return self.cells[0][i]

        # Проверка диагоналей
        if self.cells[0][0] == self.cells[1][1] == self.cells[2][2] is not None:
            return self.cells[0][0]
        if self.cells[0][2] == self.cells[1][1] == self.cells[2][0] is not None:
            return self.cells[0][2]

        return None

    def is_draw(self) -> bool:
        """Проверить закончилась ли игра в ничью"""
        return all(cell is not None for row in self.cells for cell in row)

    def reset(self) -> None:
        """Сбросить состояние доски"""
        self.cells = [[None for _ in range(3)] for _ in range(3)]


class GameModel:
    """Модель игры, управляющая состоянием и логикой"""

    def __init__(self):
        self.board = Board()
        self.current_player = "X"
        self.game_over = False
        self.winner = None

    def make_move(self, row: int, col: int) -> bool:
        """Попытаться сделать ход, возвращает True если ход был выполнен"""
        if self.game_over or not self.board.make_move(row, col, self.current_player):
            return False

        self.winner = self.board.check_winner()
        if self.winner is not None:
            self.game_over = True
        elif self.board.is_draw():
            self.game_over = True
        else:
            self.current_player = "O" if self.current_player == "X" else "X"

        return True

    def reset_game(self) -> None:
        """Сбросить игру в начальное состояние"""
        self.board.reset()
        self.current_player = "X"
        self.game_over = False
        self.winner = None

    def get_state(self) -> Tuple[List[List[Optional[str]]], str, bool, Optional[str]]:
        """Получить текущее состояние игры"""
        return (
            [row[:] for row in self.board.cells],
            self.current_player,
            self.game_over,
            self.winner
        )
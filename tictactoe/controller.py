from typing import Optional

from model import GameModel
from view import TicTacToeView


class TicTacToeController:
    """Контроллер, связывающий модель и представление"""

    def __init__(self, model: GameModel, view: TicTacToeView):
        self.model = model
        self.view = view

        # Устанавливаем обработчики событий
        self.view.set_cell_click_handler(self.handle_cell_click)
        self.view.set_restart_handler(self.handle_restart)

        # Первоначальное обновление представления
        self.update_view()

    def handle_cell_click(self, row: int, col: int) -> None:
        """Обработчик клика по клетке"""
        if self.model.make_move(row, col):
            self.update_view()

    def handle_restart(self) -> None:
        """Обработчик перезапуска игры"""
        self.model.reset_game()
        self.update_view()

    def update_view(self) -> None:
        """Обновить представление на основе текущего состояния модели"""
        board_state, current_player, game_over, winner = self.model.get_state()
        self.view.update_board(board_state)
        self.view.update_status(current_player, game_over, winner)
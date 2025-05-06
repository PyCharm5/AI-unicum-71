import tkinter as tk
from typing import Callable, List, Optional, Tuple


class TicTacToeView:
    """Класс представления игры, отвечающий за отображение GUI"""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Крестики-нолики")

        self.cell_click_handler: Optional[Callable[[int, int], None]] = None
        self.restart_handler: Optional[Callable[[], None]] = None

        self.create_widgets()

    def create_widgets(self) -> None:
        """Создать все виджеты интерфейса"""
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.root,
                    text="",
                    font=('Arial', 20),
                    width=5,
                    height=2,
                    command=lambda r=row, c=col: self.on_cell_click(r, c)
                )
                button.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row][col] = button

        self.status_label = tk.Label(
            self.root,
            text="Ход: X",
            font=('Arial', 14)
        )
        self.status_label.grid(row=3, column=0, columnspan=3, pady=10)

        self.restart_button = tk.Button(
            self.root,
            text="Начать заново",
            font=('Arial', 14),
            command=self.on_restart_click
        )
        self.restart_button.grid(row=4, column=0, columnspan=3, pady=10)

    def on_cell_click(self, row: int, col: int) -> None:
        """Обработчик клика по клетке"""
        if self.cell_click_handler:
            self.cell_click_handler(row, col)

    def on_restart_click(self) -> None:
        """Обработчик клика по кнопке перезапуска"""
        if self.restart_handler:
            self.restart_handler()

    def update_board(self, board_state: List[List[Optional[str]]]) -> None:
        """Обновить отображение доски"""
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(
                    text=board_state[row][col] if board_state[row][col] else "",
                    state="disabled" if board_state[row][col] else "normal"
                )

    def update_status(self, current_player: str, game_over: bool, winner: Optional[str]) -> None:
        """Обновить статус игры"""
        if game_over:
            if winner:
                self.status_label.config(text=f"Победил: {winner}!")
            else:
                self.status_label.config(text="Ничья!")
        else:
            self.status_label.config(text=f"Ход: {current_player}")

    def set_cell_click_handler(self, handler: Callable[[int, int], None]) -> None:
        """Установить обработчик клика по клетке"""
        self.cell_click_handler = handler

    def set_restart_handler(self, handler: Callable[[], None]) -> None:
        """Установить обработчик перезапуска игры"""
        self.restart_handler = handler
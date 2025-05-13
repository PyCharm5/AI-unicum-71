import tkinter as tk


class TicTacToeView:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-нолики")

        self.cell_click_handler = None
        self.restart_handler = None

        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for row in range(3):
            button_row = []
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
                button_row.append(button)
            self.buttons.append(button_row)

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

    def on_cell_click(self, row, col):
        if self.cell_click_handler:
            self.cell_click_handler(row, col)

    def on_restart_click(self):
        if self.restart_handler:
            self.restart_handler()

    def update_board(self, board_state):
        for row in range(3):
            for col in range(3):
                text = board_state[row][col] if board_state[row][col] else ""
                state = "disabled" if board_state[row][col] else "normal"
                self.buttons[row][col].config(text=text, state=state)

    def update_status(self, current_player, game_over, winner):
        if game_over:
            if winner:
                text = f"Победил: {winner}!"
            else:
                text = "Ничья!"
        else:
            text = f"Ход: {current_player}"
        self.status_label.config(text=text)

    def set_cell_click_handler(self, handler):
        self.cell_click_handler = handler

    def set_restart_handler(self, handler):
        self.restart_handler = handler

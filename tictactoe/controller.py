class TicTacToeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.set_cell_click_handler(self.handle_cell_click)
        self.view.set_restart_handler(self.handle_restart)

        self.update_view()

    def handle_cell_click(self, row, col):
        if self.model.make_move(row, col):
            self.update_view()

    def handle_restart(self):
        self.model.reset_game()
        self.update_view()

    def update_view(self):
        board_state = self.model.board.cells
        current_player = self.model.current_player
        game_over = self.model.game_over
        winner = self.model.winner

        self.view.update_board(board_state)
        self.view.update_status(current_player, game_over, winner)

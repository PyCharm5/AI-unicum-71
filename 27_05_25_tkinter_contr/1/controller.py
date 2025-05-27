from model import Model

class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.bind("<Key>", self.handle_numpad_key)

    def handle_numpad_key(self, click):
        arrow = self.model.get_arrow_direction(click.keycode)
        self.view.label.config(text=arrow)
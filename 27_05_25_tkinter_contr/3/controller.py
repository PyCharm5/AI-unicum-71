class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.canvase.bind("<Button-1>", self.click)

    def click(self, event):
        self.model.sets(event.x, event.y)
        self.animate_circle()

    def animate_circle(self):
        x, y = self.model.dot_x, self.model.dot_y
        coords_now = self.view.gets()
        x_now = (coords_now[0] + coords_now[2]) / 2
        y_now = (coords_now[1] + coords_now[3]) / 2

        dx = (x - x_now)
        dy = (y - y_now)

        if abs(dx) < 1 and abs(dy) < 1:
            self.view.moves(x - x_now, y - y_now)
            return

        self.view.moves(dx, dy)
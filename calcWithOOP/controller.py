class Controller:
    def __init__(self, view):
        self.view = view

    def calculate_area(self, shape):
        area = shape.area()
        self.view.display_area(area)

    def calculate_volume(self, shape):
        volume = shape.volume()
        self.view.display_volume(volume)

    def calculate_formule(self, formula):
        result = formula.calculate()
        self.view.display_formule(result)
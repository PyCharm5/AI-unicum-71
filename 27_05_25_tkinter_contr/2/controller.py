class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.view.button.config(command=self.calculate)

    def calculate(self):
        nums = self.view.gets()
        result = self.model.add_numbers(nums)
        self.view.sets(result)
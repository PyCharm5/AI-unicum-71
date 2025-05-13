from model import CombinatorialCalculatorModel
from view import CombinatorialCalculatorView

class CombinatorialCalculatorController:
    def __init__(self, root):
        self.model = CombinatorialCalculatorModel()
        self.view = CombinatorialCalculatorView(root, self)

    def update_inputs(self):
        func_type = self.view.func_var.get()
        self.view.update_input_fields(func_type != "permutations")

    def calculate(self):
        inputs = self.view.get_input_values()

        try:
            n = int(inputs['n'])
            func_type = inputs['func_type']
            with_repeat = bool(inputs['with_repeat'])

            if func_type == "permutations":
                result = self.model.calculate_permutations(n)
                k = None
            else:
                k = int(inputs['k'])
                if func_type == "arrangements":
                    result = self.model.calculate_arrangements(n, k, with_repeat)
                else:  # combinations
                    result = self.model.calculate_combinations(n, k, with_repeat)

            formula = self.model.get_formula(func_type, n, k, with_repeat, result)
            self.view.show_result(formula)

        except ValueError as e:
            self.view.show_error(str(e))
        except Exception as e:
            self.view.show_error(f"Произошла ошибка: {str(e)}")
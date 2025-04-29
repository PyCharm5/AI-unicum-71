from sympy import sympify

class Calculator:
    def calculate(self, expression):
        result = sympify(expression).evalf()
        return result
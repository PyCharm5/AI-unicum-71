import tkinter as tk
from calc import Calculator

class Calc_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.calculator = Calculator()
        self.widgets()

    def widgets(self):
        self.entry = tk.Entry(self.root, width=25)
        self.entry.place(x=20, y=20)

        self.btn = tk.Button(self.root, text='Вычислить', command=self.btn_command)
        self.btn.place(x=20, y=50)

        self.lbl = tk.Label(self.root, text='Результат: ')
        self.lbl.place(x=200, y=20)

    def btn_command(self):
        expression = self.entry.get()
        result = self.calculator.calculate(expression)
        self.lbl['text'] = 'Результат: ' + str(result)

def main():
    root = tk.Tk()
    app = Calc_GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
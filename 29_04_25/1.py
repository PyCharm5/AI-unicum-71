import tkinter as tk
from PIL import Image, ImageTk

class Calc_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("tkinter")
        self.widgets()

    def widgets(self):
        self.btn = tk.Button(self.root, text='Левая', bg="blue", fg="red", font="Lithos 30", command=self.btn_command)
        self.btn.place(x=20, y=50)

        self.btn = tk.Button(self.root, text='Правая', bg="red", fg="blue", font="Lithos 30", command=self.btn_command)
        self.btn.place(x=300, y=50)

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
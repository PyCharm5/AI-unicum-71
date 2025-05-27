from tkinter import *

class View(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")

        self.label = Label(text="Нажмите стрелки на клавиатуре")

        self.label.place(x=10, y=10)
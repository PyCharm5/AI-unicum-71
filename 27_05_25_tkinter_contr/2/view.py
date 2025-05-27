from tkinter import *

class Viewer(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x400')

        self.enter = Entry(self, width=50)
        self.button = Button(self, text="Расчитать")
        self.label = Label(self, text="")

        self.enter.place(x=10, y=15)
        self.button.place(x=10, y=65)
        self.label.place(x=10, y=40)

    def gets(self):
        return self.enter.get()

    def sets(self, result):
        self.label.config(text=result)
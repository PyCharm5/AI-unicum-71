import tkinter
from tkinter import *

class View(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")

        self.canvase = Canvas(self, bg="white")
        self.canvase.pack(fill=BOTH)

        self.circle = self.canvase.create_oval(
            30, 30, 70, 70,
            fill="red",
        )

    def gets(self):
        return self.canvase.coords(self.circle)

    def moves(self, x, y):
        self.canvase.move(self.circle, x, y)
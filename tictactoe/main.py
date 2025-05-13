import tkinter as tk

from controller import TicTacToeController
from model import GameModel
from view import TicTacToeView

def main():
    root = tk.Tk()
    model = GameModel()
    view = TicTacToeView(root)
    controller = TicTacToeController(model, view)
    root.mainloop()

if __name__ == "__main__":
    main()

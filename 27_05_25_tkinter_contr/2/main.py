from view import Viewer
from model import Model
from controller import Controller

def main():
    view = Viewer()
    model = Model()
    controller = Controller(view, model)

    view.mainloop()


if __name__ == "__main__":
    main()
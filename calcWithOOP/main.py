from model import Square, Rectangle, Circle, Cube, Parallelepiped, Ball, Pyramid, Discriminant, Pythagoras
from controller import Controller
from view import View

def main():
    view = View()
    controller = Controller(view)

    shapes = [
        Square(4),
        Rectangle(3, 5),
        Circle(2),
        Cube(5),
        Parallelepiped(2, 3, 4),
        Ball(5),
        Pyramid(6, 8)
    ]

    disc = Discriminant(1, -13, 12)
    controller.calculate_formule(disc)

if __name__ == "__main__":
    main()
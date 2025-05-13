from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.colorchooser import askcolor


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Выбор фигуры")
        self.geometry("500x375")
        self.selected_color = "#50fb46"
        self.selected_shape = "circle"
        self.create_widgets()

    def create_widgets(self):
        self.frame_title = Frame(self)
        self.frame_title.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.main_lbl = Label(self.frame_title, text="Выберите параметры фигуры",
                              font=("Arial", 24, "bold"))
        self.main_lbl.grid(row=0, column=0, columnspan=2, sticky="w")

        self.params_frame = LabelFrame(self, text="Параметры фигуры", labelanchor="nw")
        self.params_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        self.shape_frame = LabelFrame(self.params_frame, text="Тип фигуры")
        self.shape_frame.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.shape_var = StringVar(value="circle")

        shapes = [
            ("Круг", "circle"),
            ("Квадрат", "square"),
            ("Треугольник", "triangle")
        ]

        for text, shape in shapes:
            Radiobutton(self.shape_frame, text=text, variable=self.shape_var,
                        value=shape, command=self.update_shape).pack(anchor=W)

        self.color_btn = Button(self.params_frame, text="Выбрать цвет",
                                command=self.choose_color)
        self.color_btn.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.size_frame = LabelFrame(self.params_frame, text="Размер фигуры")
        self.size_frame.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.size_label = Label(self.size_frame, text="Размер:")
        self.size_label.pack(side=LEFT)

        self.size_scale = Scale(self.size_frame, from_=50, to=200,
                                orient=HORIZONTAL, command=self.update_shape)
        self.size_scale.set(100)
        self.size_scale.pack()

        self.canvas_frame = Frame(self)
        self.canvas_frame.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

        self.canvas = Canvas(self.canvas_frame, width=300, height=300, bg="white")
        self.canvas.pack(expand=True, fill=BOTH)

        self.update_shape()

    def choose_color(self):
        color = askcolor(title="Выберите цвет фигуры")
        if color[1]:
            self.selected_color = color[1]
            self.update_shape()

    def update_shape(self, event=None):
        self.canvas.delete("all")

        shape = self.shape_var.get()
        size = self.size_scale.get()
        x1, y1 = 50, 50
        x2, y2 = x1 + size, y1 + size

        if shape == "circle":
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.selected_color, outline="black")
        elif shape == "square":
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.selected_color, outline="black")
        elif shape == "triangle":
            points = [x1, y2, x1 + size // 2, y1, x2, y2]
            self.canvas.create_polygon(points, fill=self.selected_color, outline="black")


if __name__ == "__main__":
    app = App()
    app.mainloop()
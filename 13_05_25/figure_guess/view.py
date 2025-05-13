from tkinter import *
from tkinter import messagebox

class CombinatorialCalculatorView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Комбинаторный калькулятор")
        self.root.geometry("570x500")
        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        self.frame_title = Frame(self.root)
        self.frame_title.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.main_lbl = Label(self.frame_title, text="Комбинаторный калькулятор",
                             font=("Arial", 24, "bold"))
        self.main_lbl.grid(row=0, column=0, columnspan=2, sticky="w")

        # Выбор типа комбинаторной функции
        self.func_frame = LabelFrame(self.root, text="Тип комбинаторной функции")
        self.func_frame.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.func_var = StringVar(value="permutations")

        funcs = [
            ("Перестановки", "permutations"),
            ("Размещения", "arrangements"),
            ("Сочетания", "combinations")
        ]

        for text, func in funcs:
            Radiobutton(self.func_frame, text=text, variable=self.func_var,
                        value=func, command=self.controller.update_inputs).pack(anchor=W)

        # Входные параметры
        self.input_frame = LabelFrame(self.root, text="Параметры")
        self.input_frame.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        # Поле для n
        self.n_label = Label(self.input_frame, text="n (общее количество элементов):")
        self.n_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.n_entry = Entry(self.input_frame)
        self.n_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        # Поле для k (будет скрыто для перестановок)
        self.k_label = Label(self.input_frame, text="k (количество выбираемых элементов):")
        self.k_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.k_entry = Entry(self.input_frame)
        self.k_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        # Чекбокс для повторений
        self.repeat_var = IntVar()
        self.repeat_check = Checkbutton(self.input_frame, text="С повторениями",
                                       variable=self.repeat_var)
        self.repeat_check.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=5)

        # Кнопка вычисления
        self.calc_button = Button(self.root, text="Вычислить", command=self.controller.calculate)
        self.calc_button.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        # Поле для результата
        self.result_frame = LabelFrame(self.root, text="Результат")
        self.result_frame.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

        self.result_text = Text(self.result_frame, height=5, width=60, wrap=WORD, state=DISABLED)
        self.result_text.grid(row=0, column=0, padx=5, pady=5)

    def update_input_fields(self, show_k):
        if show_k:
            self.k_label.grid()
            self.k_entry.grid()
        else:
            self.k_label.grid_remove()
            self.k_entry.grid_remove()

    def show_result(self, formula):
        self.result_text.config(state=NORMAL)
        self.result_text.delete(1.0, END)
        self.result_text.insert(END, formula)
        self.result_text.config(state=DISABLED)

    def show_error(self, message):
        messagebox.showerror("Ошибка", message)

    def get_input_values(self):
        return {
            'func_type': self.func_var.get(),
            'n': self.n_entry.get(),
            'k': self.k_entry.get(),
            'with_repeat': self.repeat_var.get()
        }
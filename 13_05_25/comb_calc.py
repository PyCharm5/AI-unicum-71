from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Комбинаторный калькулятор")
        self.geometry("570x500")
        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        self.frame_title = Frame(self)
        self.frame_title.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.main_lbl = Label(self.frame_title, text="Комбинаторный калькулятор",
                              font=("Arial", 24, "bold"))
        self.main_lbl.grid(row=0, column=0, columnspan=2, sticky="w")

        # Выбор типа комбинаторной функции
        self.func_frame = LabelFrame(self, text="Тип комбинаторной функции")
        self.func_frame.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.func_var = StringVar(value="permutations")

        funcs = [
            ("Перестановки", "permutations"),
            ("Размещения", "arrangements"),
            ("Сочетания", "combinations")
        ]

        for text, func in funcs:
            Radiobutton(self.func_frame, text=text, variable=self.func_var,
                        value=func, command=self.update_inputs).pack(anchor=W)

        # Входные параметры
        self.input_frame = LabelFrame(self, text="Параметры")
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
        self.calc_button = Button(self, text="Вычислить", command=self.calculate)
        self.calc_button.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        # Поле для результата
        self.result_frame = LabelFrame(self, text="Результат")
        self.result_frame.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

        self.result_text = Text(self.result_frame, height=5, width=60, wrap=WORD, state=DISABLED)
        self.result_text.grid(row=0, column=0, padx=5, pady=5)

        # Обновляем поля ввода в соответствии с выбранной функцией
        self.update_inputs()

    def update_inputs(self):
        selected_func = self.func_var.get()

        if selected_func == "permutations":
            self.k_label.grid_remove()
            self.k_entry.grid_remove()
        else:
            self.k_label.grid()
            self.k_entry.grid()

    def calculate(self):
        try:
            n = int(self.n_entry.get())
            if n <= 0:
                raise ValueError("n должно быть положительным числом")

            selected_func = self.func_var.get()
            with_repeat = self.repeat_var.get()

            if selected_func == "permutations":
                result = math.factorial(n)
                formula = f"P(n) = n! = {n}! = {result}"
            else:
                k = int(self.k_entry.get())
                if k <= 0:
                    raise ValueError("k должно быть положительным числом")
                if k > n and not with_repeat:
                    raise ValueError("k не может быть больше n без повторений")

                if selected_func == "arrangements":
                    if with_repeat:
                        result = n ** k
                        formula = f"A(n,k) = n^k = {n}^{k} = {result}"
                    else:
                        result = math.factorial(n) // math.factorial(n - k)
                        formula = f"A(n,k) = n!/(n-k)! = {n}!/({n}-{k})! = {result}"
                elif selected_func == "combinations":
                    if with_repeat:
                        result = math.comb(n + k - 1, k)
                        formula = f"C(n,k) = (n+k-1)!/(k!(n-1)!) = ({n}+{k}-1)!/({k}!({n}-1)!) = {result}"
                    else:
                        result = math.comb(n, k)
                        formula = f"C(n,k) = n!/(k!(n-k)!) = {n}!/({k}!({n}-{k})!) = {result}"

            self.show_result(formula)

        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

    def show_result(self, formula):
        self.result_text.config(state=NORMAL)
        self.result_text.delete(1.0, END)
        self.result_text.insert(END, formula)
        self.result_text.config(state=DISABLED)


if __name__ == "__main__":
    app = App()
    app.mainloop()
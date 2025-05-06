from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Задание")
        self.geometry("570x500")
        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        self.frame_title = Frame(self)
        self.frame_title.grid(row=0, column=0, columnspan=2, sticky="ew")

        # Настройка веса колонок для выравнивания
        self.frame_title.columnconfigure(0, weight=0)
        self.frame_title.rowconfigure(1, weight=0)

        self.main_lbl = Label(self.frame_title, text="Форма заявки на работу в зоопарке",
                              font=("Arial", 24, "bold"))
        self.main_lbl.grid(row=0, column=0, columnspan=2, sticky="w")

        self.second_lbl = Label(self.frame_title,
                                text="Пожалуйста, заполните форму. Обязательные поля помечены",
                                font=("Arial", 10, "italic"))
        self.second_lbl.grid(row=1, column=0, sticky="w")

        self.label_star = Label(self.frame_title, text="*", fg="red")
        self.label_star.grid(row=1, column=1, sticky="w")

        # Контакты
        self.temp_label = LabelFrame(self, text="Контактная информация", labelanchor="nw")
        self.temp_label.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        self.temp_label.columnconfigure(1, weight=0)
        self.temp_label.rowconfigure(2, weight=0)

        # Имя с звездочкой
        self.name_frame = Frame(self.temp_label)
        self.name_frame.grid(row=0, column=0, sticky="w")

        self.name_label = Label(self.name_frame, text="Имя")
        self.name_label.pack(side=LEFT)
        self.name_star = Label(self.name_frame, text="*", fg="red")
        self.name_star.pack(side=LEFT)

        self.name_entry = Entry(self.temp_label)
        self.name_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        # Телефон
        self.pol_label = Label(self.temp_label, text="Телефон")
        self.pol_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

        self.phone_entry = Entry(self.temp_label)
        self.phone_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        # Email с звездочкой
        self.email_frame = Frame(self.temp_label)
        self.email_frame.grid(row=2, column=0, sticky="w")

        self.email_label = Label(self.email_frame, text="Email")
        self.email_label.pack(side=LEFT)
        self.email_star = Label(self.email_frame, text="*", fg="red")
        self.email_star.pack(side=LEFT)

        self.email_entry = Entry(self.temp_label)
        self.email_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        # Персональная информация
        self.pers_label = LabelFrame(self, text="Персональная информация", labelanchor="nw")
        self.pers_label.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        self.pers_label.columnconfigure(1, weight=0)
        self.pers_label.rowconfigure(2, weight=0)

        # Возраст с звездочкой
        self.age_frame = Frame(self.pers_label)
        self.age_frame.grid(row=0, column=0, sticky="w")

        self.age_label = Label(self.age_frame, text="Возраст")
        self.age_label.pack(side=LEFT)
        self.age_star = Label(self.age_frame, text="*", fg="red")
        self.age_star.pack(side=LEFT)

        self.age_entry = Entry(self.pers_label)
        self.age_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        self.gender_label = Label(self.pers_label, text="Пол")
        self.gender_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

        self.gender_combobox = ttk.Combobox(self.pers_label,
                                            values=["Мужской", "Женский", "Python"],
                                            state="readonly")
        self.gender_combobox.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        self.gender_combobox.current(0)

        self.qualities_label = Label(self.pers_label, text="Перечислите личные качества")
        self.qualities_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

        self.qualities_entry = Text(self.pers_label, height=5, width=40, wrap=WORD)
        self.qualities_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        # Выбор любимых животных
        self.animals_label = LabelFrame(self, text="Выберите ваших любимых животных", labelanchor="nw")
        self.animals_label.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

        # Создаем фрейм для чекбоксов внутри animals_label
        self.checkboxes_frame = Frame(self.animals_label)
        self.checkboxes_frame.grid(row=0, column=0, sticky="nsew")

        # Первый ряд чекбоксов
        self.zebra_var = IntVar()
        self.zebra_checkbutton = ttk.Checkbutton(self.checkboxes_frame, text="Зебра", variable=self.zebra_var)
        self.zebra_checkbutton.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.cat_var = IntVar()
        self.cat_checkbutton = ttk.Checkbutton(self.checkboxes_frame, text="Кошак", variable=self.cat_var)
        self.cat_checkbutton.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.anaconda_var = IntVar()
        self.anaconda_checkbutton = ttk.Checkbutton(self.checkboxes_frame, text="Анаконда", variable=self.anaconda_var)
        self.anaconda_checkbutton.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        self.human_var = IntVar()
        self.human_checkbutton = ttk.Checkbutton(self.checkboxes_frame, text="Человек", variable=self.human_var)
        self.human_checkbutton.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        # Второй ряд чекбоксов
        self.elephant_var = IntVar()
        self.elephant_checkbutton = ttk.Checkbutton(self.checkboxes_frame, text="Слон", variable=self.elephant_var)
        self.elephant_checkbutton.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.antelope_var = IntVar()
        self.antelope_checkbutton = ttk.Checkbutton(self.checkboxes_frame, text="Антилопа", variable=self.antelope_var)
        self.antelope_checkbutton.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.pigeon_var = IntVar()
        self.pigeon_checkbutton = ttk.Checkbutton(self.checkboxes_frame, text="Голубь", variable=self.pigeon_var)
        self.pigeon_checkbutton.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        self.crab_var = IntVar()
        self.crab_checkbutton = ttk.Checkbutton(self.checkboxes_frame, text="Краб", variable=self.crab_var)
        self.crab_checkbutton.grid(row=1, column=3, padx=5, pady=5, sticky="w")

        # Настройка растягивания главного окна
        self.columnconfigure(3, weight=0)
        self.rowconfigure(1, weight=0)

        self.send_button = Button(self, text="Отправить информацию", command=self.send_form)
        self.send_button.grid(row=4, column=0, padx=5, pady=5, sticky="w")

    def send_form(self):
        # Проверка обязательных полей
        if not self.name_entry.get():
            messagebox.showerror("Ошибка", "Поле 'Имя' обязательно для заполнения!")
            return

        if not self.email_entry.get():
            messagebox.showerror("Ошибка", "Поле 'Email' обязательно для заполнения!")
            return

        if not self.age_entry.get():
            messagebox.showerror("Ошибка", "Поле 'Возраст' обязательно для заполнения!")
            return

        try:
            age = int(self.age_entry.get())
            if age <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Ошибка", "Возраст должен быть положительным числом!")
            return

        # Собираем данные о выбранных животных
        selected_animals = []
        if self.zebra_var.get(): selected_animals.append("Зебра")
        if self.cat_var.get(): selected_animals.append("Кошак")
        if self.anaconda_var.get(): selected_animals.append("Анаконда")
        if self.human_var.get(): selected_animals.append("Человек")
        if self.elephant_var.get(): selected_animals.append("Слон")
        if self.antelope_var.get(): selected_animals.append("Антилопа")
        if self.pigeon_var.get(): selected_animals.append("Голубь")
        if self.crab_var.get(): selected_animals.append("Краб")

        # Формируем сообщение
        message = (
            f"Контактная информация:\n"
            f"Имя: {self.name_entry.get()}\n"
            f"Телефон: {self.phone_entry.get()}\n"
            f"Email: {self.email_entry.get()}\n\n"
            f"Персональная информация:\n"
            f"Возраст: {self.age_entry.get()}\n"
            f"Пол: {self.gender_combobox.get()}\n"
            f"Личные качества:\n{self.qualities_entry.get('1.0', END)}\n"
            f"Любимые животные: {', '.join(selected_animals) if selected_animals else 'Нет'}"
        )

        # Показываем сообщение
        messagebox.showinfo("Данные формы", message)


if __name__ == "__main__":
    app = App()
    app.mainloop()

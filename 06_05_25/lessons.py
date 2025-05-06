from tkinter import *
from tkinter import ttk


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Форма")
        self.geometry("400x500")
        self.create_widgets()

    def create_widgets(self):
        # Основной фрейм
        self.main_frame = Frame(self)
        self.main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Имя
        self.name_label = Label(self.main_frame, text="Ваше имя")
        self.name_label.pack(anchor=W, pady=(0, 5))

        self.name_entry = Entry(self.main_frame)
        self.name_entry.pack(fill=X, pady=(0, 10))
        self.name_entry.insert(0, "Вася")

        self.clear_button = Button(self.main_frame, text="Очистить форму", command=self.clear_form)
        self.clear_button.pack(fill=X, pady=(0, 15))

        # Пароль
        self.pass_label = Label(self.main_frame, text="Введите пароль")
        self.pass_label.pack(anchor=W, pady=(0, 5))

        self.pass_entry = Entry(self.main_frame, show="*")
        self.pass_entry.pack(fill=X, pady=(0, 10))

        self.reset_button = Button(self.main_frame, text="Сброс пароля", command=self.reset_password)
        self.reset_button.pack(fill=X, pady=(0, 15))

        # Интересы
        self.interests_label = Label(self.main_frame, text="Ваши интересы")
        self.interests_label.pack(anchor=W, pady=(0, 5))

        self.interests = ["Компьютеры", "Спорт", "Искусство"]
        for interest in self.interests:
            Checkbutton(self.main_frame, text=f"- {interest}").pack(anchor=W)

        # Combobox для баз данных
        Label(self.main_frame, text="\nБазы данных").pack(anchor=W, pady=(15, 5))
        self.db_combobox = ttk.Combobox(self.main_frame,
                                        values=["MySQL", "PostgreSQL", "Oracle", "MongoDB"], state="readonly")
        self.db_combobox.pack(fill=X, pady=(0, 15))
        self.db_combobox.set("Выберите базу данных")

        # Combobox для уроков
        self.lessons = [
            "1-й урок 9.00 - 9.45",
            "2-й урок 10.00 - 10.45",
            "3-й урок 11.00 - 11.45",
            "4-й урок 12.00 - 12.45",
            "5-й урок 13.00 - 13.45"
        ]

        self.lesson_combobox = ttk.Combobox(self.main_frame, values=self.lessons, state="readonly")
        self.lesson_combobox.pack(fill=X, pady=(0, 10))
        self.lesson_combobox.set("Выберите урок")

    def clear_form(self):
        self.name_entry.delete(0, END)
        self.pass_entry.delete(0, END)
        self.db_combobox.set("Выберите базу данных")
        self.lesson_combobox.set("Выберите урок")

    def reset_password(self):
        self.pass_entry.delete(0, END)


if __name__ == "__main__":
    app = App()
    app.mainloop()
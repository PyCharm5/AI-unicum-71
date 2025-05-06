from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Форма регистрации")
        self.geometry("570x600")
        self.create_widgets()

    def create_widgets(self):
        # Основной контейнер
        self.main_frame = Frame(self)
        self.main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Контакты
        self.contact_frame = LabelFrame(self.main_frame, text="Контактная информация", labelanchor="nw")
        self.contact_frame.pack(fill=X, padx=5, pady=5)

        # ФИО с звездочкой
        self.name_frame = Frame(self.contact_frame)
        self.name_frame.pack(fill=X, pady=2)

        Label(self.name_frame, text="ФИО").pack(side=LEFT)
        Label(self.name_frame, text="*", fg="red").pack(side=LEFT)
        self.name_entry = Entry(self.contact_frame)
        self.name_entry.pack(fill=X, padx=5, pady=2)

        # Телефон
        self.phone_frame = Frame(self.contact_frame)
        self.phone_frame.pack(fill=X, pady=2)

        Label(self.phone_frame, text="Номер телефона").pack(side=LEFT)
        self.phone_entry = Entry(self.contact_frame)
        self.phone_entry.pack(fill=X, padx=5, pady=2)

        # Email с звездочкой
        self.email_frame = Frame(self.contact_frame)
        self.email_frame.pack(fill=X, pady=2)

        Label(self.email_frame, text="Email").pack(side=LEFT)
        Label(self.email_frame, text="*", fg="red").pack(side=LEFT)
        self.email_entry = Entry(self.contact_frame)
        self.email_entry.pack(fill=X, padx=5, pady=2)

        # Город с звездочкой
        self.city_frame = Frame(self.contact_frame)
        self.city_frame.pack(fill=X, pady=2)

        Label(self.city_frame, text="Город").pack(side=LEFT)
        Label(self.city_frame, text="*", fg="red").pack(side=LEFT)
        self.city_entry = Entry(self.contact_frame)
        self.city_entry.pack(fill=X, padx=5, pady=2)

        # Дата рождения с звездочкой
        self.birth_frame = Frame(self.contact_frame)
        self.birth_frame.pack(fill=X, pady=2)

        Label(self.birth_frame, text="Дата рождения").pack(side=LEFT)
        Label(self.birth_frame, text="*", fg="red").pack(side=LEFT)
        self.birth_entry = Entry(self.contact_frame)
        self.birth_entry.pack(fill=X, padx=5, pady=2)

        # Доставка
        self.delivery_frame = LabelFrame(self.main_frame, text="Параметры доставки", labelanchor="nw")
        self.delivery_frame.pack(fill=X, padx=5, pady=5)

        # Индекс с звездочкой
        self.index_frame = Frame(self.delivery_frame)
        self.index_frame.pack(fill=X, pady=2)

        Label(self.index_frame, text="Почтовый индекс").pack(side=LEFT)
        Label(self.index_frame, text="*", fg="red").pack(side=LEFT)
        self.index_entry = Entry(self.delivery_frame)
        self.index_entry.pack(fill=X, padx=5, pady=2)

        # Адрес
        self.address_frame = Frame(self.delivery_frame)
        self.address_frame.pack(fill=X, pady=2)

        Label(self.address_frame, text="Адрес").pack(side=LEFT)
        self.address_text = Text(self.delivery_frame, height=3, wrap=WORD)
        self.address_text.pack(fill=X, padx=5, pady=2)

        # Уведомления
        self.notify_frame = LabelFrame(self.main_frame, text="Предпочитаемый способ получения уведомлений",
                                       labelanchor="nw")
        self.notify_frame.pack(fill=X, padx=5, pady=5)

        self.notify_var = StringVar(value="none")

        self.email_radio = ttk.Radiobutton(self.notify_frame, text="По Email",
                                           variable=self.notify_var, value="email")
        self.email_radio.pack(anchor=W, padx=5, pady=2)

        self.phone_radio = ttk.Radiobutton(self.notify_frame, text="По телефону",
                                           variable=self.notify_var, value="phone")
        self.phone_radio.pack(anchor=W, padx=5, pady=2)

        self.none_radio = ttk.Radiobutton(self.notify_frame, text="Не уведомлять меня",
                                          variable=self.notify_var, value="none")
        self.none_radio.pack(anchor=W, padx=5, pady=2)

        # Кнопка отправки
        self.send_button = Button(self.main_frame, text="Отправить форму",
                                  command=self.send_form, bg="#4CAF50", fg="white")
        self.send_button.pack(pady=10, ipadx=20, ipady=5)

    def send_form(self):
        # Проверка обязательных полей
        errors = []

        if not self.name_entry.get():
            errors.append("Поле 'ФИО' обязательно для заполнения")

        if not self.email_entry.get():
            errors.append("Поле 'Email' обязательно для заполнения")

        if not self.city_entry.get():
            errors.append("Поле 'Город' обязательно для заполнения")

        if not self.birth_entry.get():
            errors.append("Поле 'Дата рождения' обязательно для заполнения")

        if not self.index_entry.get():
            errors.append("Поле 'Почтовый индекс' обязательно для заполнения")

        if errors:
            messagebox.showerror("Ошибка заполнения", "\n".join(errors))
            return

        # Собираем данные формы
        form_data = {
            "ФИО": self.name_entry.get(),
            "Телефон": self.phone_entry.get(),
            "Email": self.email_entry.get(),
            "Город": self.city_entry.get(),
            "Дата рождения": self.birth_entry.get(),
            "Почтовый индекс": self.index_entry.get(),
            "Адрес": self.address_text.get("1.0", END).strip(),
            "Способ уведомлений": self.notify_var.get()
        }

        # Формируем сообщение
        message = "Данные формы:\n\n"
        for key, value in form_data.items():
            message += f"{key}: {value}\n"

        # Показываем сообщение
        messagebox.showinfo("Форма отправлена", message)


if __name__ == "__main__":
    app = App()
    app.mainloop()
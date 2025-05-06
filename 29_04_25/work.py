import tkinter as tk
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk

root = tk.Tk()
root.title("Главное окно")
root.geometry("600x400")

left_button = tk.Button(root, text="Левая кнопка")
left_button.pack(side=tk.LEFT, padx=10, pady=10)

right_button = tk.Button(root, text="Правая кнопка")
right_button.pack(side=tk.RIGHT, padx=10, pady=10)

styled_button = tk.Button(
    root,
    text="Стилизованная кнопка",
    bg="#4CAF50",  # фоновый цвет
    fg="white",  # цвет текста
    font=("Arial", 14),  # шрифт и размер
    padx=20,  # отступ по X
    pady=10,  # отступ по Y
    borderwidth=2,  # ширина рамки
    relief=tk.RAISED  # стиль рамки
)
styled_button.pack(pady=20)


image = ImageTk.PhotoImage(file="D:\google\photo_5246856246819155138_x.jpg")
tk.Button(root, image=image, command=lambda: print('click')).pack()

pressed_button = tk.Button(
    root,
    text="Нажми меня",
    bg="lightblue",
    activebackground="red",  # цвет при нажатии
    activeforeground="white"  # цвет текста при нажатии
)
pressed_button.pack(pady=10)


def button_action():
    messagebox.showinfo("Действие", "Кнопка была нажата!")


action_button = tk.Button(root, text="Выполнить действие", command=button_action)
action_button.pack(pady=10)


def create_second_window():
    second_window = tk.Toplevel(root)
    second_window.title("Второе окно")
    second_window.geometry("300x200")

    full_button = tk.Button(second_window, text="Кнопка на всю форму", bg="lightgreen")
    full_button.pack(fill=tk.BOTH, expand=True)


second_window_button = tk.Button(root, text="Открыть второе окно", command=create_second_window)
second_window_button.pack(pady=10)


def create_buttons_table():
    table_window = tk.Toplevel(root)
    table_window.title("Таблица кнопок")

    for i in range(3):
        for j in range(3):
            btn = tk.Button(table_window, text=f"Кнопка {i + 1}-{j + 1}", width=10, height=2)
            btn.grid(row=i, column=j, padx=5, pady=5)


table_button = tk.Button(root, text="Открыть таблицу кнопок", command=create_buttons_table)
table_button.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)


def show_entry_text():
    text = entry.get()
    messagebox.showinfo("Текст из поля", f"Вы ввели: {text}")


show_text_button = tk.Button(root, text="Показать текст", command=show_entry_text)
show_text_button.pack(pady=5)


def create_name_window():
    name_window = tk.Toplevel(root)
    name_window.title("Ввод имени")
    name_window.geometry("300x150")

    tk.Label(name_window, text="Имя:").pack(pady=5)
    name_entry = tk.Entry(name_window)
    name_entry.pack(pady=5)

    tk.Label(name_window, text="Фамилия:").pack(pady=5)
    surname_entry = tk.Entry(name_window)
    surname_entry.pack(pady=5)

    def show_full_name():
        name = name_entry.get()
        surname = surname_entry.get()
        messagebox.showinfo("Ваше имя", f"Моё имя и фамилия: {name} {surname}")

    tk.Button(name_window, text="Показать", command=show_full_name).pack(pady=10)


name_window_button = tk.Button(root, text="Ввести имя", command=create_name_window)
name_window_button.pack(pady=10)


def clear_entry():
    entry.delete(0, tk.END)


clear_button = tk.Button(root, text="Очистить поле", command=clear_entry)
clear_button.pack(pady=5)

root.mainloop()

import tkinter as tk
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Задание")
        self.geometry("400x400")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Введите имя и фамилию:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)

        self.button1 = tk.Button(self, text="Кнопка 1", command=self.on_button1_click)
        self.button1.pack(side=tk.LEFT, padx=20)

        self.button2 = tk.Button(self, text="Кнопка 2", command=self.on_button2_click)
        self.button2.pack(side=tk.RIGHT, padx=20)

        self.button3 = tk.Button(self, text="Задать имя", bg="lightblue", command=self.show_name)
        self.button3.pack(pady=20)

        self.table_frame = tk.Frame(self)
        self.table_frame.pack(pady=5)

        for i in range(3):
            for j in range(3):
                tk.Button(self.table_frame, text=f"Button {i},{j}").grid(row=i, column=j)

    def on_button1_click(self):
        self.button1.config(bg="green", fg="white")

    def on_button2_click(self):
        self.button2.config(bg="red", fg="black")

    def show_name(self):
        name = self.entry.get()
        if name:
            messagebox.showinfo("Имя и Фамилия", f"Ваше имя и фамилия: {name}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
                            

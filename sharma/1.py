import customtkinter as ctk
from tkinter import messagebox
from hashlib import sha256
import sqlite3
from PIL import Image, ImageTk

# Database class to handle user, order, and pizza data
class Database:
    def __init__(self, db_name="pizzeria.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            age INTEGER UNSIGNED
        )
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            pizza_id INTEGER,
            quantity INTEGER,
            FOREIGN KEY (user_id) REFERENCES Users (id),
            FOREIGN KEY (pizza_id) REFERENCES Pizzas (id)
        )
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Pizzas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL,
            category TEXT,
            image_path TEXT
        )
        ''')
        self.connection.commit()

    def close(self):
        self.connection.close()

    def get_pizzas(self, category=None):
        if category:
            self.cursor.execute('SELECT * FROM Pizzas WHERE category = ?', (category,))
        else:
            self.cursor.execute('SELECT * FROM Pizzas')
        return self.cursor.fetchall()

    def add_pizza(self, name, description, price, category, image_path):
        self.cursor.execute('''
            INSERT INTO Pizzas(name, description, price, category, image_path)
            VALUES (?, ?, ?, ?, ?);
        ''', (name, description, price, category, image_path))
        self.connection.commit()

# Password manager class to handle user registration and authentication
class PasswordManager:
    def __init__(self, db):
        self.db = db

    @staticmethod
    def hash_password(password):
        return sha256(password.encode()).hexdigest()

    def create_user(self, username, password, age):
        hashed_password = self.hash_password(password)
        try:
            self.db.cursor.execute('''
                INSERT INTO Users(username, password, age)
                VALUES (?, ?, ?);
            ''', (username, hashed_password, age))
            self.db.connection.commit()
            messagebox.showinfo("Success", f"User {username} registered successfully.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "User with this username already exists.")

    def authenticate_user(self, username, password):
        hashed_password = self.hash_password(password)
        self.db.cursor.execute('''
            SELECT * FROM Users WHERE username = ? AND password = ?;
        ''', (username, hashed_password))
        return self.db.cursor.fetchone() is not None

# Main application class
class App:
    def __init__(self):
        self.db = Database()
        self.password_manager = PasswordManager(self.db)
        self.logged_in = False
        self.username = ""

        # Добавляем тестовые пиццы в базу данных (если их еще нет)
        self.add_sample_pizzas()

        self.main_window()

    def add_sample_pizzas(self):
        # Проверяем, есть ли уже пиццы в базе данных
        self.db.cursor.execute('SELECT COUNT(*) FROM Pizzas')
        if self.db.cursor.fetchone()[0] == 0:
            # Добавляем тестовые пиццы
            self.db.add_pizza("Pepperoni", "Classic pepperoni pizza", 10.99, "Meat", "images/pepperoni.jpg")
            self.db.add_pizza("Margherita", "Tomato, mozzarella, basil", 8.99, "Vegetarian", "images/margherita.jpg")
            self.db.add_pizza("BBQ Chicken", "BBQ sauce, chicken, onions", 12.99, "Meat", "images/bbq_chicken.jpg")

    def main_window(self):
        self.main = ctk.CTk()
        self.main.title("Dodo Pizza Ordering System")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.login_button = ctk.CTkButton(self.main, text="Login", command=self.login_window)
        self.login_button.pack(pady=20)

        self.register_button = ctk.CTkButton(self.main, text="Register", command=self.registration_window)
        self.register_button.pack(pady=20)

        self.main.mainloop()

    def login_window(self):
        self.login_win = ctk.CTkToplevel(self.main)
        self.login_win.title("Login")

        ctk.CTkLabel(self.login_win, text="Username:").pack(pady=5)
        self.login_entry = ctk.CTkEntry(self.login_win)
        self.login_entry.pack(pady=5)

        ctk.CTkLabel(self.login_win, text="Password:").pack(pady=5)
        self.password_entry = ctk.CTkEntry(self.login_win, show="*")
        self.password_entry.pack(pady=5)

        ctk.CTkButton(self.login_win, text="Login", command=self.login_user).pack(pady=20)

    def registration_window(self):
        self.reg_win = ctk.CTkToplevel(self.main)
        self.reg_win.title("Register")

        ctk.CTkLabel(self.reg_win, text="Username:").pack(pady=5)
        self.username_entry = ctk.CTkEntry(self.reg_win)
        self.username_entry.pack(pady=5)

        ctk.CTkLabel(self.reg_win, text="Password:").pack(pady=5)
        self.password_entry = ctk.CTkEntry(self.reg_win, show="*")
        self.password_entry.pack(pady=5)

        ctk.CTkLabel(self.reg_win, text="Age:").pack(pady=5)
        self.age_entry = ctk.CTkEntry(self.reg_win)
        self.age_entry.pack(pady=5)

        ctk.CTkButton(self.reg_win, text="Register", command=self.register_user).pack(pady=20)

    def login_user(self):
        username = self.login_entry.get()
        password = self.password_entry.get()
        if self.password_manager.authenticate_user(username, password):
            self.logged_in = True
            self.username = username
            messagebox.showinfo("Success", "Login successful!")
            self.login_win.destroy()
            self.menu_window()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        age = self.age_entry.get()
        if username and password and age.isdigit():
            self.password_manager.create_user(username, password, int(age))
            self.reg_win.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all fields correctly.")

    def menu_window(self):
        self.menu_win = ctk.CTkToplevel(self.main)
        self.menu_win.title("Pizza Menu")

        # Фильтры
        filter_frame = ctk.CTkFrame(self.menu_win)
        filter_frame.pack(pady=10)

        ctk.CTkLabel(filter_frame, text="Filter by Category:").pack(side="left", padx=5)
        self.category_var = ctk.StringVar(value="All")
        category_menu = ctk.CTkOptionMenu(filter_frame, variable=self.category_var, values=["All", "Meat", "Vegetarian"], command=self.update_pizza_list)
        category_menu.pack(side="left", padx=5)

        # Список пицц
        self.pizza_list_frame = ctk.CTkFrame(self.menu_win)
        self.pizza_list_frame.pack(pady=10)

        self.update_pizza_list()

    def update_pizza_list(self, category=None):
        # Очищаем текущий список пицц
        for widget in self.pizza_list_frame.winfo_children():
            widget.destroy()

        # Получаем пиццы из базы данных
        if self.category_var.get() == "All":
            pizzas = self.db.get_pizzas()
        else:
            pizzas = self.db.get_pizzas(self.category_var.get())

        # Отображаем пиццы
        for pizza in pizzas:
            pizza_frame = ctk.CTkFrame(self.pizza_list_frame)
            pizza_frame.pack(pady=5, padx=10, fill="x")

            # Изображение пиццы
            try:
                image = Image.open(pizza[5])
                image = image.resize((100, 100), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                image_label = ctk.CTkLabel(pizza_frame, image=photo, text="")
                image_label.image = photo
                image_label.pack(side="left", padx=10)
            except Exception as e:
                print(f"Error loading image: {e}")

            # Информация о пицце
            info_frame = ctk.CTkFrame(pizza_frame)
            info_frame.pack(side="left", fill="both", expand=True)

            ctk.CTkLabel(info_frame, text=pizza[1], font=("Arial", 14)).pack(anchor ="w")
            ctk.CTkLabel(info_frame, text=pizza[2]).pack(anchor="w")
            ctk.CTkLabel(info_frame, text=f"${pizza[3]:.2f}").pack(anchor="w")

            # Кнопка заказа
            order_button = ctk.CTkButton(info_frame, text="Order", command=lambda p=pizza: self.order_pizza(p))
            order_button.pack(pady=5)

    def order_pizza(self, pizza):
        quantity = 1  # Можно добавить ввод количества
        self.db.cursor.execute('''
            SELECT id FROM Users WHERE username = ?;
        ''', (self.username,))
        user_id = self.db.cursor.fetchone()[0]

        self.db.cursor.execute('''
            INSERT INTO Orders(user_id, pizza_id, quantity)
            VALUES (?, ?, ?);
        ''', (user_id, pizza[0], quantity))
        self.db.connection.commit()

        messagebox.showinfo("Success", f"Your order for {pizza[1]} has been placed!")

if __name__ == "__main__":
    app = App()
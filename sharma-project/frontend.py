import customtkinter as ctk
from PIL import Image, ImageTk
import qrcode
from tkinter import messagebox
from tkintermapview import TkinterMapView
import data
from backend import Backend, shaurma, shaurmaBuilder


class Frontend:
    def __init__(self, backend):
        self.backend = backend
        self.window = ctk.CTk()
        self._setup_main_window()
        self.cart_items = []
        self.selected_marker = None  # Инициализация атрибута для выбранного маркера
        self.click_count = 0  # Счетчик кликов для выбора точки

        # Инициализация шаурмы
        self.shaurma_classic = (shaurmaBuilder().set_name("Класическая")
                                .small(350)
                                .normal(400)
                                .big(450)
                                .set_cost("Маленькая:350, Средняя:400, Большая:450")
                                .set_level_of_severity("0")
                                .set_description(
            "Класический поджаренный лаваш, свежий огурчик, листья салата, \nсвежий томат, жаренная курочка, Фирменный соус.")
                                .build())

        # ... (остальные инициализации шаурмы)

    def _setup_main_window(self):
        self.window.title("Шаурма-шоп")
        self.window.geometry("1200x800")

        # Корзина
        cart_frame = ctk.CTkFrame(self.window, width=300)
        cart_frame.pack(side="left", fill="y", padx=10, pady=10)

        ctk.CTkLabel(cart_frame, text="Корзина", font=("Arial", 16)).pack(pady=10)
        self.cart_listbox = ctk.CTkScrollableFrame(cart_frame, width=280, height=500)
        self.cart_listbox.pack()

        self.total_label = ctk.CTkLabel(cart_frame, text="Итого: 0 руб", font=("Arial", 14))
        self.total_label.pack(pady=10)

        ctk.CTkButton(cart_frame, text="Очистить корзину", command=self._clear_cart).pack(pady=5)
        ctk.CTkButton(cart_frame, text="Заказать", command=self._open_payment).pack(pady=10)

        # Товары
        products_frame = ctk.CTkScrollableFrame(self.window)
        products_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        for idx, item in enumerate(data.shaurma_items):
            item_frame = self._create_product_item(products_frame, item, idx)
            item_frame.grid(row=idx // 2, column=idx % 2, padx=10, pady=10)

        # Настройка карты
        self._setup_map()

    def _setup_map(self):
        self.map_widget = TkinterMapView(self.window, width=800, height=600, corner_radius=0)
        self.map_widget.pack(side="right", fill="both", expand=True)
        self.map_widget.set_position(55.7558, 37.6173)  # Пример: Москва
        self.map_widget.set_zoom(12)

        # Добавление обработчика клика на карту
        self.map_widget.add_left_click_map_command(self._on_map_click)

    def _on_map_click(self, latitude, longitude):
        self.click_count += 1  # Увеличиваем счетчик кликов

        if self.click_count == 1:
            messagebox.showinfo("Информация", "Нажмите еще раз, чтобы выбрать точку.")
        elif self.click_count == 2:
            # Удаляем предыдущий маркер, если он есть
            if self.selected_marker:
                self.selected_marker.delete()

            # Добавляем новый маркер
            self.selected_marker = self.map_widget.set_marker(latitude, longitude, text="Выбранная точка")
            messagebox.showinfo("Точка выбрана", f"Вы выбрали точку: {latitude}, {longitude}")
            self.click_count = 0  # Сбрасываем счетчик кликов

    def _create_product_item(self, parent, item, idx):
        try:
            img = ctk.CTkImage(Image.open(f"{item['name']}.png"), size=(150, 150))
        except FileNotFoundError:
            img = ctk.CTkImage(Image.new("RGB", (150, 150), "#333"), size=(150, 150))

        frame = ctk.CTkFrame(parent)

        ctk.CTkLabel(frame, image=img, text="").grid(row=0, column=0)

        size_var = ctk.StringVar(value="Средняя")
        size_menu = ctk.CTkOptionMenu(frame, values=["Маленькая", "Средняя", "Большая"], variable=size_var)
        size_menu.grid(row=2, column=0, pady=5)

        price_label = ctk.CTkLabel(frame, text=f"{item['price'][size_var.get()]} руб")
        price_label.grid(row=3, column=0)

        def update_price(*args):
            price_label.configure(text=f"{item['price'][size_var.get()]} руб")

        size_var.trace("w", update_price)

        ctk.CTkButton(
            frame,
            text="Добавить",
            command=lambda i=item, s=size_var: self._add_to_cart(i, s.get())
        ).grid(row=4, column=0, pady=5)

        return frame

    def _add_to_cart(self, item, size):
        price = item['price'][size]
        cart_item = {
            'name': item['name'],
            'size': size,
            'price': price,
            'description': item['description']
        }
        self.backend.add_to_cart(cart_item)
        self._update_cart_display()

    def _update_cart_display(self):
        for widget in self.cart_listbox.winfo_children():
            widget.destroy()

        for idx, item in enumerate(self.backend.cart):
            item_frame = ctk.CTkFrame(self.cart_listbox, width=260)
            item_frame.pack(fill="x", pady=2)

            ctk.CTkLabel(
                item_frame,
                text=f"{item['name']} ({item['size']}) - {item['price']} руб",
                width=200
            ).pack(side="left")

            ctk.CTkButton(
                item_frame,
                text="×",
                width=30,
                command=lambda i=idx: self._remove_from_cart(i)
            ).pack(side="right")

        self.total_label.configure(text=f"Итого: {self.backend.get_total()} руб")

    def _remove_from_cart(self, index):
        if 0 <= index < len(self.backend.cart):
            self.backend.cart.pop(index)
            self._update_cart_display()

    def _clear_cart(self):
        self.backend.clear_cart()
        self._update_cart_display()

    def _open_payment(self):
        if not self.backend.cart:
            messagebox.showwarning("Корзина пуста", "Добавьте товары в корзину перед оформлением заказа")
            return

        payment_window = ctk.CTkToplevel(self.window)
        payment_window.title("Оплата")
        payment_window.geometry("800x600")
        payment_window.grab_set()

        # Фрейм для координат
        coords_frame = ctk.CTkFrame(payment_window)
        coords_frame.pack(pady=10)

        ctk.CTkLabel(coords_frame, text="Координаты доставки (широта, долгота):").pack(pady=5)

        # Поля для ввода координат
        lat_entry = ctk.CTkEntry(coords_frame, placeholder_text="Широта (например: 55.7558)")
        lat_entry.pack(pady=5)

        lon_entry = ctk.CTkEntry(coords_frame, placeholder_text="Долгота (например: 37.6173)")
        lon_entry.pack(pady=5)

        # Кнопка для установки координат
        ctk.CTkButton(
            coords_frame,
            text="Установить координаты",
            command=lambda: self._set_coordinates(lat_entry, lon_entry)
        ).pack(pady=10)

        ctk.CTkLabel(payment_window, text="Или выберите точку на карте двойным кликом").pack(pady=5)

        # Поля для платежных данных
        fields = ["Номер карты:", "Срок действия (MM/YY):", "CVV:", "Имя на карте:"]
        entries = []

        for field in fields:
            ctk.CTkLabel(payment_window, text=field).pack(pady=5)
            entry = ctk.CTkEntry(payment_window)
            entry.pack(pady=5)
            entries.append(entry)

        ctk.CTkButton(
            payment_window,
            text="Оплатить",
            command=lambda: self._process_payment(payment_window, entries)
        ).pack(pady=20)

    def _set_coordinates(self, lat_entry, lon_entry):
        try:
            latitude = float(lat_entry.get())
            longitude = float(lon_entry.get())

            # Проверка на корректность координат
            if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
                raise ValueError("Некорректные координаты")

            # Удаляем предыдущий маркер, если он есть
            if self.selected_marker:
                self.selected_marker.delete()

            # Устанавливаем новую позицию на карте
            self.map_widget.set_position(latitude, longitude)
            self.map_widget.set_zoom(15)

            # Добавляем маркер
            self.selected_marker = self.map_widget.set_marker(latitude, longitude, text="Выбранная точка")
            messagebox.showinfo("Успешно", f"Координаты установлены: {latitude}, {longitude}")

        except ValueError as e:
            messagebox.showerror("Ошибка", "Введите корректные координаты (числа)\nПример: 55.7558, 37.6173")

    def _process_payment(self, window, entries):
        if any(not entry.get() for entry in entries):
            messagebox.showerror("Ошибка", "Заполните все поля платежных данных")
            return

        if not self.selected_marker:
            messagebox.showerror("Ошибка", "Выберите точку доставки на карте или введите координаты вручную")
            return

        selected_position = self.selected_marker.position

        receipt_number = self.backend.process_payment()
        total = self.backend.get_total()

        payment_info = f"Заказ №{receipt_number}\nСумма: {total} руб\nТочка доставки: {selected_position}"
        qr = qrcode.make(payment_info)

        qr_path = "payment_qr.png"
        qr.save(qr_path)

        qr_window = ctk.CTkToplevel(window)
        qr_window.title("QR-код для оплаты")
        qr_window.geometry("300x300")

        qr_image = ImageTk.PhotoImage(qr)
        qr_label = ctk.CTkLabel(qr_window, image=qr_image)
        qr_label.image = qr_image
        qr_label.pack(pady=20)

        messagebox.showinfo(
            "Чек",
            f"Заказ №{receipt_number} оформлен!\nСумма: {total} руб\nТочка доставки: {selected_position}\nСканируйте QR-код для оплаты!"
        )
        self._clear_cart()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    backend = Backend()
    app = Frontend(backend)
    app.run()
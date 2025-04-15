# backend.py
import random

class Backend:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)

    def get_total(self):
        return sum(item['price'] for item in self.cart)

    def process_payment(self):
        if not self.cart:
            raise ValueError("Корзина пуста")
        return random.randint(100000, 999999)

    def clear_cart(self):
        self.cart.clear()

class shaurma:
    def __init__(self):
        self.name = None
        self.cost = None
        self.level_of_severity = None
        self.description = None
        self.small = None
        self.normal = None

    def __str__(self):
        return f"Название: {self.name}\nЦена: {self.cost}\nУровень остроты: {self.level_of_severity}\nОписание: {self.description}\n"

class shaurmaBuilder():
    def __init__(self):
        self.shaurma = shaurma()
    def set_name(self,name):
        self.shaurma.name = name
        return self
    def small(self, small):
        self.shaurma.small = small
        return self
    def normal(self, normal):
        self.shaurma.normal = normal
        return self
    def big(self, big):
        self.shaurma.big = big
        return self
    def set_cost(self, cost):
        self.shaurma.cost = cost
        return self
    def set_level_of_severity(self, level_of_severity):
        self.shaurma.level_of_severity = level_of_severity
        return self
    def set_description(self, description):
        self.shaurma.description = description
        return self
    def build(self):
        return self.shaurma



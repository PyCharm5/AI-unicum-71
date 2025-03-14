import json
import openpyxl

class TeleBook():
    def __init__(self):
        self.tel_dict = {}

    def add(self, name, tel):
        self.tel_dict[name] = tel

    def delete(self, name):
        del self.tel_dict[name]

    def update(self, name, tel):
        self.tel_dict.update({name: tel})


class json_write(TeleBook):
    def __init__(self, tel_dict, file):
        self.tel_dict = super().tel_dict
        self.file = open('data.json', 'w')

    def write(self):
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(self.tel_dict, f)


class excel_write(TeleBook):
    def __init__(self, tel_dict):
        self.tel_dict = super().tel_dict

    def write(self):
        book = openpyxl.load_workbook(self.file_path)
        sheet = book.active
        sheet.append([self.tel_dict['name'], self.tel_dict['phone']])
        book.save(self.file_path)
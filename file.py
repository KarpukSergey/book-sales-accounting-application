import json
import os


class JsonFile:

    def __init__(self):
        self.employee_file = "employee.json"
        self.book_file = "book.json"
        self.sale_file = "sale.json"
        self.prise_file = "prise.json"

    @staticmethod
    def write_to_file(num, data):
        list_file = ["employee.json", "book.json", "sale.json", "prise.json"]
        with open(list_file[num], "w+", encoding='utf-8') as file:
            json.dump(data, file, indent=4)


    @staticmethod
    def reade_from_file(num):
        list_file = ["employee.json", "book.json", "sale.json", "prise.json"]
        with open(list_file[num - 1], "r", encoding='utf-8') as file:
            if num - 1 == 0:
                data = json.load(file)
                for info in data["employee"]:
                    print(f"Имя: {info.get('first_name')}\n"
                          f"Фамилия: {info.get('last_name')}\n"
                          f"Должность: {info.get('job_title')}\n"
                          f"Номер телефона: {info.get('phone_number')}\n"
                          f"Email: {info.get('email')}\n")
            elif num - 1 == 1:
                data = json.load(file)
                for info in data["book"]:
                    print(f"Название: {info.get('name')}\n"
                          f"Год: {info.get('year')}\n"
                          f"Автор: {info.get('author')}\n"
                          f"Жанр: {info.get('genre')}\n"
                          f"Закупочная цена: {info.get('cost_prise')}\n"
                          f"Цена для продажи: {info.get('price_sale')}\n")
            elif num - 1 == 2:
                data = json.load(file)
                for info in data["sale"]:
                    print(f"Имя продавца: {info.get('name')}\n"
                          f"Название книги: {info.get('book')}\n"
                          f"Дата: {info.get('date')}\n")
            elif num - 1 == 3:
                data = json.load(file)
                for prise in data.values():
                    for value in prise:
                        for key, val in value.items():
                            print(f"Название книги: {key}\n"
                                  f"Цена для продажи: {val}\n")



import csv
import os


class CsvFile:

    def __init__(self):
        self._file_name = "my_info.csv"
        self.create_file()

    def create_file(self):
        title = ["Список книг", "Список сотрудников", "Список продаж", "Список цен на книги"]
        with open(self._file_name, "w", encoding='utf-8', newline='') as file:
            write = csv.DictWriter(file, fieldnames=title)
            write.writeheader()

    def write_info_to_file(self, employee, book, sale, prise):
        title = ["Список книг", "Список сотрудников", "Список продаж", "Список цен на книги"]
        with open(self._file_name, "w", encoding='utf-8', newline='') as file:
            write = csv.DictWriter(file, fieldnames=title)
            write.writeheader()
            shop = {"Список книг": book, "Список сотрудников": employee,
                    "Список продаж": sale, "Список цен на книги": prise}
            write.writerow(shop)

    def read_info_from_file(self, new_shop):
        new_shop.employee_list = []
        new_shop.book_list = []
        new_shop.data_sale = []
        new_shop.real_prise_sale = []
        with open(self._file_name, "r+", newline='') as file:
            reader = csv.DictReader(file)
            count = 0
            list_obj = [new_shop.employee_list, new_shop.book_list, new_shop.data_sale, new_shop.real_prise_sale]
            for info in reader:
                for key, value in info.items():
                    print(list(value))
                    list_obj[count].append(value)
                    count += 1
            print(new_shop.employee_list)



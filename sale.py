from book import Book
from employee import Employee
from file import CsvFile
import datetime


class Sale:

    def __init__(self):
        self.employee_list = []
        self.book_list = []
        self.data_sale = []
        self.real_prise_sale = []
        self.obj_file = CsvFile()

    def write_file(self):
        self.obj_file.write_info_to_file(self.employee_list, self.book_list, self.data_sale, self.real_prise_sale)

    def list_empty(self):
        if len(self.data_sale) == 0:
            return True
        else:
            return False

    def add_employee_list(self):
        new_employee = Employee()
        cr = new_employee.create_employee()
        if cr:
            self.employee_list.append(new_employee)
            print("Сотрудник добавлен")

    def delete_employee_list(self):
        name_del = input("Введите имя сотруника: ").lower()
        while True:
            if len(name_del) != 0:
                for employ in self.employee_list:
                    if employ.first_name == name_del:
                        self.employee_list.remove(employ)
                        print("Сотрудник был удалён")
                        return False
                print("Сотрудник не найден")
                break
            else:
                print("Введите сотрудника для удаления")

    def add_book_list(self):
        new_book = Book()
        cr = new_book.create_book()
        if cr:
            self.book_list.append(new_book)
            self.real_prise_sale.append({new_book.name: new_book.price_sale})
            print("Книга добавлена")

    def delete_book_list(self):
        book_del = input("Введите название книги: ").lower()
        while True:
            if len(book_del) != 0:
                for book in self.book_list:
                    if book.name == book_del:
                        self.book_list.remove(book)
                        print("Книга была удалена")
                        return False
                print("Книга не найдена")
                break
            else:
                print("Введите название книги")

    def add_data_sale(self):
        name_e = None
        name_b = None
        date = None
        while True:
            try:
                if name_e is None:
                    name_employ = input("Введите имя сотрудника который совершил продажу: ").lower()
                    if not any(employ.first_name.lower() == name_employ for employ in self.employee_list):
                        raise ValueError("Tакого сотрудника нет в списки сотрудника")
                    else:
                        name_e = name_employ
                if name_b is None:
                    name_book = input("Введите название книги которую продали: ").lower()
                    if not any(book.name.lower() == name_book for book in self.book_list):
                        raise ValueError("Такой книги нету в списке продаж")
                    else:
                        name_b = name_book
                if date is None:
                    print("Введите дату в формате: date.month.year")
                    data_sale = input("Введите дату продажи: ")
                    if datetime.datetime.strptime(data_sale, '%d.%m.%Y') is False:
                        raise ValueError("Invalid date")
                    elif any(i.isalpha() for i in data_sale):
                        raise ValueError("Дата не должна содержать буквы")
                    else:
                        date = data_sale
                self.data_sale.append([name_e, name_b, date])
                print("Информация о продаже добавлена")
                break
            except ValueError as s:
                print(s)

    def delete_data_sale(self):
        name_employ = input("Введите имя сотрудника который совершил продажу: ")
        print("Введите дату в формате: date.month.year\n")
        data_sale = input("Введите дату продажи: ")
        name_book = input("Введите название книги которую продали: ")
        for data in self.data_sale:
            if name_employ in data:
                if name_book in data:
                    if data_sale in data:
                        self.data_sale.remove(data)
                        print("Информация о продаже удалена")
                        return
                    else:
                        print("Такой продажи в этот день нету")
                else:
                    print(f"Такую книгу продавец {name_employ} не продавал")
        print("продавец не найден")

    def show_info_sale(self):
        if self.list_empty():
            print("Список продаж пуст")
            return
        count = 0
        while True:
            try:
                print("Введите дату в формате: date.month.year")
                data = input("Введите дату продажи: ")
                data = datetime.datetime.strptime(data, '%d.%m.%Y')
                break
            except ValueError as s:
                print("Invalid date")
        print()
        for info in self.data_sale:
            info_date = datetime.datetime.strptime(info[2], '%d.%m.%Y')
            if data == info_date:
                print(f"Продавец: {info[0]}\n"
                      f"Книга: {info[1]}\n"
                      f"Дата продажи: {info[2]}\n")
                count += 1
        if count == 0:
            print("За эту дату продаж небыло")

    def show_info_sale_period(self):
        if self.list_empty():
            print("Список продаж пуст")
            return
        print("Введите дату в формате: date.month.year")
        count = 0
        while True:
            try:
                data1 = input("Введите c какого числа вывести продажи: ")
                data2 = input("Введите до какого числа вывести продажи: ")
                data1 = datetime.datetime.strptime(data1, '%d.%m.%Y')
                data2 = datetime.datetime.strptime(data2, '%d.%m.%Y')
                break
            except ValueError as s:
                print("Invalid date!!!")
        print()
        for info in self.data_sale:
            info_data = datetime.datetime.strptime(info[2], '%d.%m.%Y')
            if data1 <= info_data < data2:
                print(f"Продавец: {info[0]}\n"
                      f"Книга: {info[1]}\n"
                      f"Дата продажи: {info[2]}\n")
                count += 1
        if count == 0:
            print("За этот период нет продаж")

    def show_info_sale_employee(self):
        if self.list_empty():
            print("Список продаж пуст")
            return
        count = 0
        name_empl = input("Введите имя продавца: ")
        for info in self.data_sale:
            if name_empl in info:
                print(f"Продавец: {info[0]}\n"
                      f"Книга: {info[1]}\n"
                      f"Дата продажи: {info[2]}\n")
                count += 1
        if count == 0:
            print("Продавец не найден")

    def show_info_best_book(self):
        if self.list_empty():
            print("Список продаж пуст")
            return
        best_book = ["", 0]
        best_dict = dict()
        print("Введите дату в формате: date.month.year")
        while True:
            try:
                data1 = input("Введите c какого числа вывести продажи: ")
                data2 = input("Введите до какого числа вывести продажи: ")
                data1 = datetime.datetime.strptime(data1, '%d.%m.%Y')
                data2 = datetime.datetime.strptime(data2, '%d.%m.%Y')
                break
            except ValueError as s:
                print("Invalid date!!!")
        count = 0
        for info in self.data_sale:
            info_data = datetime.datetime.strptime(info[2], "%d.%m.%Y")
            if info[1] in best_book and data1 <= info_data <= data2:
                best_dict[info[1]] += 1
            elif data1 <= info_data <= data2:
                best_dict[info[1]] = 1
                count += 1

        if count == 0:
            print("Список продаж за этот период пуст")
        else:
            for key, value in best_dict.items():
                if value > best_book[1]:
                    best_book = [key, value]

            print(f"Бесцелером за период с {str(data1)} и {str(data2)} до стала книга под названием {best_book[0]}")

    def show_info_best_employee(self):
        if self.list_empty():
            print("Список продаж пуст")
            return
        best_employe = ["", 0]
        dict_employe = dict()
        print("Введите дату в формате: date.month.year")
        while True:
            try:
                data1 = input("Введите c какого числа вывести продажи: ")
                data2 = input("Введите до какого числа вывести продажи: ")
                data1 = datetime.datetime.strptime(data1, '%d.%m.%Y')
                data2 = datetime.datetime.strptime(data2, '%d.%m.%Y')
                break
            except ValueError as s:
                print("Invalid date!!!")
        count = 0
        for info in self.data_sale:
            info_data = datetime.datetime.strptime(info[2], "%d.%m.%Y")
            if info[0] in best_employe and data1 <= info_data <= data2:
                dict_employe[info[0]] += 1
            elif data1 <= info_data <= data2:
                dict_employe[info[0]] = 1
                count += 1

        if count == 0:
            print("К сожелению список продаж пуст")
        else:
            for key, value in dict_employe.items():
                if value > best_employe[1]:
                    best_employe = [key, value]
            for emoloye in self.employee_list:
                if emoloye.first_name == best_employe[0]:
                    print(f"Имя: {emoloye.first_name}\n"
                          f"Фамилия: {emoloye.last_name}\n"
                          f"Должность: {emoloye.job_title}\n"
                          f"Номер телефона: {emoloye.phone_number}\n"
                          f"Email: {emoloye.email}")

    def profit(self):
        if self.list_empty():
            print("Список продаж пуст")
            return
        list_book = []
        profit_sum = 0
        print("Введите дату в формате: date.month.year")
        while True:
            try:
                data1 = input("Введите c какого числа вывести продажи: ")
                data2 = input("Введите до какого числа вывести продажи: ")
                data1 = datetime.datetime.strptime(data1, '%d.%m.%Y')
                data2 = datetime.datetime.strptime(data2, '%d.%m.%Y')
                break
            except ValueError as s:
                print("Invalid date!!!")
        count = 0
        for info in self.data_sale:
            info_data = datetime.datetime.strptime(info[2], "%d.%m.%Y")
            if data1 <= info_data <= data2:
                list_book.append(info[1])
                count += 1

        if count == 0:
            print("Список продаж за этот период пуст")
        else:
            for book in list_book:
                for prise in self.book_list:
                    if book == prise.name:
                        profit_sum += int(prise.cost_prise) - int(prise.price_sale)

            print(f"Прибыль за период с {data1} до {data2} состовляет {abs(profit_sum)}")

    def best_genre(self):
        if self.list_empty():
            print("Список продаж пуст")
            return
        list_book = []
        best_dict = dict()
        print("Введите дату в формате: date.month.year")
        while True:
            try:
                data1 = input("Введите c какого числа вывести продажи: ")
                data2 = input("Введите до какого числа вывести продажи: ")
                data1 = datetime.datetime.strptime(data1, '%d.%m.%Y')
                data2 = datetime.datetime.strptime(data2, '%d.%m.%Y')
                break
            except ValueError as s:
                print("Invalid date!!!")
        count = 0
        for info in self.data_sale:
            info_data = datetime.datetime.strptime(info[2], "%d.%m.%Y")
            if data1 <= info_data <= data2:
                list_book.append(info[1])
                count += 1

        if count == 0:
            print("Список продаж за этот период пуст")
        else:
            for sale_book in list_book:
                for book in self.book_list:
                    if sale_book in best_dict:
                        best_dict[book.genre] += 1
                    elif sale_book == book.name:
                        best_dict[book.genre] = 1
            list_book = ["", 0]
            for key, value in best_dict.items():
                if value > list_book[1]:
                    list_book = [key, value]
            print(f"Самый популярный жанр за период с {data1} до {data2} это {list_book[0]}")

    def best_author(self):
        if self.list_empty():
            print("Список продаж пуст")
            return
        list_book = []
        best_dict = dict()
        print("Введите дату в формате: date.month.year")
        while True:
            try:
                data1 = input("Введите c какого числа вывести продажи: ")
                data2 = input("Введите до какого числа вывести продажи: ")
                data1 = datetime.datetime.strptime(data1, '%d.%m.%Y')
                data2 = datetime.datetime.strptime(data2, '%d.%m.%Y')
                break
            except ValueError as s:
                print("Invalid date!!!")
        count = 0
        for info in self.data_sale:
            info_data = datetime.datetime.strptime(info[2], "%d.%m.%Y")
            if data1 <= info_data <= data2:
                list_book.append(info[1])
                count += 1

        if count == 0:
            print("Список продаж за этот период пуст")
        else:
            for sale_book in list_book:
                for book in self.book_list:
                    if sale_book in best_dict:
                        best_dict[book.author] += 1
                    elif sale_book == book.name:
                        best_dict[book.author] = 1
            list_book = ["", 0]
            for key, value in best_dict.items():
                if value > list_book[1]:
                    list_book = [key, value]
            print(f"Самый популярный жанр за период с {data1} до {data2} это {list_book[0]}")

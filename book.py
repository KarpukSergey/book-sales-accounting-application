class Book:

    def __init__(self, name=None, year=None, author=None,
                 genre=None, cost_prise=None, price_sale=None):
        self.name = name
        self.year = year
        self.author = author
        self.genre = genre
        self.cost_prise = cost_prise
        self.price_sale = price_sale

    def create_book(self):
        print("Добавление книги\n")
        while True:
            try:
                if self.name is None:
                    name = input("Введите название книги: ").lower()
                    if len(name) == 0:
                        raise ValueError("Введите имя!!!\n")
                    elif len(name) > 30:
                        raise ValueError("Имя привысило количество символов - '15'\n")
                    else:
                        self.name = name
                if self.year is None:
                    year = input("Введите год выпуска: ")
                    if any(num.isalpha() for num in year):
                        raise ValueError("Введите год издание книги\n")
                    elif 0 >= len(year) > 4:
                        raise ValueError("Год выпуска не доджен привышать и быть меньше 4 сиволов")
                    else:
                        self.year = year
                if self.author is None:
                    author = input("Введите имя автора: ")
                    if len(author) == 0:
                        raise ValueError("Введите имя автора!!!\n")
                    elif len(author) > 20:
                        raise ValueError("Имя привысило количество символов - '20'\n")
                    elif any(i.isdigit() for i in author):
                        raise ValueError("В имени автора не дожно быть цыфр")
                    else:
                        self.author = author
                if self.genre is None:
                    genre = input("Введите жанр книги: ")
                    if any(ch.isdigit() for ch in genre):
                        raise ValueError("Водите только буквы!!!")
                    elif len(genre) == 0:
                        raise ValueError("Введите имя жанр!!!\n")
                    elif len(genre) > 25:
                        raise ValueError("Имя привысило количество символов - '20'\n")
                    else:
                        self.genre = genre
                if self.cost_prise is None:
                    cost_prise = input("Введите себестоймость книги: ")
                    if any(num.isalpha() for num in cost_prise):
                        raise ValueError("Ошибка даных введёное не является числом")
                    else:
                        self.cost_prise = cost_prise
                if self.price_sale is None:
                    price_sale = input("Введите стоимость книги для покупателя: ")
                    if any(num.isalpha() for num in price_sale):
                        raise ValueError("Ошибка даных введёное не является числом")
                    else:
                        self.price_sale = price_sale
                        return True
            except ValueError as s:
                print(s)
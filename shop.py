from sale import Sale, datetime


class BookShop:

    @staticmethod
    def shop_menu(shop_sale=None):
        # shop_sale = Sale()
        while True:
            print("""
            \tSHOP MENU
            1  Повна інформація про співробітників книгарні.
            2  Повна інформація про книги.
            3  Повна інформація про продаж.
            4  Усі продажі за певну дату.
            5  Усі продажі за певний період часу.
            6  Усі продажі певного співробітника.
            7  Назва книги, яка стала бестселером за вказаний період часу.
            8  Інформація про найуспішнішого продавця за вказаний період часу.
            9  Сумарний прибуток за вказаний період часу.
            10  Найпопулярніший автор за вказаний період часу.
            11  Найпопулярніший жанр за вказаний період часу.
            12  Додавання інформації про співробітників.
            13  Видалення інформації про співробітників.
            14  Додавання інформації про книги.
            15  Видалення інформації про книги.
            16  Додавання інформації про продаж.
            17  Видалення інформації про продаж.
            18  Записать информацию в файл.
            19  Вывести информацию из файла
            20  Выход из магазина.
            """)
            selection = input("\t\tВведите выбор: ")
            print()
            if selection == "1":
                print("Повна інформація про співробітників книгарні\n")
                if len(shop_sale.employee_list) != 0:
                    for employ in shop_sale.employee_list:
                        print(f"Имя: {employ.first_name.title()}\n"
                              f"Должность: {employ.last_name.title()}\n"
                              f"Номер телефона: {employ.phone_number}\n"
                              f"Email: {employ.email}")
                        print()
                else:
                    print("Список сотрудников пуст")
            elif selection == "2":
                print("Повна інформація про книги\n")
                if len(shop_sale.book_list) != 0:
                    for book in shop_sale.book_list:
                        print(f"Назва книги: {book.name.title()}\n"
                              f"Рік видання: {book.year}\n"
                              f"Автор: {book.author}\n"
                              f"Жанр: {book.genre}\n"
                              f"Собівартість: {book.cost_prise}\n"
                              f"Потенційна ціна продажу: {book.price_sale}")
                else:
                    print("Список книг пуст")
            elif selection == "3":
                print("Повна інформація про продаж\n")
                if len(shop_sale.real_prise_sale) != 0:
                    for prise in shop_sale.data_sale:
                        print(f"Имя сотрудника: {prise[0].title()}\n"
                              f"Книга: {prise[1].title()}\n"
                              f"Дата продажы: {prise[2]}\n")
                        print()
                else:
                    print("Список цен пуст")
            elif selection == "4":
                print("Усі продажі за певну дату\n")
                shop_sale.show_info_sale()
            elif selection == "5":
                print("Усі продажі за певний період часу\n")
                shop_sale.show_info_sale_period()
            elif selection == "6":
                print("Усі продажі певного співробітника\n")
                shop_sale.show_info_sale_employee()
            elif selection == "7":
                print("Назва книги, яка стала бестселером за вказаний період часу\n")
                shop_sale.show_info_best_book()
            elif selection == "8":
                print("Інформація про найуспішнішого продавця за вказаний період часу\n")
                shop_sale.show_info_best_employee()
            elif selection == "9":
                print("Сумарний прибуток за вказаний період часу\n")
                shop_sale.profit()
            elif selection == "10":
                print("Найпопулярніший автор за вказаний період часу\n")
                shop_sale.best_author()
            elif selection == "11":
                print("Найпопулярніший жанр за вказаний період часу\n")
                shop_sale.best_genre()
            elif selection == "12":
                print("Додавання інформації про співробітників\n")
                shop_sale.add_employee_list()
                shop_sale.write_file()
            elif selection == "13":
                print("Видалення інформації про співробітників\n")
                shop_sale.delete_employee_list()
                shop_sale.write_file()
            elif selection == "14":
                print("Додавання інформації про книги\n")
                shop_sale.add_book_list()
                shop_sale.write_file()
            elif selection == "15":
                print("Видалення інформації про книги\n")
                shop_sale.delete_book_list()
                shop_sale.write_file()
            elif selection == "16":
                print("Додавання інформації про продаж\n")
                shop_sale.add_data_sale()
                shop_sale.write_file()
            elif selection == "17":
                print("Видалення інформації про продаж\n")
                shop_sale.delete_data_sale()
                shop_sale.write_file()
            elif selection == "18":
                print("Записать информацию в файл\n")
                shop_sale.write_file()
            elif selection == "19":
                print("Вывести информацию из файла\n")
                shop_sale.reade_file()
            elif selection == "20":
                print("Выход из магазина\n")
                break
            else:
                print("Такого пункта не существует")


# if __name__ == '__main__':
#     my_shop = BookShop()
#     my_shop.shop_menu()
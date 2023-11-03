from book import Book
from employee import Employee
from sale import Sale
from shop import BookShop

if __name__ == '__main__':
    my_shop = BookShop()
    shop_sale = Sale()
    shop_sale.book_list.append(Book("a_book", "2012", "puschkin", "roman", "156", "200"))
    shop_sale.book_list.append(Book("b_book", "2013", "scheva", "pop", "120", "250"))
    shop_sale.book_list.append(Book("c_book", "2014", "puschkin", "roman", "120", "220"))
    shop_sale.employee_list.append(Employee("A_employee", "A-familia", "A-Developer", "+38099999999", "user1@gmail.com"))
    shop_sale.employee_list.append(Employee("B_employee", "B-familia", "B-Developer", "+38066666666", "user2@gmail.com"))
    shop_sale.employee_list.append(Employee("B_employee", "C-familia", "B-Developer", "+38066666666", "user2@gmail.com"))
    shop_sale.data_sale.append(["A_employee", "a_book", "03.11.2023"])
    shop_sale.data_sale.append(["B_employee", "b_book", "05.11.2023"])
    shop_sale.data_sale.append(["B_employee", "c_book", "11.11.2023"])
    shop_sale.real_prise_sale.append({"a_book": "200"})
    shop_sale.real_prise_sale.append({"b_book": "250"})
    shop_sale.real_prise_sale.append({"c_book": "220"})
    my_shop.shop_menu(shop_sale)




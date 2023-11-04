import json


class Employee:

    def __init__(self, first_name=None, last_name=None,
                 job_title=None, phone_number=None, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.phone_number = phone_number
        self.email = email

    def create_employee(self):
        while True:
            try:
                if self.first_name is None:
                    first_name = input("Введите имя: ").lower()
                    if len(first_name) > 20:
                        raise ValueError("Имя превышает 20 символов\n")
                    elif len(first_name) == 0:
                        raise ValueError("Вы должны ввести имя сорутдника\n")
                    elif any(ch.isdigit() for ch in first_name):
                        raise ValueError("Имя не должно содержать цыфры\n")
                    else:
                        self.first_name = first_name
                if self.last_name is None:
                    last_name = input("Введите фамилию: ").lower()
                    if len(last_name) > 20:
                        raise ValueError("Фамилия превышает 20 символов\n")
                    elif len(last_name) == 0:
                        raise ValueError("Вы должны ввести фамилию сорутдника\n")
                    elif any(ch.isdigit() for ch in last_name):
                        raise ValueError("Фамилия не должно содержать цыфры\n")
                    else:
                        self.last_name = last_name
                if self.job_title is None:
                    job_title = input("Введите должность сотрудника: ")
                    if len(job_title) > 30:
                        raise ValueError("Строка долность сотрудника превышает 30 символов\n")
                    elif len(job_title) == 0:
                        raise ValueError("Вы должны ввести  долность сотрудника\n")
                    elif any(ch.isdigit() for ch in job_title):
                        raise ValueError("Строка долность сотрудника не должна содержать цыфры\n")
                    else:
                        self.job_title = job_title
                if self.phone_number is None:
                    phone_number = input("Введите номер телефона: ")
                    if len(phone_number) == 0:
                        raise ValueError("Вы должны ввести номер телефона")
                    elif any(num.isalpha() for num in phone_number):
                        raise ValueError("Номер телефона не должен содержать буквы")
                    else:
                        self.phone_number = phone_number
                if self.email is None:
                    print("Почта должна быть gmail\n")
                    email = input("Введите почту: ")
                    if not email.endswith("@gmail.com"):
                        raise ValueError("строка должна заканчиваться: ...@gmail.com")
                    elif len(email) > 40:
                        raise ValueError("почта не должна быть больше 40 символов")
                    else:
                        self.email = email
                        return True
            except ValueError as s:
                print(s)

    def to_json(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "job_title": self.job_title,
            "phone_number": self.phone_number,
            "email": self.email
        }
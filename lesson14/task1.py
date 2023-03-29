# Создать класс Contact, у которого должны быть атрибуты email, phone, first_name, last_name
# Сделать валидации, что email - строка, содержащая символ @ и правая часть находится в списке из:
# gmail.com, yandex.ru, ya.ru, yahoo.com
#
# phone - номер телефона начинается с символа +, код страны находится в списке
# 375, 48, 374
#
# first_name, last_name - строки, начинающиеся с большой буквы и длиной от 5 до 15  символов
#
# Все проверки реализовать через property
class Contact:
    def __init__(self, email, phone, first_name, last_name) ->None:
        self.email = email
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def _valid_email(value: str) -> None:
        email = value.split("@")
        if len(email) != 2:
            raise ValueError("Email must contains only one @.")

        if email[1] not in ["gmail.com", "yandex.ru", "ya.ru", "yahoo.com"]:
            raise ValueError("Unsupported email provider.")

    @staticmethod
    def _validation_phone(value) -> None:
        if value[0] != "+":
            raise ValueError("Phone must starts from +.")

        if len(value) != 13:
            raise ValueError("Phone length must be 13.")

        if value[1:4] not in ("375", "374") and value[1:3] != "48":
            raise ValueError("code must be start from 375 or 374 or 48")

    @staticmethod
    def _validation_name(value: str) -> None:
        if not value[0].isupper():
            raise ValueError("Name should start from capital letter.")

        if len(value) not in range(5, 16):
            raise ValueError("Name length must be in range (5, 15).")

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        self._valid_email(value=value)
        self._email = value

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str) -> None:
        self._validation_phone(value=value)
        self._phone = value

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        self._validation_name(value=value)
        self._first_name = value

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        self._validation_name(value=value)
        self._last_name = value


contact = Contact("dddd@gmail.com", "+375111111111", "Aleksandra", "Krivaltsevich")
print(contact)


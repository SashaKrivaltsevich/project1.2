from random import random, choice
import string


class EmailProvider:
    def __call__(self, *args, **kwargs):
        email_dom = ['gmail.com', 'mail.ru', 'yandex.ru', 'yahoo.com']
        username = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        return f'{username}@{email_dom}'


class PhoneProvider:
    @staticmethod
    def get_digit():
        digits = string.digits
        return choice(digits)

    def __call__(self, *args, **kwargs):
        first_num = ['29', '33', '44']
        return f"+375 {choice(first_num)} {''.join([self.get_digit() for _ in range(7)])}"


class BankCardProvider:
    @staticmethod
    def get_digit():
        digits = string.digits
        return choice(digits)

    def __call__(self, *args, **kwargs):
        return f"{''.join([self.get_digit() for _ in range(16)])}"


class NameProvider:
    def __call__(self, *args, **kwargs):
        first_names = ["Sasha", "Dasha", "Masha", "Max", "Alex", "Elena"]
        return choice(first_names)




import random
import string
from typing import Any


class EmailProvider:
    @staticmethod
    def generate() -> str:
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com'])
        return f"{username}@{domain}"


class PhoneProvider:
    @staticmethod
    def generate() -> str:
        digits = ''.join(random.choice(string.digits) for _ in range(7))
        prefix = ["33", "25", "29"]
        return f'+375({random.choice(prefix)}) {digits[:3]}-{digits[3:5]}-{digits[5:]}'


class BankCardProvider:
    @staticmethod
    def generate() -> str:
        return ''.join(random.choices(string.digits, k=16))


class NameProvider:
    @staticmethod
    def generate() -> str:
        first_name = random.choice(['Sasha', 'Dasha', 'Masha', 'Max'])
        last_name = random.choice(['Smith', 'Brown', 'Tolstoy', 'Bowie'])
        return f"{first_name} {last_name}"

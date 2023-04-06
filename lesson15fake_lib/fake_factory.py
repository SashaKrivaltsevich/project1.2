from typing import Type, Generator
from provider import PhoneProvider, NameProvider, BankCardProvider, EmailProvider


class FakeFactory:
    def __init__(self, provider: Type, number: int) -> None:
        if number <= 0:
            raise ValueError("Count must be greater than 0")
        self.provider = provider
        self.number = number
        self.index = 0

    def __iter__(self) -> 'FakeFactory':
        self.index = 0
        return self

    def __next__(self) -> str:
        if self.index >= self.number:
            raise StopIteration
        self.index += 1
        return self.provider.generate()

    def generate(self) -> str:
        return self.provider.generate()


def generate(self) -> int:
    return self.provider_class.generate()


def __len__(self) -> int:
    return self.count


def __repr__(self) -> str:
    return f"<FakeFactory(provider={self.provider_class.__name__}, count={self.count})>"


fake = FakeFactory(PhoneProvider,  2)


print(fake.generate())
print()

for email in fake:
    print(email)
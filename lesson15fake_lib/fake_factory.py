from provider import PhoneProvider


class FakeFactory:
    def __init__(self, provider, number):
        if number <= 0:
            raise ValueError('number must be more than 0')
        self.provider = provider
        self.number = number

    def generate(self):
        return self.provider()

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration
        self.number -= 1
        return self.generate()


fake = FakeFactory(PhoneProvider(), 2)
print(fake.generate())
print()

for email in fake:
    print(email)

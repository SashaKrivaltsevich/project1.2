# def alph_range():
#     print(list(map(chr, range(97, 123))))


class Alphabet:
    def __init__(self, end, lower):
        self.end = end
        self.first = 97
        self.lower = lower

    def __next__(self):

        if self.value == ord(self.end):
            raise StopIteration
        else:
            self.value += 1

        return chr(self.value)

    def __iter__(self):
        if self.lower is False:
            self.first = 65
            self.end = self.end.upper()
        self.value = self.first - 1
        return self


for letter in Alphabet(end="d", lower=True):
    print(letter)


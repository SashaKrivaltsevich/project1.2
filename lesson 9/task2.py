"""
Программа на вход должна принимать файл с каким-то текстом.
Пользователь вводит любую английскую букву.
Программа должна считать сколько раз эта буква встречается в тексте
(без учёта регистра).
То есть буквы n и N считать одинаковыми.
"""
def letter_count(letter: str):
    counter = 0
    with open('text.txt', 'r') as file_txt:
        for line in file_txt:
            for i in range(len(line)):
                if letter.lower() == line[i] or letter.upper() == line[i]:
                    counter += 1
            print(f'Буква встречается {counter} раз')


letter_count(input("Введите латинскую букву: "))

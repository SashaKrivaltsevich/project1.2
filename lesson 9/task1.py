"""
Есть 2 словаря
first_dict = { 'a': 1, 'b': 2, 'c': 3}
second_dict = { 'c': 3, 'd': 4,'e': 5}
Необходимо их объединить по ключам,
а значения ключей поместить в список,
если у одного словаря есть ключ "а",
а у другого нету, то поставить значение None на соответствующую позицию
(1-я позиция для 1-ого словаря, вторая для 2-ого)
"""
from collections import defaultdict


def get_common_dict(first_dct: dict, second_dct: dict) -> dict:
    merged_dict = [first_dct, second_dct]
    key_list = []
    [key_list.append(key) for item in merged_dict
     for key in item.keys() if key not in key_list]
    result = defaultdict(list)
    for item in merged_dict:
        for key in key_list:
            result[key].append(item.get(key))

    return dict(result)


print(get_common_dict({'a': 1, 'b': 2, 'c': 3, 'ff': 2.3},
                      {'c': 3, 'd': 4, 'e': 5, '3': -8}))

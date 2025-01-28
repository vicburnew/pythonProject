from typing import List


def get_polindroms(a: list[int]) -> List[int]:
    """Функция, которая получает на вход список чисел и возвращает новый список,
    содержащий только числа, которые являются палиндромами"""
    new_list = []
    for item in a:
        item_string = str(item)
        item_reversed = item_string[::-1]
        if item_reversed == item_string:
            new_list.append(item)
    return new_list

    # return [i for i in a if str(i) == str(i)[::-1]]

print(get_polindroms([121, 123, 131, 34543]))

# Пример вывода:
# [121, 131, 34543]

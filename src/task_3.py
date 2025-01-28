from typing import List


def get_unique_numbers(list_1: List[int], list_2: List[int]) -> List[int]:
    """Функция, которая получает на вход два списка чисел и возвращает новый список,
    содержащий только те числа, которые есть только в одном из списков."""
    # set_a = set(list_1)
    # set_b = set(list_2)
    # set_c = set_a.difference(set_b)
    # set_d = set_b.difference(set_a)
    # set_e = set_c.union(set_d)
    # list_c = list(set_e)
    # return list_c
    return list(set(list_1) - set(list_2)) + list(set(list_2) - set(list_1))


print(get_unique_numbers([1, 2, 3, 4], [3, 4, 5, 6]))
# Пример вывода: [1, 2, 5, 6]

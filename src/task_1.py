from typing import List


def function_list_intersection(a: List[int], b: List[int]) -> List[int]:
    """Функция, которая получает на вход два списка чисел и возвращает новый список,
    содержащий только те числа, которые встречаются в обоих списках."""
    set_a = set(a)
    set_b = set(b)
    set_c = set_a.intersection(set_b)
    list_c = list(set_c)
    return list_c

# альтернативное решение:
#     return([i for i in a if i in b])

print(function_list_intersection([1, 2, 3, 4], [3, 4, 5, 6]))


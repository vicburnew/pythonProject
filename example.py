# from typing import Union
#
# from untils.hello import hello
#
#
# def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
#     """Функция, которая складывает два числа"""
#     return a + b
#
#
# from untils.add import add
#
# print(add(6, 2))
# help(add)
# help(hello)

import os
# import os.path

# current_directory = os.getcwd()
# print(current_directory)
#
# directory_files = os.listdir("c:/Users/Home/PycharmProjects/pythonProject")
# print(directory_files)

# path_1 = "c:/Users/Home/PycharmProjects/pythonProject"
# path_2 = "test.txt"
#
# joined_path = os.path.join(path_1, path_2)
# print(joined_path)

# path_1 = "c:/Users/Home/PycharmProjects/example.txt"
# dir_name = os.path.dirname(path_1)
# print(dir_name)

# for root, dirs, files in os.walk('c:/Users/Home/PycharmProjects/pythonProject'):
#     for name in files:
#         print(os.path.join(root, name))
#     for name in dirs:
#         print(os.path.join(root, name))

# path = 'c:/Users/Home/PycharmProjects/pythonProject/test.txt'
#
# filename = os.path.basename(path)
# print(filename)

# import os
#
# print(os.name)

import os
# print(os.path.isdir("c:/Users/Home/PycharmProjects/pythonProject"))

# print(os.environ)
# print(os.getenv("ALLUSERSPROFILE"))

# current_directory = os.getcwd()
# print(current_directory)
#
# files = os.listdir(current_directory)
# print(files)

# file = open("test.txt", "r+")
# file.write("heyay ewrwer ")
# content = file.read()
# print(content)
# file.close()

# file = open(".flake8", "r", encoding="utf-8")
# print(file)
# file.close()

# with open(".flake8", "r", encoding="utf-8") as file:
#     print(file)

with open("test.txt", "w", encoding="utf-8") as file:
    file.write("\nhello")
    file.write("\nbuy")

# with open("test.txt", "r", encoding="utf-8") as file:
#     content = file.read()

# print(content)

with open("test.txt", "r+", encoding="utf-8") as file:
    content_2 = file.read()
    # print(content)
    file.write("\nheyy")
    file.write("\nsay")

with open("test.txt", "r", encoding="utf-8") as file:
    content_3 = file.read()

print(content_3)


# students = [
# {'name': 'John', 'age': 23},
# {'name': 'Jane', 'age': 22},
# {'name': 'Mike', 'age': 24},
# ]
#
# with open("students.txt",'w') as file:
#     for student in students:
#         file.write(f"Nane: {student["name"]}, Age: {student["age"]}\n")
#
# with open("log.txt", "w", encoding="utf-8") as file:
#     file.write("log Entry 1\n")
#
# with open("log.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)
#
# with open("log.txt", "a", encoding="utf-8") as file:
#     file.write("log Entry 2\n")
#
# with open("log.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)
#
# with open("shopping_list.txt", "w", encoding="utf-8") as file:
#      file.write("milk\n")
#      file.write("bread\n")
#      file.write("eggs\n")
#
# with open("shopping_list.txt", "r", encoding="utf-8") as file:
#     print(file.read())
#
# with open("shopping_list.txt", "a", encoding="utf-8") as file:
#     file.write("butter\n")
#     file.write("cheese\n")
#
# with open("shopping_list.txt", "r", encoding="utf-8") as file:
#     print(file.read())


# print(base_path)

# full_path = os.path.join(os.path.dirname(__file__), "data", "log.txt")
# with open(full_path, "r") as file:
#     print(file.read())

# 1. Написать функцию, которая получает на вход список чисел и возвращает новый список,
# содержащий только числа, которые меньше среднего значения списка.
# Пример ввода:
# [1, 2, 3, 4, 5]
#
# Пример вывода:
# [1, 2]
# return [number for number in list_of_numbers if number < avg_val]
# def list_below_average(list_of_numbers):
#     avg_val = sum(list_of_numbers) / len(list_of_numbers)
#     # short_list = []
#     # for number in list_of_numbers:
#     #     if number < avg_val:
#     #         short_list.append(number)
#
#     return [x for x in list_of_numbers if x > avg_val]
#
# list = [1,2,3,4,5,6]
# print(list_below_average(list))

# 2. Написать функцию, которая получает на вход список строк и
# возвращает новый список, содержащий только уникальные строки.
# Пример ввода:
# ['apple', 'banana', 'orange', 'apple']
#
# Пример вывода:
# ['apple', 'banana', 'orange']

# def unique_list(list_of_stings):
#     set_1 = set(list_of_stings)
#     list_1 = list(set_1)
#     # for x in list_of_stings:
#     #     set_1.add(x)
#     # list_new = list(set_1)
#     # return list_new
#
#     # return list(set(list_of_stings))
#     return list_1
#
# list_1 = ['apple', 'banana', 'orange', 'apple']
# print(unique_list((list_1)))

# 3. Написать функцию, которая получает на вход список кортежей,
# содержащих информацию о товарах (например, название, цена, количество и т. д.),
# и возвращает новый список, отсортированный по убыванию цены.
# Пример ввода:
# [(apple, 2.5), (banana, 3.5), (orange, 1.5)]
#
# Пример вывода:
# [(banana, 3.5), (apple, 2.5), (orange, 1.5)]
#
# def sorted_list(list_of_goods):
#     new_list = sorted(list_of_goods, reverse=True, key = lambda x: x[1])
#     return new_list
#
# list = [("apple", 2.5), ("banana", 3.5), ("orange", 1.5)]
# print(sorted_list(list))
# # [(banana, 3.5), (apple, 2.5), (orange, 1.5)]

# 4. Написать функцию, которая получает на вход список словарей,
# содержащих информацию о фильмах (например, название, жанр, режиссер и т. д.),
# и возвращает новый список, содержащий только те фильмы, которые
# относятся к заданному жанру.
# Пример ввода:
# [{title: 'The Shawshank Redemption', genre: 'Drama', director: 'Frank Darabont'}, {title: 'The Godfather', genre: 'Crime', director: 'Francis Ford Coppola'}, {title: 'The Dark Knight', genre: 'Action', director: 'Christopher Nolan'}], 'Drama'
#
# Пример вывода:
# [{title: 'The Shawshank Redemption', genre: 'Drama', director: 'Frank Darabont'}]

# def filter_by_genre(list_of_films, my_genre):
#     new_list = [x for x in list_of_films if x["genre"] == my_genre]
#     return new_list
#
#
# print(filter_by_genre([{"title": 'The Shawshank Redemption', "genre": 'Drama', "director": 'Frank Darabont'},
#                        {"title": 'The Godfather', "genre": 'Crime', "director": 'Francis Ford Coppola'},
#                        {"title": 'The Dark Knight', "genre": 'Action', "director": 'Christopher Nolan'}], 'Drama'))
# [{title: 'The Shawshank Redemption', genre: 'Drama', director: 'Frank Darabont'}]

import math


def add_num(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError ("делить на ноль нельзя")
    return a / b

def calc_log(a, b):
    return math.log(a, b)

def calculate_logarithm(number):
    if number <= 0:
        raise ValueError("Логарифм можно вычислить только для положительных чисел")
    return math.log(number)

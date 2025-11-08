from math import sqrt
from typing import Union


def add_numbers(var1: Union[int, float], var2: Union[int, float]):
    return var1 + var2


def calculate_square_root(Number: Union[int, float]):
    return sqrt(Number)


def calc(your_number):
    if your_number <= 0:
        return

    return f"Мы вычислили квадратный корень из введённого вами числа. \
        Это будет: {calculate_square_root(your_number)}"


var1 = 10
var2 = 5

print("Сумма чисел: ", add_numbers(var1, var2))

print(calc(25.5))

from math import sqrt
from typing import Optional, Union


def add_numbers(var1: Union[int, float],
                var2: Union[int, float]) -> Union[int, float]:
    return var1 + var2


def calculate_square_root(number: Union[int, float]) -> float:
    return sqrt(number)


def calc(your_number: Union[int, float]) -> Optional[str]:
    if your_number <= 0:
        return None
    res = calculate_square_root(your_number)
    return (
        'Мы вычислили квадратный корень из введённого вами числа. Это будет:'
        f' {res}'
    )


var1 = 10
var2 = 5

print('Сумма чисел: ', add_numbers(var1, var2))

print(calc(25.5))
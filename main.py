import os
import os.path
from typing import Union

from untils.hello import hello


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Функция, которая складывает два числа"""
    return a + b



from untils.add import add

print(add(6, 2))
help(add)
help(hello)




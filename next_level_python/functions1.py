from typing import Callable
from functools import partial

Numeric = int | float


numbers = [1, 2, 3, 4, 5, 6, 7]

def is_even(num: int) -> bool:
    return num % 2 == 0

def is_greater(val: Numeric, reference: Numeric) -> bool:
    return val > reference


def my_filter(values: list[int], criterion: Callable[[int], bool]) -> None:
    for val in values:
        if criterion(val):
            print(val)


if __name__ == '__main__':
    print('Is even:')
    my_filter(numbers, is_even)
    my_filter(numbers, lambda x: x % 2 == 0)
    
    print('\nGreater than 5:')
    greater_5 = partial(is_greater, reference=5)
    my_filter(numbers, greater_5)
    my_filter(numbers, lambda val: is_greater(val, 5))
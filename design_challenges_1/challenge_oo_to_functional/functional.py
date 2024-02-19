from typing import Collection, Callable
from math import pi


def rectangle_area(a: float, b: float) -> float:
    return a * b

def rectangle_perimeter(a: float, b: float) -> float:
    return 2 * (a + b)



def circle_area(r: float) -> float:
        return pi * r**2

def circle_perimeter(r: float) -> float:
        return 2 * pi * r


def get_total_area(figures: Collection[Collection[float]]) -> float:
    total: float = 0
    for fig in figures:
        if len(fig) == 1:
             total += circle_area(*fig)
        if len(fig) == 2:
             total += rectangle_area(*fig)
    return total

def get_total_perimeter(figures: Collection[Collection[float]]) -> float:
    total: float = 0
    for fig in figures:
        if len(fig) == 1:
             total += circle_perimeter(*fig)
        if len(fig) == 2:
             total += rectangle_perimeter(*fig)
    return total

def calculate_total(*shape_functions: Callable[[], float]):
    return sum([fun() for fun in shape_functions])


def main() -> None:
    total_area = calculate_total(
         lambda: rectangle_area(4., 5.),
         lambda: rectangle_area(3., 3.),
         lambda: circle_area(2.)
    )
    total_perimeter = calculate_total(
         lambda: rectangle_perimeter(4., 5.),
         lambda: rectangle_perimeter(3., 3.),
         lambda: circle_perimeter(2.)
    )
    print("Total Area:", total_area)
    print("Total Perimeter:", total_perimeter)


if __name__ == "__main__":
    main()

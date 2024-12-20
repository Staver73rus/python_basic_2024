"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args: tuple):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    res = [i**2 for i in args]
    return res


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number: int):
    if number in (0, 1):
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


def filter_numbers(lst_data: list, param: str) -> list:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if param == PRIME:
        return list(filter(is_prime, lst_data))
    elif param == ODD:
        return list(filter(lambda x: x % 2 != 0, lst_data))
    return list(filter(lambda x: x % 2 == 0, lst_data))

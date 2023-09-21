"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    if args == None:
        return []
   
    return [x**2 for x in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    if n<2:
        return False
    elif n==2:
        return True
    for i in range(2, n):
        if n%i==0:
            return False
    return True
      
def even(z):
    if z%2==0:
        return True
    elif z%2!=0:
        return False
def odd(d):
    if d%2!=0:
        return True
    elif d%2==0:
        return False   


def filter_numbers(nums, filter_tupe):
     
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
   
    if filter_tupe == EVEN:
       return list(filter (even, nums))
    elif filter_tupe == ODD:
        return list(filter(odd, nums))
    elif filter_tupe == PRIME:
        return list(filter(is_prime, nums))

    
     
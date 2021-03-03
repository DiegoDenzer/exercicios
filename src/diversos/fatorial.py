from functools import reduce
from operator import mul


def fat1(num: int):
    """
    >>> fat1(4)
    24
    >>> fat1(1)
    1
    """
    if num == 1:
        return num;
    fatorial = 1
    for n in reversed(range(num)):
        fatorial = fatorial * (n + 1)

    return fatorial


def fat2(num:int):
    """
        >>> fat2(4)
        24
        >>> fat2(1)
        1
    """
    fatorial = 1
    for n in range(1, num + 1):
        fatorial *= n
    return fatorial

def fat3(num:int):
    """
        >>> fat2(4)
        24
        >>> fat2(1)
        1
    """
    return reduce(mul, range(1, num + 1))
""" Encontrar segundo maior elemento de um interavel de numeros """
from numbers import Number
from typing import List
import bisect


def encontrar_segundo_maior_elemento(ordenada: List) -> Number:
    """
    >>> encontrar_segundo_maior_elemento([1,1,1,1,2,2,2,3,3,3])
    2
    :param ordenada:
    :return:
    """
    index = bisect.bisect_left(ordenada, 2, )
    return 
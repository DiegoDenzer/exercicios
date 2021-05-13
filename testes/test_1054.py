import pytest as pytest

from src.iniciante.exercicio_1054 import tipo_triangulo


def test_nao_forma_triangulo():
    assert 'NAO FORMA TRIANGULO' == tipo_triangulo(sorted([5.0, 2.0, 7.0], reverse=True))
    assert 'TRIANGULO RETANGULO' == tipo_triangulo(sorted([6.0, 8.0, 10.0], reverse=True))
    assert 'TRIANGULO OBTUSANGULO' == tipo_triangulo(sorted([6.0, 6.0, 10.0], reverse=True))
    assert 'TRIANGULO ACUTANGULO' == tipo_triangulo(sorted([7.0, 5.0, 7.0], reverse=True))
    assert 'TRIANGULO EQUILATERO' == tipo_triangulo(sorted([10.0, 10.0, 10.0], reverse=True))
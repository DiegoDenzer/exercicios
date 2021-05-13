"""
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados.
A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos,
 sempre escrevendo uma mensagem adequada:

 RETANGULO = A2**2 = B2**2 + C2**2
    se A2**2 > B2**2 + C2**2, apresente a mensagem: TRIANGULO OBTUSANGULO
    se A2**2 < B2**2 + C2**2, apresente a mensagem: TRIANGULO ACUTANGULO
"""


def somaCatetosAoQuadrado(val1, val2):
    return (val1**2 + val2**2)


def tipo_triangulo(dados):
    a, b, c = dados[0], dados[1], dados[2]
    if a >= (b + c):
        return 'NAO FORMA TRIANGULO'
    elif a == b and a == c and b == c:
        return 'TRIANGULO EQUILATERO'
    elif a == b and a == c or b == c and a == b:
        return 'TRIANGULO ISOSCELES'
    elif a ** 2 == somaCatetosAoQuadrado(b, c):
        return 'TRIANGULO RETANGULO'
    elif a ** 2 > somaCatetosAoQuadrado(b, c):
        return 'TRIANGULO OBTUSANGULO'
    elif a ** 2 < somaCatetosAoQuadrado(b, c):
        return 'TRIANGULO ACUTANGULO'



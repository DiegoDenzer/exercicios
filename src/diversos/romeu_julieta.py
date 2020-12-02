"""

Multiplos de 3 retorna - > Queijo
Multiplos de 5 goiabada -> Goiabada
Multiplos de 3 e 5  -> romeu e julieta


"""


def romeu_julieta(val: int):
    if val % 3 == 0 and val % 5 == 0:
        return 'Romeu e Julieta'
    elif val % 3 == 0:
        return 'Queijo'
    elif val % 5 == 0:
        return 'Goiabada'

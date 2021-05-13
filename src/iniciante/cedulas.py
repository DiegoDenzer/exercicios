"""
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas)
no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1,000,000).

Saída 576.73
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias.

"""
entrada = float(input())

saidas = {
    '100.00': 0,
    '50.00': 0,
    '20.00': 0,
    '10.00': 0,
    '5.00': 0,
    '2.00': 0,
    '1.00': 0,
    '0.50': 0,
    '0.25': 0,
    '0.10': 0,
    '0.05': 0,
    '0.01': 0,
}


def subtrai_valor(key):
    global entrada
    if round(entrada, 2) >= round(float(key), 2):
        saidas[key] = saidas[key] + 1
        entrada -= round(float(key), 2)
        subtrai_valor(key)


def meu_print(i, value, key):
    if i == 0:
        print('NOTAS:')
    if i == 6:
        print('MOEDAS:')

    if float(key) > 1:
       tipo = "nota"
    else:
       tipo = "moeda"
    print(f'{value} {tipo}(s) de R$ {key}')


[subtrai_valor(key) for key in saidas.keys()]
[meu_print(i, tuple[1], tuple[0]) for i, tuple in enumerate(saidas.items())]

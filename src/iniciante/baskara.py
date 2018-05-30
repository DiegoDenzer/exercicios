"""Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara.
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”,
caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes,
apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto,
com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem."""

#Formula dalta = b² - 4.a.c
#-b raiz delta sobre 2*a
#10.0 20.1 5.1
#R1 = -0.29788   -1.71212
#0.0 20.0 5.0
#10.3 203.0 5.0
#10.0 3.0 5.0

entrada = input().split()
t = ([float(i) for i in entrada])
if t[0] == 0:
    print("Impossivel calcular")
else:
    delta = (t[1] ** 2) - (4*t[0]*t[2])
    if delta < 0:
        print("Impossivel calcular")
    else:
        raiz_delta = delta ** (1/2)
        x = t[1]*(-1)
        baixo = 2 * t[0]
        x = x + raiz_delta
        r1 = x / baixo
        x = t[1]*(-1)
        x = x - raiz_delta
        r2 = x / baixo

        print("R1 = {:.5f}".format(r1))
        print("R2 = {:.5f}".format(r2))

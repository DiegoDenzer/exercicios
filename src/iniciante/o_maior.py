"""
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.
Utilize a fórmula:

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

"""
valores = input().split()
v = ([int(i) for i in valores])
v1 = ([abs(a) for a in v])
print("{} eh o maior".format(max(v1)))

"""
Leia a hora inicial e a hora final de um jogo.
A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro,
tendo uma duração mínima de 1 hora e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo.
16 2 10
"""

entrada = input().split()
num = ([int(numero) for numero in entrada])
horas = 0
# Verifica se já passou do meio dia
if num[0] >= 12:
    for h in range(num[0], 24):
        horas += 1
    for h in range(0, num[1]):
        horas += 1
else:
    for h in range(num[0], num[1]):
        horas += 1
print("O JOGO DUROU {} HORA(S)".format(horas))
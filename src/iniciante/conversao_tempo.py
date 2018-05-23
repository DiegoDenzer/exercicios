"""
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica,
e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:
minutos:segundos, conforme exemplo fornecido. 556 0:9:16
"""
segundos = int(input())
dias = segundos // 86400
horas = segundos // 3600
segundos_rest = segundos % 3600
minutos = segundos_rest // 60
segundos_rest = segundos_rest % 60

print("{}:{}:{}".format(horas,minutos, segundos_rest))
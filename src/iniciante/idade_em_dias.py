"""
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias
Obs.: apenas para facilitar o cálculo, considere
ano com 365 dias e  mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias,
como 360, 363 ou 364.
Este é apenas um exercício com objetivo de testar raciocínio matemático simples.
Entrada

O arquivo de entrada contém um valor inteiro.

Saída
Imprima a saída conforme exemplo fornecido
1 ano(s)
1 mes(es)
5 dia(s)
"""
entrada = int(input())
ano = 0
mes = 0
dia = 0

while entrada != 0:
    if entrada >= 365:
        ano += 1
        entrada -= 365
    if 365 > entrada >= 30:
        mes += 1
        entrada -= 30
    if 30 > entrada >= 1:
        dia += 1
        entrada -= 1

print("{} ano(s)".format(ano))
print("{} mes(es)".format(mes))
print("{} dia(s)".format(dia))

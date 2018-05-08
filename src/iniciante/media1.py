"""Leia 2 valores de ponto flutuante de dupla precisão A e B,
 que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno,
 sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5
 (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
"""
#media 
a = float(input())
b = float(input())
print('MEDIA = {:4.5f}'.format((a * 3.5 + b * 7.5) / 11))

a = float(input())
b = float(input())
c = float(input())
a = a * 2
b = b * 3
c = c * 5
div = a+b+c
di = 2+3+5
print('MEDIA = {:2.1f}'.format(div/di))


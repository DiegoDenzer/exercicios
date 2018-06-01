"""
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo.
Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

Perimetro = XX.X    6.0 4.0 2.1 Perimetro = 12.1

Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem

Area = XX.X         6.0 4.0 2.0   Area = 10.0

A é menor que a SOMA de B + C e B é menor que a SOMA de A + C e C é menor que a SOMA de A + B

"""
entrada = input().split()
teste = ([float(numero) for numero in entrada])

if teste[0] < teste[1]+teste[2] and teste[1] < teste[0]+teste[2] and teste[2] < teste[0]+teste[1]:
    print("Perimetro = {:.1f}".format(teste[0]+teste[1]+teste[2]))
else:
    soma = (teste[0]+teste[1])
    print("Area = {:.1f}".format((soma * teste[2]) / 2))
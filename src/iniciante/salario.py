""" Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas,
 o valor que recebe por hora e calcula o salário desse funcionário. A seguir,
 mostre o número e o salário do funcionário, com duas casas decimais.

Entrada
O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais,
representando o número, quantidade de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada,
respectivamente.

Saída
Imprima o número e o salário do funcionário, conforme exemplo fornecido,
com um espaço em branco antes e depois da igualdade. No caso do salário,
também deve haver um espaço em branco após o $. """


#Calcula Salario Usando uma Função
def calcula_salario(n_f, horas, valor):
    print("NUMBER = {}".format(n_f))
    print("SALARY = U$ {:4.2f}".format(horas * valor))


numero_funcionario = int(input())
horas = int(input())
valor_hora = float(input())
calcula_salario(numero_funcionario, horas, valor_hora)
"""
Cada trem que chega na direção A é manobrado e seus vagões continuam na direção B, reorganizados conforme o chefe da
estação deseja. Ao chegar pelo lado A, cada vagão é desconectado e vai até a estação e depois segue para a direção B,
para ser conectado na segunda locomotiva. Você pode desconectar quantos trens deseja na estação,
 mas o vagão que entra na estação só pode sair pelo lado B e uma vez que ele sai, não pode mais entrar novamente.

Todos vagões são identificados pelas letras minúsculas (a até z).
Isto significa 26 vagões no máximo. O chefe da organização dos vagões precisa agora que você ajude a resolver para ele,
através de um programa, qual a sequência de movimentos é necessária para obter a saída desejada após a entrada na
estação, seguindo para a direção B. O movimento de entrada e saída da estação é descrito
respectivamente pelas letras I e R (Insere e Remove). Utilizando a figura dada como exemplo, a entrada e,t,d,a para
uma saída desejada d,a,t,e, resulta nos movimentos I,I,I,R,I,R,R,R

Entrada
A entrada consiste em vários casos de teste, onde cada caso de teste é composto por 3 linhas. A primeira das 3 linhas
contém um número inteiro N que representa o número total de vagões. A segunda linha contém a sequência dos vagões que
vêm do lado A e a Terceira linha contém a sequência que o chefe de organização deseja como saída para o lado B.
A última linha de entrada contém apenas 0, indicando o fim da entrada.

Saída
O arquivo de saída contém a quantidade de linhas correspondente ao número de casos de teste de entrada.
Cada linha de saída contém uma sequência de I e R conforme o exemplo. Se não for possível mostrar a saída,
as operações devem ser interrompidas e a mensagem "Impossible" deve ser impressa, com um espaço após a sequência.
4
e t d a
d a t IIIRIRRR

o s t a p
patos
"""
pos_trem = 0
patio = []
saida = []
log = []


def colocar_trem():
    global pos_trem, patio, saida, log

    if len(patio) > 0 and saida[pos_trem] == patio[-1]:
        patio.pop()
        log.append('R')
        pos_trem += 1
        if len(saida) >= pos_trem:
            colocar_trem()


def manobrar(entrada):
    global pos_trem, patio, saida, log

    patio = []
    log = []
    for i, e in enumerate(entrada):

        patio.append(e)
        log.append('I')

        colocar_trem()
    if len(patio) > 0:
        log.append(' Impossible')
    print(''.join(map(str, log)))


def iniciar():
    global pos_trem, patio, saida, log
    t = int(input())
    lista = []
    while t != 0:
        if 26 >= t > 0:
            e = str(input())
            entrada = list(e.lower())[:t]
            print(entrada)
            s = str(input())
            saida = list(s.lower())[:t]
            print(saida)
            lista.append((entrada, saida))
        t = int(input())

    for tupla in lista:
        pos_trem = 0
        saida = tupla[1]
        manobrar(tupla[0])


iniciar()
print('\n')




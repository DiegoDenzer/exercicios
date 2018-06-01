"""
Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno.
Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ".
Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.".
Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.".
Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".

No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno.
Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada.
Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2).
e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos).
Para estes dois casos (aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem
"Media final: " seguido da média final para esse aluno.

Entrada
A entrada contém quatro números de ponto flutuante correspendentes as notas dos alunos.

Saída
Todas as respostas devem ser apresentadas com uma casa decimal. As mensagens devem ser impressas conforme a descrição do problema.
Não esqueça de imprimir o enter após o final de cada linha.

"""
entrada = input().split()
notas = ([float(i) for i in entrada])
media = (notas[0] * 2) + (notas[1] * 3) + (notas[2] * 4) + (notas[3] * 1)
media = media / 10
if media < 5.0:
    print('Media: {:.1f}'.format(media))
    print('Aluno reprovado.')
elif 5 <= media <= 6.9:
    print('Media: {:.1f}'.format(media))
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame: {:.1f}'.format(exame))
    final = (media + exame) / 2
    if final >= 5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(final))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(final))
else:
    print('Media: {:.1f}'.format(media))
    print('Aluno aprovado.')

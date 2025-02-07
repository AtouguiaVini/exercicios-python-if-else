# Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:

# Média >= 7: Aprovado
# 5 <= Média < 7: Recuperação
# Média < 5: Reprovado
# Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.

media_reprovado = 5
media_aprovado = 7

try:
    nota_1 = float(input('Digite aqui a primeira nota: '))
    nota_2 = float(input('Digite aqui a segunda nota: '))
    nota_3 = float(input('Digite aqui a terceira nota: '))

    media = (nota_1 + nota_2 + nota_3)/3

    print(f'A média da nota do aluno é: {media:.2f}')

    if media < media_reprovado:
        print('Aluno reprovado!')
    elif media_aprovado > media >= media_reprovado:
        print('Aluno em recuperação!')
    else:
        print('Aluno aprovado!')
          
except:
    print('Valor da nota inválido')
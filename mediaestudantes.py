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
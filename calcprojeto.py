try:
    a = int(input('Informe os dias para a atividade A: '))
    b = int(input('Informe os dias para a atividade B: '))
    c = int(input('Informe os dias para a atividade C: '))
    if a < 0 or b < 0 or c < 0:
        print('Número inserido negativo, por favor tente novamente')

    else:
        soma = a+b+c
        print(f'A quantidade de dias para as atividades serem concluídas são {soma} dias!')
except:
    print('Não informado um número')
def desempenho_vendas():
    try:
        maças = int(input('Digite a quantidade de maçâs vendidas: '))
        bananas = int(input('Digite a quantidade de maçâs vendidas: '))

        if maças > bananas:
            print('As maçãs tiveram mais vendas!')
        elif bananas > maças:
            print('As bananas tiveram mais vendas!')
        else:
            print('As maçãs e as bananas tiveram a mesma quantidade de vendas!')
    except:
        print('O valor informado não é um valor correto. Tente novamente!')
        return

desempenho_vendas()
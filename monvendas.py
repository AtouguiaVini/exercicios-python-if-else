# Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.

# Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.



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
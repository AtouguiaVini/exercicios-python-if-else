renda_limite = 2000
percentual_parcela = 30


try:
    renda_mensal = float(input('Digite sua renda mensal: R$ '))
    parcela_desejada = float(input('Digite a parcela desejável para pagamento: R$ '))
    parcela_possivel = (renda_mensal * percentual_parcela)/100

    if renda_mensal > renda_limite and (parcela_desejada / renda_mensal) * 100 <= percentual_parcela :
        print('Empréstimo aprovado!')

    elif renda_mensal <= renda_limite:
        print('Empréstimo negado: renda insuficiente')
        print(f'O valor mínimo de renda mensal é de R$ {renda_limite:.2f}')
    else:
        print(f'Empréstimo negado: Parcela acima de {percentual_parcela}% da renda')
        print(f'Valor máximo da parcela: R$ {parcela_possivel:.2f}')


except:
    print('Valor informado incorreto. Tente novamente')

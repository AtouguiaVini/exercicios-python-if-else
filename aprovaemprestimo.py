# Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:

# O valor da renda mensal precisa ser maior que R$ 2.000,00.
# O valor da parcela não pode ultrapassar 30% da renda.
# Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.

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

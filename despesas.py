valor_limite = 3000.00
try:
    despesas = float(input('Digite o valor de despesas (R$): '))

    if despesas > valor_limite:
        print('O valor de despesas é maior que o valor limite para gastos!')
    else:
        print('O valor de despesas está dentro do valor limite para gastos!')

except:
    print('O valor informado não é um valor válido! Tente novamente')
# Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.

valor_limite = 3000.00
try:
    despesas = float(input('Digite o valor de despesas (R$): '))

    if despesas > valor_limite:
        print('O valor de despesas é maior que o valor limite para gastos!')
    else:
        print('O valor de despesas está dentro do valor limite para gastos!')

except:
    print('O valor informado não é um valor válido! Tente novamente')
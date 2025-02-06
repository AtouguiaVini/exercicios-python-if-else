imc_minimo = 18.5
imc_maximo = 25

try:
    peso = float(input('Digite seu peso (kg): '))
    altura = float(input('Digite sua altura (m): '))
    imc = peso/(altura ** 2)

    print(f'seu IMC é: {imc:.2f}')

    if imc < imc_minimo:
        print('Você está abaixo do peso!')
    elif imc > imc_maximo:
        print('Você está acima do peso!')
    else:
        print('Você está no peso ideal!')

except:
    print('Não é um valor válido, por favor tente novamente!')

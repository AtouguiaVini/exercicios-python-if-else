numero = int(input('Digite um número inteiro: '))

try:
    if numero % 2 == 0:
        print(f'O número {numero} é par!')
    else:
        print('O número é impar!')
except: print('Número informado inválido!')
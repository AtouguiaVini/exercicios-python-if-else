# Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. O valor do pedágio depende da distância percorrida:

# Até 100 km: R$ 10,00
# Entre 100 km e 200 km: R$ 20,00
# Acima de 200 km: R$ 30,00
# Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.


km_primeiro = 100
km_segundo = 200

pedagio_1 = 10
pedagio_2 = 20
pedagio_3 = 30


try:
    distancia_percorrida = float(input('Digite a distância percorrida (km): '))
    print(f'A distância percorrida é de {distancia_percorrida:.2f} km')
    
    if distancia_percorrida <= km_primeiro:
        print(f'O valor do pedágio é de R$ {pedagio_1:.2f}')
    elif distancia_percorrida > km_segundo:
        print(f'O valor do pedágio é de R$ {pedagio_3:.2f}')
    else:
        print(f'O valor do pedágio é de R$ {pedagio_2:.2f}')

except: print('Valor informado errado!')
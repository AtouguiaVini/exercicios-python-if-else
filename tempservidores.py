temp_maxima = 25

try:
    temp_atual = int(input('A temperatura atual é(°C): '))
    
    if temp_atual > temp_maxima:
        print('Alerta! Nivel da temperatura excedeu o limite aceitável!')
    elif temp_atual == temp_maxima:
        print('Nivel de temperatura atingiu seu limite! Por favor, verifique comprometimento!')
    else:
        print('Temperatura aceitável! Sem comprometimento identificado')
except:
    print('Não identificado valor informado. Por favor, tente novamente.')
# Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

temp_maxima = 25

try:
    temp_atual = float(input('A temperatura atual é(°C): '))
    
    if temp_atual > temp_maxima:
        print('Alerta! Nivel da temperatura excedeu o limite aceitável!')
    elif temp_atual == temp_maxima:
        print('Nivel de temperatura atingiu seu limite! Por favor, verifique comprometimento!')
    else:
        print('Temperatura aceitável! Sem comprometimento identificado')
except:
    print('Não identificado valor informado. Por favor, tente novamente.')
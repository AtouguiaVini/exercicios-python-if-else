hr_inicial = 8 
hr_final = 18

try:
    hr_entrada = int(input('Digite aqui a hora atual (24h): '))
    
    if hr_inicial <= hr_entrada < hr_final:
        print('Acesso permitido!')
    else: print('Acesso negado!')
except:
    print('Valor incorreto')
        
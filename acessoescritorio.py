# Mariana é responsável por liberar o acesso ao escritório e precisa de um programa que verifique se os funcionários podem entrar. Para isso, ela usará o horário atual. O escritório só permite acesso entre 8h e 18h. Crie um programa que receba a hora atual como entrada (em formato de 24 horas) e exiba uma mensagem informando se o acesso é permitido ou negado.

hr_inicial = 8 
hr_final = 18

try:
    hr_entrada = int(input('Digite aqui a hora atual (24h): '))
    
    if hr_inicial <= hr_entrada < hr_final:
        print('Acesso permitido!')
    else: print('Acesso negado!')
except:
    print('Valor incorreto')
        
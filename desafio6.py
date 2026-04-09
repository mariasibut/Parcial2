# Exibe o título do desafio
print(' DESAFIO 6 - CONVERSÃO DE TEMPO ')

# Escolha do tipo de conversão
op = input('1: Segundos -> h/m/s | 2: h/m/s -> Segundos: ')

if op == '1':
    # Entrada: total em segundos
    s = int(input('Digite os segundos: '))
    
    # Conversão usando divisão inteira e resto
    h = s // 3600
    m = (s % 3600) // 60
    s = s % 60
    
    # Saída
    print(f'{h}h {m}m {s}s')

elif op == '2':
    # Entrada: horas, minutos e segundos
    h = int(input('Horas: '))
    m = int(input('Minutos: '))
    s = int(input('Segundos: '))
    
    # Soma tudo em segundos
    total = h*3600 + m*60 + s
    
    # Saída
    print('Total em segundos:', total)

else:
    # Caso inválido
    print('Opção inválida!')

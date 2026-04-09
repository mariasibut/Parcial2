# Exibe o título 
print(' DESAFIO 7 - CÁLCULO DE JUROS SIMPLES ')

# Entrada de dados
C = float(input('Digite o capital (C): '))
I = float(input('Digite a taxa (%): '))
T = float(input('Digite o tempo: '))

# Pergunta o tipo da taxa
tipo = input('A taxa é ao mês (m) ou ao ano (a)? ')

# Conversão do tempo
if tipo == 'a':
    unidade = input('O tempo está em meses (m) ou anos (a)? ')
    if unidade == 'm':
        T = T / 12
else:
    unidade = input('O tempo está em meses (m) ou anos (a)? ')
    if unidade == 'a':
        T = T * 12

# Cálculo
J = (C * I * T) / 100

# Saída
print('Juros calculados:', J)

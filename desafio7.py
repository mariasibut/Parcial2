# Exibe o título 
print(' DESAFIO 7 - CÁLCULO DE JUROS SIMPLES ')

# Entrada de dados: capital, taxa e tempo
C = float(input('Digite o capital (C): '))
I = float(input('Digite a taxa (%): '))
T = float(input('Digite o tempo: '))

# Processamento: usa a fórmula J = (C * I * T) / 100
J = (C * I * T) / 100

# Saída de dados
print('Juros calculados:', J)

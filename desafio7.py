# ===== DESAFIO - JUROS SIMPLES =====

print('===== CÁLCULO DE JUROS SIMPLES =====')

# Entrada de dados: capital, taxa e tempo
C = float(input('Digite o capital (C): '))
I = float(input('Digite a taxa (%): '))
T = float(input('Digite o tempo: '))

# Processamento: aplica a fórmula J = (C * I * T) / 100
J = (C * I * T) / 100

# Saída de dados
print('Juros calculados:', J)

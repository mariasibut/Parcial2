# Mostra o título
print('DESAFIO 02 - VERIFICANDO NÚMERO PAR ')

# Pede para o usuário digitar um número = int(input('Digite um número: '))

# Verifica se o número é par
# O operador % calcula o resto da divisão
# Se o resto da divisão por 2 for 0, significa que o número é par
if numero % 2 == 0:
    print('O número {} é PAR'.format(numero))
else:
    # Caso o resto não seja 0, então o número é ímpar
    print('O número {} é ÍMPAR'.format(numero))

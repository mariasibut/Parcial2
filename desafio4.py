# ===== DESAFIO - CALCULADORA SIMPLES =====

# Exibe um título na tela
print('===== CALCULADORA SIMPLES =====')

# Solicita que o usuário digite o primeiro número
n1 = float(input('Digite o primeiro valor: '))

# Solicita que o usuário digite o segundo número
n2 = float(input('Digite o segundo valor: '))

# Solicita que o usuário escolha a operação desejada
op = input('Escolha a operação (+, -, *, /): ')

# Verifica qual operação foi escolhida e realiza o cálculo
if op == '+':
    resultado = n1 + n2  # Soma os valores

elif op == '-':
    resultado = n1 - n2  # Subtrai os valores

elif op == '*':
    resultado = n1 * n2  # Multiplica os valores

elif op == '/':
    # Verifica se o segundo número é zero antes de dividir
    if n2 != 0:
        resultado = n1 / n2  # Divide os valores
    else:
        resultado = None
        print('Erro: divisão por zero não é permitida!')

else:
    resultado = None  # Caso a operação seja inválida

# Exibe o resultado apenas se for válido
if resultado is not None:
    print('O resultado é:', resultado)

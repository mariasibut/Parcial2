# ===== DESAFIO - CONVERSÃO DE TEMPO =====

# Exibe o título do desafio
print('===== DESAFIO - CONVERSÃO DE TEMPO =====')

# Entrada de dados: o usuário escolhe o tipo de conversão
print('Escolha o tipo de conversão:')
print('1 - Converter segundos para horas, minutos e segundos')
print('2 - Converter horas, minutos e segundos para segundos')

opcao = input('Digite 1 ou 2: ')

# Estrutura condicional para decidir qual cálculo será feito
if opcao == '1':
    # Usuário informa o total de segundos
    total_segundos = int(input('Digite o total de segundos: '))
    
    # Processamento:
    # Calcula quantas horas existem no total de segundos
    horas = total_segundos // 3600
    
    # Calcula o restante após retirar as horas
    resto = total_segundos % 3600
    
    # Calcula quantos minutos existem no restante
    minutos = resto // 60
    
    # O que sobra são os segundos finais
    segundos = resto % 60
    
    # Saída de dados
    print('Resultado da conversão:')
    print(horas, 'hora(s),', minutos, 'minuto(s) e', segundos, 'segundo(s)')

elif opcao == '2':
    # Usuário informa horas, minutos e segundos separadamente
    horas = int(input('Digite as horas: '))
    minutos = int(input('Digite os minutos: '))
    segundos = int(input('Digite os segundos: '))
    
    # Processamento:
    # Converte tudo para segundos
    total_segundos = (horas * 3600) + (minutos * 60) + segundos
    
    # Saída de dados
    print('O total em segundos é:', total_segundos)

else:
    # Caso o usuário digite uma opção inválida
    print('Opção inválida! Por favor, execute o programa novamente.')

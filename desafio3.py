# Exibe o título 
print(' DESAFIO 03 - LISTAR 5 NOMES E IMPRIMIR ')

# Cria uma lista vazia para armazenar os nomes
nomes = []

# Entrada de dados: pede que o usuário digite 5 nomes
for i in range(5):
    nome = input(f'Digite o {i+1}º nome: ')
    nomes.append(nome)  # Adiciona o nome à lista

# Saída de dados: imprime cada nome separadamente
print('Nomes digitados:')

for nome in nomes:
    print(nome)

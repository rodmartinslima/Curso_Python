'''
  enumerate - enumera iteráveis (índices)

'''

lista_nomes = ['Rodrigo', 'Ana', 'Luna']
lista_nomes.append('Sofia')
lista_nomes.append('Cida')

print(50 * '=')
lista_enumerada = enumerate(lista_nomes) 
print(next(lista_enumerada))

print(50 * '=')
print('Para pegar todos os dados é necessário utilizar o for')
for nome in lista_enumerada:
    print(nome)

print(50 * '=')
print('Obter o índice e valor')
for indice, valor in enumerate(lista_nomes):
  print(indice, valor)

print(50 * '=')
print('Após a finalização do for os dados da variável lista_enumerada são consumidos.')
print(lista_enumerada)

print(50 * '=')
print('A forma correta para evitar o consumo é realizar o for quantas vezes necessária')
for itens in enumerate(lista_nomes):
    print(itens)

print(50 * '=')

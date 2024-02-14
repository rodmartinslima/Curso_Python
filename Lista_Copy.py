lista_nomes = ['Rodrigo', 'Martins', 'de', 'Lima']

lista_nomes2 = lista_nomes #isso não faz cópia e sim referência na memória
lista_nomes[0] = 'TESTE'
print(lista_nomes2)

# forma correta de copiar uma lista

lista_nomes_a = ['Rodrigo', 'Martins', 'Lima']
lista_nomes_b = lista_nomes_a.copy()
lista_nomes_a[0] = 'Mudei'
print(lista_nomes_b)
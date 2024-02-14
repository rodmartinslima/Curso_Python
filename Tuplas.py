#Tupla é um tipo de lista imutável

times = 'Corinthians', 'Barcelona', 'Arsenal', 'Borussia Dortmund'
print(type(times), times)

#mudar uma tupla para lista
list_times = list(times)
print(type(list_times), list_times)

#mudar uma lista para tupla
valores = ['1', '2', '3']
valores_tupla = tuple(valores)

#Se tentar adicionar/Alterar um valor ocorre erro
#times[2] = 'Liverpool'
#print(times)
#identidade de um objeto na memória

a = 'a'
print(id(a))

'''
O python busca otimizar o consumo de memória, abaixo um exemplo de duas variáveis diferentes
porém com mesmo ID pois o python entende que por ser uma informação do mesmo tipo não precisa 
ocupar um espaço de memória diferente
'''

b = 'aaa' #esse valor terá um id diferente dos demais abaixo
c = 'AAA'
d = 'AAA'

print(id(b))
print(id(c))
print(id(d))

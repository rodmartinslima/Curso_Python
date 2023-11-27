#Fatiar strings com a função Len

nome = 'Rodrigo Martins de Lima'

print(nome[3:9]) #Pegando trecho dd índice 3 até o 9
print(nome[3:len(nome):1]) #Pegando trecho do índice 3 até o tamnho máximo da string, pegando de 1 em 1
print(nome[0:len(nome):1]) #Pegando trecho do índice 0 até o tamnho máximo da string, pegando de 1 em 1
print(nome[0:len(nome):3]) #Pegando trecho do índice 0 até o tamnho máximo da string, pegando de 3 em 3
print(nome[::-1]) #Nome invertido
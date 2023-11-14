#Exercício 

#Criei um array para pegar dados de uma pessoa, replace na vígula antes de transformar em float
# 
#  
from datetime import date

dados_pessoa = ['nome', 'sobrenome', 'idade', 'ano_nascimento', 'altura']

dados_pessoa[0] = str(input('Digite o seu nome : \n'))
dados_pessoa[1] = str(input('Digite o seu sobrenome : '))
dados_pessoa[2] = int(input('Digite a sua idade : '))
dados_pessoa[3] = int(input('Digite o ano de nascimento : '))
dados_pessoa[4] = float(input('Digite a sua altura : ').replace(',','.'))
ano = date.today().year

print()
print('========================================================')
print('Nome: ', dados_pessoa[0])
print('Sobrenome: ', dados_pessoa[1])

if int(ano) - dados_pessoa[3] != dados_pessoa[2]:
    print('atenção!! A idade informada está errada ou o ano de nascimento está errado')
    print('Ano nascimento informado: ', dados_pessoa[3])
    print('Idade informada: ', dados_pessoa[2])
    print('Idade esperada: ', int(ano) - dados_pessoa[3])
    print('Maior de idade: ', (int(ano) - dados_pessoa[3]) >= 18)
else:
    print('Idade: ', dados_pessoa[2])
    print('Ano de Nascimento:', dados_pessoa[3])
    print('Maior de idade: ', dados_pessoa[2] >= 18)

print('Altura (m):',dados_pessoa[4])
print('========================================================')
#Exercício
# Peça para o usuário digitar o nome dele
# Peça para o usuário digitar a idade dele
# Se o nome e idade forem digitados exibir:
#           Seu nome é {nome}
#           Seu nome invertido é
#           Se contém espaços no nome
#           Quantidade de letras
#           A primeira letra
#           A última letra
# Se nada for digitado no nome ou idade exibir uma mensagem

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if nome == '' or idade == '':
    print('Desculpe, você não informou todos os dados')
else:
    print(f'O seu nome é: {nome}')
    print(f'O seu nome invertido é: {nome[::-1]}')
    print(f'O seu nome {nome} tem espaços? ',  " " in nome)
    print(f'O seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[len(nome) - 1]}')

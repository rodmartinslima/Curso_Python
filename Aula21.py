#Operadores in e not in

nome = 'Rodrigo'

print('Rod' in nome)
print('rig' in nome)
print('abc' not in nome)
print('ana' in nome)
print('Rod' not in nome)
print('=' * 15)

numero_sorte = ['19', '12', '35', '7']

procurar = input('Qual número deseja informar? ')

if procurar in numero_sorte:
    print(f'{procurar} é um número da sorte')
else:    
    print(f'{procurar} não é um número da sorte')
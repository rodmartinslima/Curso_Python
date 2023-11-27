#Formatação de strings com f-strings

# s - strng
# f - float
# n - int
# x ou X para hexadecimal

# > Preenche na esquerda
# < Preenche na direta
# ^ Centraliza

print('Exemplos')
variavel = 'RODRIGO'
print(f'{variavel}') #Normal
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10} -')
print(f'{variavel}') #Normal

print('É possível preencher os espaços vazios com quaisquer caracteres')
print(f'{variavel}') #Normal
print(f'{variavel:|>50}')
print(f'{variavel:|<50}')
print(f'{variavel:|^50} -')

#Formatação de valores
print(f'{19275.19535:.2f}') #Formatando o valor com duas casas decimais
print(f'{19275.19535:,.2f}') #Possível definir para exibir a vírgula
print(f'{19275.19535:+.2f}') #Possível exibir o sinal de mais em valores positivos

#Valor hexadecimal
print(f'O valor Hexadecimal de 1500 é {1500:08x}') #Valor com 8 casas decimais "08" antes do x ou X
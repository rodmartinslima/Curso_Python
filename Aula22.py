#Interpolação básica de strings
# siglas após a %
# s para Strings
# i e d para int
# f para float
# x e X para hexadecimal

nome = 'Rodrigo'
preco = 12.988452
texto = '%s, o preço do produto é R$%.2f' %(nome, preco)
print(texto)

valor = 19
hexa = 19
print('O valor: %i é representado pelo hexadecimal: %08x' %(valor, hexa))
print('O valor: %i é representado pelo hexadecimal: %08x' %(1200, 1200))
print('O valor: %i é representado pelo hexadecimal: %08x' %(195000, 195000))
#%0 e qtde de dígitos, exeplo %08 ou %04
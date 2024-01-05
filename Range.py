#Exemplo de utilização da função range do python > range(start, stop, step)

'''  
    O código abaixo irá mostrar todos os números mútiplos do valor selecionado
    pelo usuário.

'''
stop = int(input('Informe o valor final : '))
step = int(input('Informe o múltiplo : '))

numeros = range(0, stop + 1, step)

print(10 * ' = ')
print(f'Os múltiplos de {step} entre 0 e {stop} são...')

for numero in numeros:
    print(numero)


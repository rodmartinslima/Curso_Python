#Operadores lógicos
#AND (e)

#Valor considerados falsos em variáveis: 0, 0.00 e string vazia > ' '

valor01 = input('informe um valor : ')
valor02 = input('Informe outro valor : ')

valor01_numerico = float(valor01)
valor02_numerico = float(valor02)

if valor01_numerico > 0 and valor02_numerico > 0:
    print('Validando dados...')

    if valor01_numerico > valor02_numerico:
        print(f'O primeiro valor informado: {valor01_numerico} é maior do que o segundo valor informado {valor02_numerico}')
    elif valor01_numerico == valor02_numerico:
        print(f'Valores iguais: {valor01_numerico} = {valor02_numerico}')
    else:
        print(f'O primeiro valor informado: {valor01_numerico} é menor do que o segundo valor informado {valor02_numerico}')
else:
    print(f'Os valores informados são inválidos: {valor01_numerico} e {valor02_numerico}')
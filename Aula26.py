#Exemplo de try except

valor_digitado = input('Informe um valor númérico: ')

try:
    valor_float = float(valor_digitado)
    print(f'O valor informado foi: {valor_float}')
except:
    print('O valor informado não é númérico.')
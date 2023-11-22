#Exercício com validação (if - else) e operadores de comparação

valor1 = input('Informe o primeiro valor: ')
valor2 = input('Informe o outro valor: ')

maior = float(valor1) > float(valor2)
igual = float(valor1) == float(valor2)

print('=' * 20)
print(f'Valor 01 : {valor1}')
print(f'Valor 02 : {valor2}')
print('=' * 20)

if maior:
    print('O primeiro valor é MAIOR do que o segundo valor digitado.')
else:
    if igual:
        print('Os valores informados são iguais.')
    else:
        print('O primeiro valor é MENOR do que o segundo valor digitado.')
# Calculadora que recebe os numeros e operadores desejados pelo usuário

while True:
    num1 = input('Informe o primeiro valor : ')
    num2 = input('Informe o segundo valor valor : ')
    operador = input('Informe um dos opeadores  (+-*/) : ')

    num1_float = 0
    num2_float = 0
    operadores_validos = '+-*/'
    try:
        num1_float = float(num1)
        num2_float = float(num2)
    except:
        print('Um dos valores informados é inválido')
        continue

    if len(operador) > 1:
        print('Informe apenas um operador')
        continue

    if operador not in operadores_validos:
        print('Nenhum operador válido informado')
        continue
    
    if (operador == '/') and (num2_float == 0):
        print('Divisão por zero é inválida!')
        continue

    print('Calculando valores...')    
    if operador == '+':
        print(f'{num1_float}+{num2_float} = ', num1_float + num2_float)
    elif operador == '-':
        print(f'{num1_float}-{num2_float} = ', num1_float - num2_float)
    elif operador == '*':
        print(f'{num1_float}*{num2_float} = ', num1_float * num2_float)
    elif operador == '/':
        print(f'{num1_float}/{num2_float} = ', num1_float / num2_float)

    sair = input('Deseja (s)air? ').lower().startswith('s')

    if sair:
        print('Calculadora encerrada')
        break
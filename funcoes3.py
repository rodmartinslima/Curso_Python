# Calculadora para demonstrar o uso de funções 

def Calculadora():
    calcular = True
    operadores_validos = ['+', '-', '/', '*']

    def Somar(a, b):
        return (f'O resultado da soma de {a} + {b} é : {a+b}')

    def Subtrair(a, b):
        return (f'O resultado da subtração de {a} - {b} é : {a-b}')

    def Dividir(a, b):
        return (f'O resultado da divisão de {a} por {b} é : {a/b}')

    def Multiplicar(a, b):
        return (f'O resultado da multiplicação de {a} * {b} é : {a*b}')

    print('*** INICIANDO CALCULADORA *** \n')
    while calcular:        
        operador = input(' Soma(+) | Subtração(-) | Divisão(/) | Multiplicação(*) : ')

        if operador.strip() == '':
            print('Operador Inválido')

        if operador in operadores_validos:
            
            valor1 = int(input('Informe o primeiro valor: '))
            valor2 = int(input('Informe o segundo valor: '))
            
            if operador == '+':
                print(Somar(valor1, valor2))
            elif operador == '-':
                print(Subtrair(valor1, valor2))
            elif operador == '/':
                if valor2 == 0:
                    print('A T E N Ç Ã O!! Não é possível dividir por zero')
                    print(f'Primeiro valor: {valor1} |  Segundo Valor {valor2}.')
                else:
                    print(Dividir(valor1, valor2))    
            elif operador == '*':
                print(Multiplicar(valor1, valor2))

            sair = input('Deseja sair? (S/N)') 
            if sair == 's' or sair =='S':
                calcular == False                   
                break
Calculadora()
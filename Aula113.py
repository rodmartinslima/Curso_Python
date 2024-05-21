#1 - Criar uma funçãoq ue recebe diversos números e multiple todos os argumentos

def criarseparador(nvezes):
    return print(nvezes*'=')


def multiplicar(*args):
    
    criarseparador(20)
    print(args)
    criarseparador(20)

    total = 1
    numero_anterior = 1

    for numero in args:
        if numero == 0:
            print(f'Voce informou o valor {numero}, ele será desconsiderado no cálculo')
            continue
        else:
            total *= numero
            print(f'{numero_anterior} x {numero} = {total}')
            numero_anterior = total
    
    criarseparador(20)
    return f'Resultado : {total}'

print(multiplicar(2, 6, 12, 1, 0, 3,0 ,0,0,0,0,0))     

# 2 - Criar uma função para saber se o número informado é par ou ímpar
criarseparador(30)
def parimpar(*args):    
    for numero in args:
        resultado = (f'O número {numero} é Par' if numero % 2 == 0 else f'O número {numero} é Ímpar')
        print(resultado)

print(parimpar(2,3,1,4,6,8,9,11,13))
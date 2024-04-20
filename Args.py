#Argumentos não nomeados em funções 

'''
  Utilizado quando não sabemos a quantidade de parâmetros que serão utilizados
  No exemplo abaixo foi criada uma função para somar todos os valores digitados pelos 
  usuário quando este pressionar a tecla =
'''

def somar(*args):
    total = 0
    
    for numero in args:
        total += numero 

    return(f'A soma é {total}')

print(somar(1,2,10,3)) 
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b
   
print(somar(3,9))
print(somar(15,9))

print(subtrair(3,9))
print(subtrair(13,9))

print(multiplicar(13,9))
print(multiplicar(2,9))

#Argumento nomeado. Se nomear um todos após devem ser nomeados
print(somar(a=2, b=3))
#Com argumentos nomeados podemos alterar a ordem
print(somar(b=7, a=3))

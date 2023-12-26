#Tipos imutáveis
#int, str, float, bool
#Documentação: https://docs.python.org/pt-br/3/


texto = input('Digite um valor qualquer : ')
texto_novo = texto
# não é permitido fazer isso texto = texto[5] 
print(texto)

print(texto.lower()) #Tudo minúsculo
print(texto.upper()) #Tudo maiúsculo
print(texto_novo.zfill(50))
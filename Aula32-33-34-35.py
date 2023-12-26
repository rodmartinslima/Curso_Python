#Aula sobre o loop while
#Uso do break e continue

contador = 0

while contador < 100:
    contador += 1 #incrementa de 1 em 1

    '''
    if contador in (1, 3, 5, 7, 9): #ignorar os primeiros números ímpares
        continue #continue faz voltar para o início do laço 
    '''

    #Trecho abaixo mostra apenas números pares
    if contador % 2 > 0:
        continue #continue faz voltar para o início do laço

    print(contador)

    if contador == 50:
        break  #break interrompe o loop

print('Acabou a contagem')
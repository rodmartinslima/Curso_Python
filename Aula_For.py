#Utilização do for no python

'''
  
  O código abaixo irá formatar uma frase digitada com o caractere selecionado pelo usuário.
  O sistema não irá prosseguir caso a frase não tenha sido informada ou o caractere selecionado
  seja inválido.

'''
caracteres_validos = '*-_'
nova_frase = ''
validador_frases = False
validador_caracteres = False

while validador_frases == False:
    frase = input('Digite a sua frase : ')

    if frase == '':
        print('Nenhuma frase digitada!')
        continue
    else:
        while validador_caracteres == False:
            formata = input('Digite um dos caracteres para formatar a sua frase (*-_) : ')

            if formata not in caracteres_validos:
                print('Nenhum caractere válido informado!')
                continue

            validador_caracteres = True

    validador_frases = True
       
for letra in frase:
    if letra != ' ':
        letra = formata + letra
        nova_frase = nova_frase + letra

nova_frase = nova_frase.upper() + formata
print(f'{nova_frase}')
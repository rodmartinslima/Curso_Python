#Programa para validar qual letra de uma frase apareceu mais vezes

i = 0
qtde_Letra = 0
letra_vencedora = ''
letras_encontradas = ''

frase = input('Digite uma frase : ')

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual in letras_encontradas:
        qtde_Letra = frase.count(letra_atual)
        letra_vencedora = letra_atual 

    letras_encontradas = letras_encontradas + letra_atual
    i += 1

if letra_vencedora != '':
    print(f'A letra vencedora foi "{letra_vencedora}" que apareceu {qtde_Letra} vezes no texto "{frase}".')
else:
    print(f'Nenhuma letra digitada se repetiu no texto "{frase}"')

    
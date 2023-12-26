#Exemplo de While com utilização do else

print('Iniciando o sistema....')
meu_texto = input('Informe o texto a ser percorrido : ').lower()
i = 0
caracteres_invalidos = '@#$%¨&*()'

if meu_texto == '':
    print('Nenhum texto informado.')

while i < len(meu_texto):
    letras = meu_texto[i]

    if letras in caracteres_invalidos:
        print('Caractere inválido detectado')
        break
    
    print(letras)
    i += 1
else:
    print('Texto validado com sucesso')

print('Programa finalizado')

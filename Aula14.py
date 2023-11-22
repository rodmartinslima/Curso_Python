#Estudo de if - elif e else

genero = input('Informe o sexo: (M)asculino ou (F)eminino: ')
feminino = bool(genero == 'F')

if  feminino:
    print('Você é do sexo Femino')
elif genero == 'M':
    print('Você informou que é do sexo masculino')
else:
    genero_escrito = input('O sexo informado não foi válido, digite o seu gênero de forma escrita: ')

    if genero_escrito == '':
        ...
    else:
        print(f'Gênero informado {genero_escrito}')
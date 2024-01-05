'''
  O jogo consiste em que o usuário acerte a palavra secreta baseado nas letras que ele chutar
''' 
palavra_secreta = 'vencer'
rodando = True
n_tentativas = 0

print('Descubra a palavra secreta...')
print('=' * 50)
while rodando:
    letra = input('Digite uma letra : ').lower()

    if len(letra) > 1:
        print('Informe apenas uma letra, tente novamente...')
        continue

    n_tentativas += 1    
    letra_certa = palavra_secreta.count(letra)

    if letra_certa > 0:
        print(f'Você acertou a letra {letra}')
        palavra_misteriosa = ''

        for letter in palavra_secreta:
            if letter == letra:
                palavra_misteriosa = palavra_misteriosa + letra
            else:
                palavra_misteriosa = palavra_misteriosa + '*'

        print(palavra_misteriosa)
        palpitar = True

        while palpitar:
            validar_frase = input('Deseja chutar qual é a palavra secreta? (s/n) ').lower()

            if validar_frase not in ('s', 'n'):
                print('Escolha inválida')
                continue

            if validar_frase == 's':
                palpite = input('Digite seu palpite de frase secreta: ').lower()

                if palpite == palavra_secreta:
                    print(20 * '=')
                    print('PARABÉNS! Você acertou a palavra secreta')
                    n_tentativas += 1
                    palpitar = False
                    rodando = False
            else:
                palpitar = False
    else:
        print('*')
        dica = input('Desejar receber dica(s)? (s/n)').lower()

        if dica == 's':
            print(f'A quantidade de letras da palavra secreta {len(palavra_secreta)}')

        continue

print(50 * '=')
print(f'Número de tentativas {n_tentativas}')
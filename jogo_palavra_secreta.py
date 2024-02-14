'''
  O jogo consiste em que o usuário acerte a palavra secreta baseado nas letras que ele chutar
''' 
import random
lista_palavras = ['vencer', 'lutar', 'falar', 'fazer', 'jogar', 'comer', 'corinthians', 'orar', 'laranja', 'filme', 'televisão']
lista_letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']

palavra_secreta = random.choice(lista_palavras)
rodando = True
n_tentativas = 0

print('Descubra a palavra secreta...')
print('=' * 50)
while rodando:
    letra = input('Digite uma letra : ').lower()

    if len(letra) > 1:
        print('Informe apenas uma letra, tente novamente...')
        continue

    if letra == '':
        print('Nenhum letra digitada.')
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
                    print(f'PARABÉNS, você acertou! "{palavra_secreta}" é a palavra secreta')
                    n_tentativas += 1
                    palpitar = False
                    rodando = False
            else:
                palpitar = False
    else:
        print('*')
        dica = input('Desejar receber dica(s)? (s/n) ').lower()

        if dica == 's':
            print(f'A quantidade de letras na palavra secreta é {len(palavra_secreta)}')
            letra_dica = random.choice(lista_letras)
            print(f'Na palavra secreta a letra "{letra_dica}" aparece {palavra_secreta.count(letra_dica)}x')

        continue

print(50 * '=')
print(f'Número de tentativas {n_tentativas}')
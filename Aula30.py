#Exercícios

'''
  Crie um programa que peça para o usuário informar um número inteiro
  verifique se esse número é par ou ímpar
  Caso o usuário não digite um número inteiro informe que não é um númer inteiro
 
'''
print('=' * 80)
valor_str = input('Digite um número inteiro : ')

try: 
    valor_int = int(valor_str)

    if (valor_int % 2) == 0:
        print(f'O valor {valor_int} é um número par')
    else:
        print(f'O valor {valor_int} é um número ímpar')
except:
    print('O valor digitado não é um número inteiro')

print('=' * 80)

'''
  Crie um programa que pergunte a hora para o usuário e faça uma saudação (bom dia, boa tarde ou boa noite)
  de acordo com a hora informada.
'''

hora = input('Informe a hora atual (entre 0 e 23): ')

try:
    hora_int = int(hora)

    if hora_int >= 24 or hora_int < 0:
        hora_int = 0

    if hora_int >= 0 and hora_int < 12:
        print('Bom dia!')
    elif hora_int >= 12 and hora_int < 18:
        print('Boa tarde!')
    elif hora_int >= 18 and hora_int < 24:
        print('Boa noite!')
except:
    print(f'O valor {hora} não é uma hora válida')

print('=' * 80)

'''
  Crie um programa que pergunte ao usuario o seu nome. Se o nome tiver menos do que 4 letras
  escrever que o nome é curto, se o nome tiver entre 5 e 6 letras escreva que o nome é normal,
  se tiver mais do que 6 letras escreva que o nome é extenso
'''
nome = input('Informe o seu nome : ')

tamanho = len(nome)

if tamanho == 0:
    print('Tamanho do nome inválido')
elif tamanho <= 4:
    print(f'O seu nome {nome} é curto.')
elif tamanho > 4 and tamanho <= 6:
    print(f'O seu nome {nome} é normal.')
elif tamanho > 6:
    print(f'O seu nome {nome} é extenso.')

print('=' * 80)
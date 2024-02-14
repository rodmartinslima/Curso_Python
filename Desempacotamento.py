'''
  Introdução ao desempacotamento
'''

nomes = ['Rodrigo', 'Ana', 'Luna']

nome1, nome2, nome3 = nomes
print(nome1)
print(nome2)
print(nome3)

#pegar um valor de um índice específico
primeiro_nome, *resto = nomes #variável resto não é usual
#forma correta > primeiro_nome, _ = nomes
print(primeiro_nome, resto)

#exemplo correto pegando o valor do índice 1
_, segundo_nome, _ = nomes
print(f'O segundo nome é {segundo_nome}')


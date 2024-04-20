'''
  Uma lista de compras que permita inserir, apagar e listar os valores gravados
  *Não pode gerar erros de índices inexistentes
'''
print('=' * 50)
print('Bem vindo a sua lista de compras')
inserindo = True
opcoes = ['I','D','L','F']
lista_compras = []

while inserindo:
    opt = input('(I)ncluir - (D)eletar - (L)istar - (F)inalizar Programa : ').upper()
    
    if opt in opcoes:       
      if opt == 'I':
        item_lista = input('Digite o item da sua lista : ')
        lista_compras.append(item_lista)
        print(f'Item inserido: {item_lista}')
      elif opt == 'D':
        item_lista = input('Digite o nome do ite para apagar da sua lista : ')
        for indice, nome in lista_compras:
          if nome == item_lista:
            lista_compras.remove(indice)
      elif opt == 'L':
        print('Essa é a sua lista de compra atual : ')
        for item in lista_compras:
          print(item)
      elif opt == 'F':
        print('Limpando a lista de compras')
        inserindo = False
        lista_compras.clear
    else:
      continue

print('Lista de compras finalizada.')
    


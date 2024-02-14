'''
Utilização de lista em Python
- append
- pop
- insert
- delete

'''
escolhas_validas = ['A', 'N', 'S', 'L']
lista_nomes = []

pedir_nome = True
while pedir_nome:
    lista_nomes.append(input('Digite um nome para a lista : '))
    print(f'O nome {lista_nomes[-1]} foi inserido.')

    continuar = True
    while continuar:
        chosen = input('(A)pagar último nome | (N)ovo nome | (S)air | (L)impar Lista ').upper()
    
        if chosen not in escolhas_validas:
            print('Opção inválida')
            continue
        elif chosen == 'S':
            pedir_nome = False
            break
        elif chosen == 'A':
            print(f'Lista antes de apagar o último nome: {lista_nomes}')
            nome_apagado = lista_nomes.pop(-1)
            print(f'O nome {nome_apagado} foi inserido.')
            print(f'Lista após de apagar o último nome: {lista_nomes}')
        elif chosen == 'L':
            lista_nomes.clear()
            print('A lista foi completamente limpa')
            continue
        break

print(f'Os nomes informados foram {lista_nomes}')
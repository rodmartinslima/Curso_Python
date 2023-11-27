#none = não valor
# is e is not

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Atendeu a condição')
else:
    print('Não atendeu a condição')

if passou_no_if is None:
    print('Não passou no if')
    print(f'Valor da variável {passou_no_if}')

if passou_no_if is not None:
    print('Passou no if')
    print(f'Valor da variável {passou_no_if}')

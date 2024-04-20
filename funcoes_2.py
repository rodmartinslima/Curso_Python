#Validação de valores dos parâmetros das funções com NONE
#Essa validação evita um erro caso tente manipular o valor que não tenha sido informado

#Obs: A regra de argumento nomeados também se aplica a este caso

def ImprimirMensagem(nome, sobrenome, cidade=None):
    if cidade is not None:
        return (f'Olá {nome} {sobrenome} da cidade de {cidade}!')
    else:
        return (f'Olá {nome} {sobrenome}!')

print(ImprimirMensagem('Rodrigo', 'Martins'))
print(ImprimirMensagem('Rodrigo', 'Martins','Viçosa'))
print(50 * '=')
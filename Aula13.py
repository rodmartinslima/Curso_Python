#Estudo da função format para strings

meu_nome = 'Rodrigo'
meu_sobrenome = 'Martins'
minha_idade = 35

nome_completo = 'nome={} sobrenome={} idade={}'
texto_formatado = nome_completo.format(meu_nome, meu_sobrenome, minha_idade)
print(texto_formatado)

#pode ser passado o index
nome_completo_index = 'nome={0} sobrenome={1} idade={2}'
texto_formatado = nome_completo_index.format(meu_nome, meu_sobrenome, minha_idade)
print(texto_formatado)

# ou usar parâmetro nomeado
nome_completo_param_nomeado = 'nome={nome_} sobrenome={sobrenome_} idade={idade_:.2f}'
texto_formatado_param_nomeado = nome_completo_param_nomeado.format(
    nome_=meu_nome, 
    sobrenome_=meu_sobrenome, 
    idade_=minha_idade)
print(texto_formatado)
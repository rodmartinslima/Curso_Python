print(123, 988, sep=';') #Possível informar separador para não deixar espaço entre valores
print('A', 0)

print(123, 988, sep=';', end='!!') #Possível informar separador e indicador do final do arquivo
print(' $$ Não quebrou linha por causa do end=!!')

# Comandos ocultos para quebra de linha
#Windows > CRLF, na programação é representado pelo \r \n
print("Comando", "Windows", sep='_', end='\r\n') 
print(' Quebrou linha') 

#Linux/MAC > LF, na programação é representado pelo \n
print("Comando", "Unix", sep='%', end='\n') 
print(' Quebrou linha') 

#possível quebrar linha informando dois valores para end
print("Dois", "Parametros", sep='___', end='#_(\n') 
print(' Quebrou linha')
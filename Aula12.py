#Cálculo IMC

nome = str(input('Digite o seu nome completo : \n'))
peso = float(input('Informe o seu peso : \n'))
altura = float(input('Informe a sua altura : \n'))

imc = peso / (altura * altura)

#f-strings
print('=' * 50)
print(f'Ficha do paciente {nome}')
print(f'Altura : {altura:.2f}')
print(f'Peso : {peso:.2f}')
print(f'{nome}, o resultado do seu IMC é: {imc:.3f}')
print('_' * 50)
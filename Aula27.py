#CONSTANTES e variáveis
#Exemplo de um sistema de radar
#Constantes escritas com letras maiúsculas

print('Ligando o Motor...')
RADAR1_LOCAL_KM = 30
RADAR2_LOCAL_KM = 65
RADAR1_VELOCIDADE_MAX = 80 #Rodovia faixa simples
RADAR2_VELOCIDADE_MAX = 40 #Trecho de perímetro urbano
RADAR_TAXA_TOLERANCIA = 12 #Taxa em porcentagem
RANGE_RADAR = 1.5 #Pega a velocidade do carro 1.5km antes do local do radar.

print('Marcha engatada, saindo da garagem...')
velocidade_carro = 40
km_local_carro = 10
multa = False
abandono = False

print('=' * 70)
print(f'Entrando na rodovia, Km: {km_local_carro} ')
while not multa:
    print(f'A sua velocidade atual é de {velocidade_carro} Km/h ')

    acao = input('Deseja (a)celerar gradualmente - (f)rear gradualmente - (A)celerar pisando fundo \
- (F)rear bruscamente?')

    if acao == 'a':
        velocidade_carro = velocidade_carro + 5
    elif acao == 'A':
        velocidade_carro = velocidade_carro + 20
    elif acao == 'f':
        velocidade_carro = velocidade_carro - 10
    elif acao == 'F':
        velocidade_carro = velocidade_carro - 35 

    if velocidade_carro < 0:
        velocidade_carro = 0

    if velocidade_carro == 0:
        print('O carro está parado!')
        acao = input('Deseja (A)celerar ou (S)air do carro?')

        if acao in ('s', 'S'):
            print('Desligando o motor...')
            print('Porta destravada...')
            print('saindo..')
            abandono = True
            break

    #Aviso de fiscaliação eletrônica
    if km_local_carro == (RADAR1_LOCAL_KM - 2):
        print(f'PLACA >> Radar Eletrônico : {RADAR1_VELOCIDADE_MAX}  << ')
    elif km_local_carro == (RADAR2_LOCAL_KM - 2):
        print(f'PLACA >> Radar Eletrônico : {RADAR2_VELOCIDADE_MAX}  << ')

    if (km_local_carro == RADAR1_LOCAL_KM) or (km_local_carro == (RADAR1_LOCAL_KM - RANGE_RADAR)):
        
        velocidade_permitida_com_tolerancia = RADAR1_VELOCIDADE_MAX + (
            (RADAR1_VELOCIDADE_MAX * RADAR_TAXA_TOLERANCIA) / 100
            )
        
        if velocidade_carro > velocidade_permitida_com_tolerancia:
            print('!' * 70)
            print(f'Você recebeu uma multa no Km {RADAR1_LOCAL_KM}, a velocidade máxima permitida é {RADAR1_VELOCIDADE_MAX} km/h')
            print(f'A sua velocidade foi {velocidade_carro} Km/h')
            print(f'A velocidade máxima com a tolerância de {RADAR_TAXA_TOLERANCIA}% é de {velocidade_permitida_com_tolerancia} Km/h')
            print('!' * 70)
            multa = True
            break
    elif (km_local_carro == RADAR2_LOCAL_KM) or (km_local_carro == (RADAR2_LOCAL_KM - RANGE_RADAR)):
        
        velocidade_permitida_com_tolerancia = RADAR2_VELOCIDADE_MAX + (
            (RADAR2_VELOCIDADE_MAX * RADAR_TAXA_TOLERANCIA) / 100
            )
        
        if (velocidade_carro > velocidade_permitida_com_tolerancia):
            print('!' * 70)
            print(f'Você recebeu uma multa no km {RADAR2_LOCAL_KM}, a velocidade máxima permitida é {RADAR2_VELOCIDADE_MAX} Km/h')
            print(f'A sua velocidade foi {velocidade_carro} km/h')
            print(f'A velocidade máximo com a tolerância de {RADAR_TAXA_TOLERANCIA}% é de {velocidade_permitida_com_tolerancia} km/h')
            print('!' * 70)
            multa = True
            break
        else:
            print(f'Você não recebeu nenhuma multa ao passar pelo radar do Km {RADAR2_LOCAL_KM}')
    elif km_local_carro == 150 and not multa and not abandono:
        print('Parabéns,você não recebeu nenhuma multa durante a viagem!')
    
    print(f'Você passou pelo Km {km_local_carro} e sua velocidade foi {velocidade_carro}')
    print('-' * 70)

    #Atualizando valores
    km_local_carro = km_local_carro + 1
    velocidade_carro = velocidade_carro + 1.5 #Velocidade ganha sem aceleração
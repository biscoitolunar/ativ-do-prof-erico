#faça um programa que converta metros para centímentro.
#1m tem 100cn
#entrada
tamanho_em_metros = float(input('digite o tamanho em metro: '))

#cálculo
tamanho_em_centimentros = tamanho_em_metros * 100

#exibir
print('{} mentros é igual a{:.0f} cemtímentros'. format(tamanho_em_metros, tamanho_em_centimentros))

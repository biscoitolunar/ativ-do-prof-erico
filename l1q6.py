#importa o valor de pi e a função de potencia (pow) da biblioteca math
from math import pi, pow

#faça um programa que peça um raio de um circulo, calcule e mostre sua area.
#area do circulo = 2 * pi * r * r
#entrada
raio_do_circulo = float(input('informe o tamanho do raio do circulo:'))

#processamento
area_do_circulo = pi * pow(raio_do_circulo,2)

#resposta
print('a area do circulo e {:.2f}'.format(area_do_circulo))

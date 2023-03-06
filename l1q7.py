import math
#faça um programa que calcule a area de um quadrado, em seguida mostre o dobro desta area para o usuario.
#area do quadrado = l * l 
#entrada
lado_do_quadrado = float(input('digite o valor do lado do quadrado:'))

#processamento
area_do_quadrado = pow(lado_do_quadrado,2)

#resposta
print('o valor do quadrado da area e:{}'.format(area_do_quadrado *2))

"""
@rozendox_

Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
método format
usando a biblioteca sicpy

"""

import scipy

#  entrada de dados informando o raio.
raio = int(input('informe o raio'))

#  diametro do círculo
diametro = raio ** 2

#  calculo da área.
area = scipy.pi * raio

#  retirando as virgulas do output.
area2 = int(area)

print(f'o círculo que tem', {raio}, ' cm de raio, tem ', {area2}, 'cm² de área')

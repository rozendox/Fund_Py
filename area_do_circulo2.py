"""

Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

nessa versão vamos mostrar as casas após a vírgula
método format

@rozendox_
"""

raio = float(input('Informe o raio do cículo'))
pi = float(3.14)
diametro = raio ** 2
area = pi * raio

print(f'O diâmetro do círculo é de:', {diametro},
      'centímetros, e sua área é de:', {area}, 'm²')

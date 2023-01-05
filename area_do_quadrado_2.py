"""

@Rozendox_

Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
método format

"""

lado = int(input('Informe o lado do quadrado'))

area_quadrado = lado * lado
dobro_area = area_quadrado * 2

print(f'o quadrado que tem:', {lado}, 'Centímetros de lado, '
                                      'tem', {area_quadrado}, 'cm² de área, e seu dobro é de:', {dobro_area}, 'cm²')

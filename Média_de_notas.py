"""
@Rozendo

Faça um Programa que peça as 4 notas bimestrais e mostre a média.

#método de impressão
"""

nota_1 = int(input('Digite a primeira nota'))
nota_2 = int(input('Digite a segunda nota'))
nota_3 = int(input('Digite a terceira nota'))
nota_4 = int(input('Digite a quarta nota'))

soma_notas = nota_1 + nota_2 + nota_3 + nota_4

media_notas = soma_notas / 4

print(media_notas)

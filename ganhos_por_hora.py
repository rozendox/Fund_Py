"""

@rozendox_

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.

um trabalhador que trabalha de segunda a sexta
"""


trabalhador = str(input('Informe o nome do trabalhador'))

#  ganhos por horas
g_h = int(input('Informe seus ganhos por hora'))

#  horas semanais
h_s = 8 * 6

#  horas trabalhadas totais
h_t = h_s * 4

#  salario final
salario = g_h * h_t

#Transformar o valor do salário em float para aparecer o zero após a vírgula
salario2 = float(salario)


print(f'Sr.', {trabalhador}, 'trabalhando por', {h_s}, 'horas semanais, seu salário é de: R$', {salario2}, 'Reais')

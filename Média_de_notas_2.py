"""
@rozendo
Faça um Programa que peça as 4 notas bimestrais e mostre a média.

método format
programa que mostra a média com o nome do aluno
e a série/ ano.

"""
aluno = str(input('Insira o nome do aluno'))
serie_escola = str(input('Informe a série do aluno'))
nota_1 = int(input('Digite a primeira nota'))
nota_2 = int(input('Digite a segunda nota'))
nota_3 = int(input('Digite a terceira nota'))
nota_4 = int(input('Digite a quarta nota'))

soma_notas = nota_1 + nota_2 + nota_3 + nota_4

media_notas = soma_notas / 4

print(f'A média anual das notas do aluno', {aluno}, 'do', {serie_escola}, 'é de', {media_notas})

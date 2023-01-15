#Rozendox

#loop que retorna a tabela de multiplicação de 1 a 10

#entrada de dados
num = int(input("Enter number\n"))

#enquanto o numero da entrada de dados for menor que 11
while num < 11:
  
    #entrada de valores
    #lool para x corre a partir do numero 1, 10 vezes
    for x in range(1, 11):
        print(f"{num} X {x} = {num * x}")
    #auto incrementa 1 à variável.
    num += 1

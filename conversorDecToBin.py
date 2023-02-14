#Rozendox



divd = int(input("Informe um numero em base decimal para continuar....: "))
num_digit = divd
quoc = 1
list = []

while quoc >= 1:
  resto = divd % 2
  list.insert(0, resto)
  quoc = divd // 2
  divd = quoc

binario = ''.join([str(item) for item in list])
print("O número", num_digit, ", quando convertido em binário, vale:", binario)

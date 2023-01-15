#calculadora que multiplica um numero de 1 a 10

#entrada de dado
x = int(input("entre com o numero"))

#loop
for i in range(1,11):
    multi = x * i
    print(f"{x} x {i} = {multi}")
    
    
"""    
output:
  
entre com o numero2

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
"""

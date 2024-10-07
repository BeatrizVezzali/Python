num = int(input("Digite o número de termos:"))
a = 1
b = aux = 2
print(a, end = '   ')

for cont in range(num - 1) :
      print(aux, end = '   ')
      aux = a * b
      a = b
      b = aux

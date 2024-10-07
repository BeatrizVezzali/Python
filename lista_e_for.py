numeros = [0, 1, 2, 3, 4, 5]

for elementos in range(len(numeros)) :
      print("%d: %d"%(elementos, numeros[elementos]))

for cont, elementos in enumerate(numeros) :
      print(cont, ":", elementos)

for cont in range(2, 7) :
      print(cont)
else :
    print("Até logo!")


for letras in 'Python' :
      print(letras, '    ')

for letras in 'Anticonstitucionalíssimamente' :
      print(letras, end = '\t')

frutas = ['banana', 'abacaxi', 'abacate', 'manga']

for palavra in frutas :
      print(palavra)

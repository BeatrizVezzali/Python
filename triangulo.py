A = int(input("Digite o primeiro número:"))
B = int(input("Digite o segundo número:"))
C = int(input("Digite o terceiro número:"))

if (A < B+C) and (B < A+C) and (C < A+B):
    if (A == B) and (B == C):
        print("É um triângulo equilátero",A,B,C)
    elif (A == B) or (B == C) or (C == A):
          print("É um triângulo isóceles",A,B,C)
    else:
        print("É um triângulo escaleno",A,B,C)
else:
    print("Não é um triângulo",A,B,C)


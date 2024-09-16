A = int(input("Digite o primeiro número:"))
B = int(input("Digite o segundo número:"))
C = int(input("Digite o terceiro número:"))

A < B + C
B < A + C
C < A + B

if (A == B) or (A == C) or (B == C) :
    print("Triângulo isósceles")
else :
    if (A!= B) and (B!= C) :
        print("Triângulo escaleno")
    else :
       print("Triângulo equilátero")

   

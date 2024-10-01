n = int(input("Digite o valor de n:"))

while (n < 1) or (n > 50) :
    print("Número inválido!")
    n = int(input("Digite o valor de n:"))
    
while (n < 250) :
    n = n * 2
    print(n)

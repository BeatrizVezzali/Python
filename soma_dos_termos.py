num = int(input("Digite um número:"))

while (num != 0) :
      soma = cont = 0
      while (cont < num) :
            soma = soma + cont
            cont = cont + 1
      print("A soma dos termos é:", soma)
      num = int(input("Digite um número:"))

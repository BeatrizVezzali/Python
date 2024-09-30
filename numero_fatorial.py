num = int(input("Digite o número:"))

while (num != 0) :
      fat = cont = 1
      while (cont < num) :
            fat = fat * cont
            cont += 1
      print("O fatorial de", num, "é:", fat)
      num = int(input("Digite o número:"))
    

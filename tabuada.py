num = int(input("Digite a tabuada:"))

while (num != 0) :
      for cont in range(1, 11) :
            res = cont * num
            print(num, "x", cont, "=", res)
      num = int(input("Digite a tabuada:"))
      

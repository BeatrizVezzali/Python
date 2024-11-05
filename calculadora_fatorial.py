def main() :
      num = int(input("Digite um número:"))
      while (num > 0) :
           fatorial = calculofat(num)
           print("O fatorial de:", num, "é:", fatorial)
           num = int(input("Digite um número:"))

def calculofat(n) :
      cont = 1
      fatorial = 1
      while (cont <= n) :
           fatorial = fatorial * cont
           cont += 1
      return fatorial

main()

cont = 0
resp = "sim"

while (resp == "sim" or resp == "batata") :
      x = int(input("Digite x:"))
      r = x * 3
      print("Valor de r:", r)
      resp = input("Deseja continuar?")
      cont += 1

print("Repetições realizadas:", cont)



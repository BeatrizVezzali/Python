dias = int(input("Digite o número de dias:"))
seg = dias * 24 * 60 * 60

horas = int(input("Digite o número de horas:"))
seg = seg + horas * 60

minutos = int(input("Digite o número de minutos:"))
seg = seg + minutos * 60

print("O tempo total em segundos é:", seg)

somaM = 0.0

for cont in range(1,10):
  sexo = input("Digite o sexo:")
  if (sexo == 'M') or (sexo == 'm') :
      alturaM = float(input("Digite a altura:"))
      if (cont == 1) :
          maior = alturaM
          menor = alturaM
      elif (alturaM > maior) :
            maior = alturaM
      elif (alturaM < menor) :
            menor = alturaM
            somaM = somaM + alturaM
      sexo = input("Digite o sexo:")
      if (sexo == 'H') or (sexo == 'h') :
          alturaH = float(input("Digite a altura:"))
          if (cont == 1):
              maior = alturaH
              menor = alturaH
          elif (alturaH > maior) :
                maior = alturaH
          elif (alturaH < menor) :
                menor = alturaH
                

media = somaM // (10 - cont)

print("A média de mulheres é:", media)

print("A maior altura é maior:", maior)

print("A menor altura é:", menor)
          
    

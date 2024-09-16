nota1 = float(input("Insira a nota da primeira prova:"))
nota2 = float(input("Insira a nota da segunda prova:"))
nota3 = float(input("Insira a nota da terceira prova:"))
media = 0
exame = 0

media = (nota1 + nota2 + nota3) / 2

exame = nota2 + nota3

if (media <= 3.0) :
    print("Reprovado!")
elif (media > 3.0) and (media <= 6.0) :
      print("Exame!", "Você precisa tirar", exame , "na próxima prova.")
else :
   print("Aprovado!")

print("Sua média é:", media)
      


laboratorio = float(input("Digite a nota de laboratório:"))
avaliacao_semestral = float(input("Digite a nota da avaliação semestral:"))
exame_final =  float(input("Digite a nota do exame final:"))

media_final = ( (laboratorio * 2) + (avaliacao_semestral * 3) + (exame_final * 5) ) / 10

print("A média final é: %.2f" %media_final)


if (media_final >=  8) and (media_final <= 10) :
    print("Seu conceito  é  A")
elif (media_final >= 7) and (media_final < 8) :
       print("Seu conceito é B")
elif (media_final >= 6) and (media_final < 7) :
       print("Seu conceito é C")
elif (media_final >= 7) and (media_final < 6) :
       print("Seu conceito é D")
else :
     print("Seu conceito é E")
       
    


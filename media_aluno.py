nota1 =  float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))

media = (nota1 + nota2) / 2

if(media >= 7):
    print("Aluno aprovado!")
    print("Nota:", media)
else:
      if(media >= 5):
         print("Aluno de exame!")
         print("Nota:", media)
      else:
         print("Aluno reprovado!")
         print("Nota:", media)

       

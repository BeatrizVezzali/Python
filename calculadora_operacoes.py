num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
operador = input("Digite a operação desejada:")
res = 0

if (operador == '+') :
    res = num1 + num2
elif (operador == '-') :
       res = num1 - num2
elif (operador == '*') :
       res = num1 * num2
elif (operador == '/') :
     if (num2 == 0) :
         print("Erro! Divisão com 0")
     else :
           res = num1 / num2
else :
      print("Operador inválido!")
      
print("Resultado:", res)
        








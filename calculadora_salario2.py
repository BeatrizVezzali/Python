salatual = float(input("Informe o salário atual:"))

if (salatual < 500) :
    novosal = salatual * 1.15
elif (salatual <= 1000) :
       novosal = salatual * 1.10
else :
       novosal = salatual * 1.05

print("O salário com o reajuste é de R$: %.2f" %novosal)


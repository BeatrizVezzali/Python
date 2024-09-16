codigo = int(input("Informe o código do funcionário:"))
salarioatual = float(input("Informe o salário atual do funcionário:"))
salariocorrigido = 0

if (codigo == 101) :
    salariocorrigido = salarioatual * 1.1
elif (codigo == 102) :
      salariocorrigido = salarioatual * 1.2
elif (codigo == 103) :
      salariocorrigido = salarioatual * 1.3
else :
  salariocorrigido = salarioatual * 1.4


print(f"O salário atual é: R${salarioatual: 4.2f}")
print(f"O novo salário é: R${salariocorrigido: 4.2f}")
print(f"O aumento salarial foi de: R${salariocorrigido - salarioatual: 4.2f}")

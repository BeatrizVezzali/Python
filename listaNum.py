listaNum = []
num = float(input("Digite o primeiro número ou zero para finalizar:"))

while(num != 0) :
    listaNum.append(num)
    num = float(input("Digite outro número ou zero para finalizar:"))

listaNum.sort()
tam = len(listaNum) -1
x = 0
while(x <= tam) :
    print(listaNum[x])
    x = x + 1

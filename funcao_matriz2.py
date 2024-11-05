def criamatriz(num_lin, num_col) :
      matriz = []
      for i in range(num_lin) :
           linha = []
           for j in range(num_col) :
                valor = int(input("Digite  o elemento [" + str(i) + "] [" + str(j) + "]"))
                linha.append(valor)
                matriz.append(linha)
      return matriz

def lematriz() :
      lin = int(input("Digite o número de linhas:"))
      col = int(input("Digite o número de colunas:"))
      return criamatriz(lin, col)

m = lematriz()
print(m)

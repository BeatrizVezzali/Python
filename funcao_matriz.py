def criamatriz(num_linhas, num_col, val) :
      matriz =[]
      for i in range(num_linhas) :
           linha = []
           for j in range(num_col) :
                linha.append(val)
                matriz.append(linha)
      return matriz

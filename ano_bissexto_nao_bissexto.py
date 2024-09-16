ano = int(input("Digite o ano desejado:"))

if (ano %400 == 0) or (ano %4 == 0) and (not(ano %100 == 0)) :
    print("O ano", ano, "é bissexto")
else:
    print("O ano", ano, "não é bissexto")

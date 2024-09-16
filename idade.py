idade = int(input("Digite a sua idade:"))

if(idade < 12):
    print("Você é uma criança!", "\nSua idade:", idade)
elif(idade <18):
    print("Você é um adolescente!", "\nSua idade:",  idade)
elif(idade < 60):
    print("Você é um adulto!", "\nSua idade:", idade)
else:
    print("Você é um idoso!", "\nSua idade:", idade)

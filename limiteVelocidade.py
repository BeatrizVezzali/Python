velocidade = int(input("Entre com a velocidade [km/h]"))
limiteVelocidade = 80

if (velocidade > limiteVelocidade):
 print("Parabéns! Você foi multado!")
 valorMulta = (velocidade - limiteVelocidade)*5.00
 print(f"Valor da multa: R${valorMulta:.2f}")
 opCPF = input("Deseja colocar CPF na nota? Digite S para Sim e N para Não:")
 if (opCPF == 'S' or opCPF == 's'):
     CPF = int(input("Entre com o CPF:"))
     print("Obrigado volte sempre... Detran te aguarda...")
 else:
     print("Obrigado volte sempre... Detran te aguarda...")
if (velocidade < limiteVelocidade):
    print("Você não foi multado... Na próxima me aguarde... Ass: Radar")
    

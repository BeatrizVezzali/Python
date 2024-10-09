pontos = 0
questao = 1

while (questao <= 10) :
    resposta = input(f"Resposta da questão {questao}")
    if (questao == 1) and (resposta == "d") :
        pontos += 1
    if (questao == 2) and (resposta == "c") :
        pontos += 1
    if (questao == 3) and (resposta == "b") :
        pontos += 1
    if (questao == 4) and (resposta == "a") :
        pontos += 1
    if (questao == 5) and (resposta == "a") :
        pontos += 1
    if (questao == 6) and (resposta == "d") :
        pontos += 1
    if (questao == 7) and (resposta == "b") :
        pontos += 1
    if (questao == 8) and (resposta == "c") :
        pontos += 1
    if (questao == 9) and (resposta == "e") :
        pontos += 1
    if (questao == 10) and (resposta == "e") :
        pontos += 1
    questao += 1

print(f"A nota do aluno é {pontos}")
    

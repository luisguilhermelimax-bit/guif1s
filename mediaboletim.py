
#gostei muito desse
#media do boletim
print("                             ESCOLA FUCTURA                             ")
nome=input("qual seu nome?")
turma=(input("qual seria sua turma "))
print(f"ola,{nome} da turma:{turma} seja bem vindo ao seu boletim")

nota_de_atividade=float(input("qual foi sua nota nas ativades?"))
nota_do_teste=float(input("qual  foi sua nota no teste?"))
nota_da_prova=float(input("qual foi sua nota na prova?"))
print("    calculando nota....")

media=(nota_da_prova + nota_de_atividade + nota_do_teste )/ 3
media_recuperacao=7-media

if media >=6:
    print(f"parabens voce estar aprovado com o total de {media:.2f} ")
elif media >= 4 and media <6:
    print(f"voce estar de recuperacao por {media_recuperacao:.2f} pontos ")
else:
    print(f"voce nao atingiu nota suficiente para ser aprovado ou pra ficar em recuperacao pra atingir a nota de recuperacao falta:{media_recuperacao:.2f}")


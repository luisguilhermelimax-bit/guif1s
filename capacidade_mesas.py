print("                                           RESTAURANTE DO KILLUA                                                                         ") 


print('bem vindo ao restaurante do kilua    ')
nome=input("QUAL SERIA  O NOME DO SENHOR(A)?   ")
print(f"sejam bem vindo senhor(a):{nome}")
pessoas_por_cadeira=int(input("quantas pessoas estar com voce?"))
#matematica discreta um pouco complicada!!
mesas_por_cadeira=int(pessoas_por_cadeira+3)//4
print(f"serao  necessario para {pessoas_por_cadeira} pessoas,essa quantidade de mesas:{mesas_por_cadeira}")

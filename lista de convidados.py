
print("                                                    lista de convidados                                                    ")

convidados=['gondim','shallon','alberto','miguel','matheus','kaio','felipe','samuel','maga','vector']
novos_convidados=input("quem vc deseja adicionar")
convidados.append(novos_convidados)
remover_convidado=input("quem deseja retirar da lista.")
convidados.remove(remover_convidado)
print(len(convidados))
print(f"o nome do primeiro convidado e {convidados[0]}e o ultimo e o {convidados[10]}")

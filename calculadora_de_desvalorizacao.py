# guif1s
#cod1
#calculadora de desvalorizacao de carros
marca_do_carro=input("qual marca")
cor=input("que cor")
ano_do_carro=int(input("qual ano do carro?"))
comprado_carro=float(input("quanto foi?"))
print(f"parabens pela compra do carro {marca_do_carro},com a cor {cor} e do ano de {ano_do_carro} pelo preco de {comprado_carro}")
vender_o_carro=int(input("em quantos anos deseja vender o carro?"))
desvalorizacao=float(comprado_carro*(1-0.10)**vender_o_carro)
print("o preco que vai ser vendido e de ",desvalorizacao)
km_pecorridos=float(input("quantos km  vai ser a viagem?"))
consumo=float(input("quantos o litro o carro faz em um km?"))
media=float(km_pecorridos/consumo)
print((f"a media  foi de {media:.2f}"))
print("--------------------------------------------------------------------")
print("calculadora de depreciacao ")

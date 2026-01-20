#guif1s
print("                                    CALCULADORA DE  DESCONTO                                        ")

print("Formas de pagamento:")
print("1 - À vista (10% de desconto)")
print("2 - Cartão (preço normal)")
print("3 - Parcelado (10% de acréscimo)")


geladeira=float(3456.50)
tv=float(2000.50)
cama=int(1500)
print(f"a geladeira custa:{geladeira},a tv custa;:{tv},a cama cuusta:{cama}")
valor=float(input("vai gastar quanto?"))
forma = int(input("Escolha a forma de pagamento (1, 2 ou 3): "))

if forma == 1:
    valor_final = valor * 0.90
    print(f"com o desconto fica:{valor_final:.2f}")
elif forma == 2:
    valor_final = valor
    print(f"o valor deu:{valor_final}")
elif forma == 3:
    valor_final = valor * 1.10
    print(f"o valor final deu:{valor_final:.2f}")
else:
    print("esse tipo de pagamento nao e aceito!")

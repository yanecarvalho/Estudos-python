print("calculo de cubagem")


altura = float(input("digite a altura: "))
largura = float(input("digite a largura: "))
comprimento = float(input("digite o comprimento: "))


volume = altura * largura * comprimento


print("O volume é:", volume)


if volume < 300:
    print("transporte rodoviario")
elif volume < 1000:
    print("transporte marítimo")
else:
    print("transporte aéreo")
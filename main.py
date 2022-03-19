# Calculadorea de imc

# imc = Pesp / (altura * altura)

# < 19: delgadez
# entre 20 y 25: normal
# entre 26 y 30: sobrepeso
# > de 30: obesidad

peso = float(input("Introduce tu peso en KG: \n"))
altura = float(input("Introduce tu altura en cm: \n"))


def calcularIMC(peso, altura):
    imc = peso / (altura * altura)
    return imc


if calcularIMC(peso, altura) < 19:
    print("Tu imc es: ", imc, "y estas delgadez")
if calculaIMC(peso, altura) >= 19 and calcularIMC(peso, altura) <= 25:
    print("Tu imc es: ", imc, "y estas en una buena condicion")
if 25 < calcularIMC(peso, altura) <= 30:
    print("Tu imc es: ", imc, "y estas en sobrepeso")
if calcularIMC(peso, altura) > 30:
    print("Tu imc es: ", imc, "y estas en obesidad")

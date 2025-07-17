numeroA = int(input("Digite o valor de A: "))
numeroB = int(input("Digite o valor de B: "))
numeroC = int(input("Digite o valor de C: "))

delta = numeroB ** 2 - 4 * numeroA * numeroC

if delta < 0:
    print("Delta negativo, Não existem raízes reais.")
else:
    raizDelta = delta ** 0.5

    numeroX = - (numeroB + raizDelta) / (2 * numeroA)
    numeroX2 = - (numeroB - raizDelta)  / (2 * numeroA)

    print("O valor de delta é: ",delta)
    print(numeroX)
    print(numeroX2)

    
# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

metros = int(input("Digite a quantidade de metros a ser convertida: "))
cent = metros * 100
mili = metros * 1000
print(f"o numero de centimetros de {metros}m é igual a: {cent}cm")
print(f"o numero de milimetros de {metros}m é igual a: {mili}mm")
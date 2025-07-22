# faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m quadrados.

lar = float(input('Digite a largura da parede: '))
alt = float(input("Digite a altura da parede: "))
area = lar * alt
tinta = area / 2
print(f"A area da parede é: {area}")
print(f"a quantidade de tinta necessaria será: {tinta} litros")
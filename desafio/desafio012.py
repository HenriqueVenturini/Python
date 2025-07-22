# faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
n1 = float(input("digite o preço do produto: "))
desconto = n1 * (5/100)
preco = n1 - desconto
print(f"O valor com desconto é igual a: {preco}")
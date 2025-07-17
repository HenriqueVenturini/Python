# Faça um programa que leia algo pelo teclado e mostra na tela o seu tipo primitivo e toas as informações possiveis sobre ele.

algo = input("Digite algo: ")
print(type(algo))
print(algo.isalnum())
print(algo.isalpha())
print(algo.isdecimal())
print(algo.isdigit())
print(algo.islower())
print(algo.isupper())
print(algo.isascii())
print(algo.isnumeric())
# faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento
salario = float(input("Digite seu salario: "))
aumento = salario * (15 / 100)
novosalario = salario + aumento

print(f"o novo salario é igual a: {novosalario}")
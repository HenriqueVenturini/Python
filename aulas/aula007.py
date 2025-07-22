# Operadores Aritmeticos

# adição = +
# subtração = -
# multiplicação = *
# divisão = /
# potenciação = **
# divisão inteira = //
# resto da divisão = %

nome = input("Qual é o seu nome? ")
print(f"prazer em te conhecer, {nome:=^20}!")

n1 = int(input("digite um valor: "))
n2 = int(input("digite outro valor: "))
soma = n1+n2
sub = n1-n2
multi = n1*n2
divi = n1/n2
diviInt = n1//n2
expo = n1**n2
print(f"a soma vale {soma} \n o produto vale {multi} \n e a divisão é {divi:.3f}", end=' ')
print(f"divisão inteira {diviInt} e potencia {expo}")

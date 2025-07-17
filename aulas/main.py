print("Hello Word")
nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
peso = float(input("digite seu peso: "))

print(nome)
print(idade)
print(peso)

soma = 1 + 1 
multiplicacao = 4 * 4
divisao = 30 / 3
potencia = 7 ** 2  

print("soma ", soma)
print("multiplicação ", multiplicacao)
print("divisao ", divisao)
print("potencialização ", potencia)

idade = int(input("informe sua idade: "))
 
if idade < 18:
    print("cai fora!")
else:
    print("Bem vindo!")

lista_numeros = [1, 2, 3]

lista_numeros[0] = 5

lista_vazia = []

lista_vazia.append("Hello")
lista_vazia.append("Word")

# append = acrescenta um novo item a lista
# inset = insere um novo item na posição dada
# pop = remove e retorna o último item / da posição
# sort = ordena a lista
# reverse = ordena a lista em ordem reversa
# index = retorna a posição da primeira ocorrencia do item
# count = retorna o numero de ocorrencias do item
# remove = remove a primeira ocorrencia do item

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])

print(lista_vazia[0])
print(lista_vazia[1])


# x = valor alterado para cada repetição, pode ser usada apenas dentro do bloco de repetição
# x ja comeca com o valor 0
for x in range(5):
    print(x)
    

notas = []

for x in range(5):
    nome_aluno = input("nome: ")
    nota = float(input("nota: "))
    resultado = [nome_aluno, nota]
    notas.append(resultado)

print("quantidade de notas: ", len(notas))

for n in notas:
    nome_aluno = n[0]
    nota = n[1]
    print("o nome: ",nome_aluno, "tirou nota: ",nota)

num = 0

# ele vai parar no 11
while num <= 10:
    num+= 1
    print(num)

# ele vai parar no 10
while num < 10:
    num += 1
    print(num)
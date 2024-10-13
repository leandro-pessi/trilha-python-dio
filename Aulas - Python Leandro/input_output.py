nome = input("Digite o seu nome: ")
idade = input("Informe a sua idade: ")
print(nome, idade)

nome = "Leandro"
sobrenome = "Pessi Orige"

print(nome, sobrenome)
print(nome, sobrenome, end="...\n") #adiciona reticência e uma quebra de linha (\n)
print(nome, sobrenome, sep="#")  #mudou o separador
print(nome, sobrenome, sep="_", end=" ...\n")
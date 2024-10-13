# Exemplo utilizando um iterável
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end = "--")
print()

# range
list(range(11))
print(list(range(11)))

# Exemplo utilizando a função built-in range
tabuada=int(input("Digite um número: ", ))
for numero in range(0,(tabuada*10+1),tabuada):
    print(numero, end="--")
print()

# While
opcao = -1

while opcao !=0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando ...")
    elif opcao == 2:
        print("Exibindo o extrato ...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")

# Break
opcao = -1

while opcao !=0:
    opcao = int(input("Informe um número: "))

    if opcao == 10:
        break

    print(opcao)

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)

for numero in range(100):
    if numero % 2 == 0:
        continue
    print(numero, end=" ")
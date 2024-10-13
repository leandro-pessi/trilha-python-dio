nome = "PyThOn"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "   Olá mundo!                     "

print(texto + ".")
print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")

menu="Python"

print("###" + menu + "###")
print(menu.center(12,"#"))
print("P-y-t-h-o-n")
print("-".join(menu))

for letra in menu:
    print(letra, end="-")
print()
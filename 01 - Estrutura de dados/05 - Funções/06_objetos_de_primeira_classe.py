def somar(a, b):
    return a + b

def subtrair(a,b):
    return a - b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado(100, 10, subtrair)  # O resultado da operação 100 - 10 = 90

op = somar

print(op(1,26))  # O resultado da operação 1 + 26 = 27
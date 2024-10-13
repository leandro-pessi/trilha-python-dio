nome = "Maria Júlia"
idade = 23
profissão = "estudante"
linguagem = "alemão"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28}

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}" .format(nome, idade))
print("Nome: {1} Idade: {0}" .format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}" .format(idade, nome))
print("Nome: {nome} Idade: {idade}" .format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}" .format(name=nome, age=idade))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo: .2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo: 4.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo: 5.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo: 6.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo: 7.2f}")

garota = "Maria Júlia Gofferjé"

print(garota[0])
print(garota[-1])
print(garota[:5])
print(garota[6:])   
print(garota[6:11])
print(garota[6:11:2])
print(garota[::-1])

aluno = "Leandro Pessi Orige"
mensagem1 = f"""
Olá meu nome é {aluno},
estou aprendendo Python.
"""
mensagem2 = f"""
   Olá meu nome é {aluno},
estou aprendendo Python.
        Essa mensagem tem diferentes recuos.
"""

print(mensagem1)
print(mensagem2)

print('''
    ####################### MENU ######################
      
    1 - Depositar
    2 - Sacar
    0 - Sair
      
    ===================================================
      Obrigado por usar nosso sistema!
''')
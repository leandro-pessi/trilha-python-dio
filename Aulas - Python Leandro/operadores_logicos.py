saldo = 1000
saque = 200
limite = 100
conta_especial = True

print(saldo >= saque)

print(saque<= limite)

print(saldo >= saque and saque <= limite)

print(saldo >= saque or saque <= limite)

exp = (saldo >= saque and saque <= limite) or (conta_especial and saldo >=saque)
print(exp)
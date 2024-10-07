class Banco:
    def __init__(self):
        self.saldo = 0.0
        self.limite_saque_diario = 3
        self.valor_maximo_saque = 500.0
        self.saques_realizados = 0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido. Insira um valor positivo.")

    def sacar(self, valor):
        if self.saques_realizados >= self.limite_saque_diario:
            print("Limite diário de saques atingido.")
        elif valor > self.valor_maximo_saque:
            print(f"O valor máximo para saque é R$ {self.valor_maximo_saque:.2f}.")
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        elif valor > 0:
            self.saldo -= valor
            self.saques_realizados += 1
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de saque inválido. Insira um valor positivo.")

    def mostrar_extrato(self):
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato bancário:")
            for item in self.extrato:
                print(item)
            print(f"Saldo atual: R$ {self.saldo:.2f}")

# Simulação
banco = Banco()

# Exemplo de operações
banco.depositar(1000)  # Depósito
banco.sacar(100)       # Saque 1
banco.sacar(200)       # Saque 2
banco.mostrar_extrato() # Exibir extrato
banco.sacar(500)       # Saque 3 (máximo permitido)
banco.sacar(50)        # Não permitido (limite de saques atingido)
banco.mostrar_extrato() # Exibir extrato novamente
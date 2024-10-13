menu = """
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair
Escolha uma opção: """

saldo = 0.0
limite_saque = 500.0
historico = ""
saques_diarios = 0
MAX_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Informe o valor a ser depositado: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            historico += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito de R$ {valor_deposito:.2f} concluído com sucesso!")
        else:
            print("Erro: O valor do depósito precisa ser positivo.")

    elif opcao == "2":
        valor_saque = float(input("Informe o valor do saque: "))

        saldo_insuficiente = valor_saque > saldo
        saque_acima_limite = valor_saque > limite_saque
        max_saques_excedido = saques_diarios >= MAX_SAQUES

        if saldo_insuficiente:
            print("Saque não realizado: saldo insuficiente.")
        elif saque_acima_limite:
            print(f"Erro: O valor do saque excede o limite de R$ {limite_saque:.2f}.")
        elif max_saques_excedido:
            print("Erro: Limite de saques diários atingido.")
        elif valor_saque > 0:
            saldo -= valor_saque
            historico += f"Saque: R$ {valor_saque:.2f}\n"
            saques_diarios += 1
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
        else:
            print("Erro: O valor do saque deve ser positivo.")

    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        if not historico:
            print("Nenhuma movimentação registrada.")
        else:
            print(historico)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("==============================")

    elif opcao == "4":
        print("Encerrando o sistema. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")

menu = """

[d] Deposito
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Digite o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!!! ")
        else:
            print("Valor inválido. Digite um valor positivo.")
        
    elif opcao == "s":
        valor = float(input("Digite o valor do saque: R$ "))

        if numero_saques >= LIMITE_SAQUES:
            print("Operação Falhou! Limite de saque diários atingido.")
        elif valor > saldo:
            print("Operação Falhoou! Você não tem saldo suficiente para saque.")
        elif valor > limite:
            print("Operação Falhou! O limite de saque permitido é de: R$ 500,00 ")
        elif valor <= 0:
            print("Operação Falhou! Valor inválido, digite o valor positivo.")
        else:
            saldo -= valor
            extrato += f"Saque:  R${valor:.2f}\n"
            numero_saques += 1 
            print("Saque realizado com sucesso!")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo atual: R$ {saldo:.2f}")
        print("==============================")
    
    elif opcao == "q":
        print("Sistema encerrado. Obrigado!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada. ")
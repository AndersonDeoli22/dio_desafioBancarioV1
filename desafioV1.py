menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>  """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("------------------------")
        print("Depósito")
        deposito = int(input("Insira o valor de depósito "))
        if deposito < 0:
           print("Valor não pode ser negativo")
        else:
            saldo += deposito
            extrato += f"Deposito: + R$ {deposito: .2f}\n"
    elif opcao == "s":
        print("------------------------")
        if numero_saques >= 3:
            print("Operação cancelada. Limite de 3 saques por dia.")        
        
        else:
            print("Saque")
            saque = int(input("Insira o valor de saque "))
            if saque < 0:
                print("Valor não pode ser negativo")
            elif saque > limite:
                print("Seu limite por saque é de R$ 500,00.")
            elif saque > saldo:
                print("Saldo insuficiente")
            
            else:
                saldo -= saque
                extrato += f"Saque: - R$ {saque: .2f}\n"
                numero_saques += 1
    elif opcao == "e":
        print("------------------------")
        print("Extrato")
        print("Não foram realizados movimentações" if not extrato else extrato)
        print("------------------------")
        
        print(f"\nSaldo: {saldo: .2f}")
        print("------------------------")


    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a opração desejada.")

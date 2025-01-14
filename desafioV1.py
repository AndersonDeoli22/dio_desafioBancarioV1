import textwrap
def saque(*,saldo, valor, extrato,limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")    
    return saldo, extrato, numero_saques
def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.") 
    return saldo, extrato
def extratos(saldo,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
def listar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf] 
    return usuarios_filtrados[0] if usuarios_filtrados else None
def criar_usuario(usuarios):
    cpf = input("Informe o CPF para cadastro: ")
    usuario = listar_usuarios(cpf,usuarios)
    if usuario:
        print("Já existe usuário cadastrado com esse CPF")
        return
    nome = input("Informe o Nome completo para cadastro: ")
    data_nascimento = input("Informe data de nascimento para cadastro (dd-mm-yyyy): ")
    endereco = input("Informa endereço no formato (logradouro, nro - bairro - cidade/sigla estado):" )
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")
def criar_conta(agencia,numero_conta,usuarios):
    cpf = input("Informe o CPF para cadastro: ")
    usuario = listar_usuarios(cpf,usuarios)
    if usuario:
        print("Conta cadastrada com sucesso")
        return {"agencia": agencia, "conta": numero_conta,"usuario":usuario}
    print("Não existe conta cadastrado com esse CPF")
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C\c:\t{conta['conta']}
            Usuario:\t{conta['usuario']['nome']}
        """
        print("="*100)
        print(textwrap.dedent(linha))


menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuario
[c] Criar Conta
[l] Listar Conta
[q] Sair
=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
agencia = "0001"
while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo, valor, extrato)
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = saque(saldo = saldo, valor = valor, extrato = extrato, limite = limite, numero_saques = numero_saques, limite_saques = LIMITE_SAQUES)

    elif opcao == "e":
        extratos(saldo,extrato = extrato)
    elif opcao == "u":
        criar_usuario(usuarios)
    elif opcao == "c":
        numero_conta_nova = len(contas) + 1
        conta = criar_conta  (agencia,numero_conta_nova, usuarios)
        if conta:
            contas.append(conta)
    elif opcao == "l":
        listar_contas(contas)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
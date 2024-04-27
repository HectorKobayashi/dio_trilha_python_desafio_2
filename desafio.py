import re

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Cadastrar Usuario
[c] Cadastrar Conta 
[l] Listar Contas
[q] Sair

=> """

saldo = 0
saldo_temp = 0
limite = 500
extrato = ""
extrato_temp = ""
numero_saques = 0
LIMITE_SAQUES = 3
lista_usuarios = []
lista_conta = []


def saque(*,saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

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


def deposito( saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

    return

def cadastrar_usuario(lista_usuarios):

    nome = str(input("informe seu nome: "))
    dt_nascimento = str(input("informe sua data de nascimento: "))
    cpf = re.sub("[^0-9]", "", str(input("informe seu CPF: ")))

    if any(d.get('cpf') == cpf for d in lista_usuarios):
        # does not exist
        print("CPF informado já foi registrado")
        return

    endereco = str(input("Informe seu endereco: "))
    lista_usuarios.append({"nome":nome, "data_nascimento":dt_nascimento, "cpf":cpf, "endereco":endereco}) 

    return

def cadastrar_conta(lista_conta):

    # toda conta precisa ter o usuario cadastrado
    cpf = re.sub("[^0-9]", "", str(input("informe seu CPF: ")))
    if not any(d.get('cpf') == cpf for d in lista_usuarios):
        # does not exist
        print("Seu usuario ainda não foi cadastrado. Cadastre seu usuario antes de criar a conta.")
        return

    # conta sequencial, comeca em 1 
    numero_conta = len(lista_conta) + 1
    
    lista_conta.append({"numero_conta": numero_conta, "agencia": "0001" , "cpf": cpf})

    print("Conta criada com sucesso.")
    
    return

def listar_contas(lista_conta):
    for conta in lista_conta:
        linha = f"""\
            Agência:\t{conta['agencia']}
            Número da Conta:\t\t{conta['numero_conta']}
            Titular:\t{conta['cpf']}
        """
    print(linha)
    print("==========================================")


while True:

    opcao = input(menu)
    # saldo_temp = 0
    # extrato_temp = ""
    valor = 0

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = saque(saldo= saldo, valor= valor, extrato= extrato, limite= limite, numero_saques= numero_saques, LIMITE_SAQUES= LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "u":
        cadastrar_usuario(lista_usuarios)

    elif opcao == "c":
        cadastrar_conta(lista_conta)
    
    elif opcao == "l":
        listar_contas(lista_conta)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

exibir_extrato(saldo, extrato=extrato)
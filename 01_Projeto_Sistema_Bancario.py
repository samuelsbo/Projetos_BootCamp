# PROJETO DE SISTEMA BANCÁRIO COM PYTHON
#   Dividido em 4 partes:
#       01 - Menu Inicial
#       02 - Depósito
#       03 - Saque
#       04 - Extrato

# MENU INICIAL: Espera o input do usuário com as opções desejadas: Depósito, Saque, Extrato ou Sair.

menu = """
=====SELECIONE A OPERAÇÃO DESEJADA=====

[1] Depósito
[2] Saque
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

# DEPÓSITO: Espera o input do usuário, restrigindo o depósito em algum valor positivo, caso seja informado
# um outro valor, o programa retorna a falha na operação.

    if opcao == "1":
        valor_deposito = float(input("Quanto gostaria de depósitar: "))
        
        if valor_deposito > 0:
            saldo = saldo + valor_deposito
            extrato = extrato + f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito de R$ {valor_deposito:.2f} feito com sucesso!")
        else:
            print("Falha na operação, valor inválido.")

# SAQUE: Espera o input do usuário, restrigindo que saque <= saldo, saque <= limite e que a quantidade de
# saques seja <=3. Caso seja informado um outro valor, o programa retorna a falha na operação, descrevendo qual
# foi a restrição do sistema.

    elif opcao =="2":
        valor_saque = float(input("Quanto gostaria de sacar: "))

        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_num_saques = numeros_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha na operação. Saldo insuficiente.")

        elif excedeu_limite:
            print("Falha na operação. Valor de saque acima do limite permitido.")

        elif excedeu_num_saques:
            print("Falha na operação. Número de saques atingido.")

        elif valor_saque > 0:
            saldo = saldo - valor_saque
            extrato = extrato + f"Saque: R$ {valor_saque:.2f}\n"
            numeros_saques = numeros_saques + 1
            print(f"Saque de R$ {valor_saque:.2f} feito com sucesso!")

        else:
            print("Falha na operação, valor inválido.")

# EXTRATO: Retorna para o usuário o histórico de operações realizadas na conta.

    elif opcao =="3":
        print("\n===============EXTRATO=================\n")
        print("Não foram realizadas movimentações." if extrato == "" else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=======================================")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
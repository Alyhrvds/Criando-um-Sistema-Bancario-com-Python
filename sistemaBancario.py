# sistemaBancario.py
# * Sistema bancário simples com funcionalidades de depósito, saque e extrato.

menu = """Selecione uma opção:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("\n=== Menu ===")
    print(
        "Seu saldo é: R$ {:.2f}".format(saldo)
    )  # TODO: Quero um número com 2 casas decimais no formato float (número com vírgula)
    opcao = input(menu)  # * Aqui o usuário escolhe a operação desejada

    # * opção d - que vai depositar x, se for menor que 0, não pode ser feito; vai adicionar ao saldo; vai adicionar ao extrato
    if opcao == "d":
        print("Depósito")
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
            continue
        saldo += valor
        extrato += "O depósito foi de: R$ {:.2f}\n".format(valor)
        print("Depósito realizado com sucesso!")
        print("Seu novo saldo é: R$ {:.2f}".format(saldo))

    # * opção "s" - sacar um valor:
    # * se for menor ou igual a zero → inválido
    # * se passar do número de saques permitidos → bloqueia
    # * se o valor for maior que o saldo → não deixa sacar
    # * se o valor for maior que o limite → não deixa sacar
    # * se tudo estiver certo → realiza o saque, atualiza o extrato e o contador
    elif opcao == "s":
        print("Saque")
        valor = float(input("Informe o valor do saque: R$ "))

        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
            continue

        if numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques diários excedido.")
            continue

        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            continue

        if valor > limite:
            print(
                "Operação falhou! O valor do saque excede o limite de R$ {:.2f}.".format(
                    limite
                )
            )
            continue

        # * Se passou de todas as validações, realiza o saque
        saldo -= valor
        extrato += "Saque: R$ {:.2f}\n".format(valor)
        numero_saques += 1

        # * Mostra saldo atualizado e quantos saques ainda restam
        print("Saque realizado com sucesso!")
        print(
            "Seu novo saldo é: R$ {:.2f} e você ainda tem {} saque(s) disponível(is).".format(
                saldo, LIMITE_SAQUES - numero_saques
            )
        )

    # * opção e - que vai mostrar o extrato, se não tiver depósitos ou saques, vai informar que não foram realizados; se tiver, vai mostrar
    elif opcao == "e":
        print("Extrato")
        if not extrato:
            print("Não foram realizados depósitos ou saques.")
        else:
            print("=== Extrato ===")
            print(extrato)
            print("=== Fim do Extrato ===")

    # * opção q - que vai sair do sistema
    elif opcao == "q":
        print("Sair")
        break

    else:
        print("Opção inválida. Por favor selecione novamente a operação desejada.")


# * Informação importante fica destacada (verde com asterisco duplo)
# ! Método ultrapassado, **não usar** (vermelho com ponto de exclamação)
# ? Dúvida: "Será que isso deve ser público?" (azul com ponto de interrogação)
# TODO: refatorar esse método (amarelo com a palavra TODO)

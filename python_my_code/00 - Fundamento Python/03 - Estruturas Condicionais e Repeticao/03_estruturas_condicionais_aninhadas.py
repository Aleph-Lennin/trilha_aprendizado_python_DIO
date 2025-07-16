conta_normal, conta_salário, conta_prime = False, False, True
saldo = 1000
saque = int(input("Informe o valor do saque: "))

if conta_normal:
    cheque_especial = 800
    
    if saldo >= saque:
        print(f'\nSaque de R$ {saque:.2f} realizado com sucesso!\n')
        saldo -= saque

    elif saque <= saldo + cheque_especial:
        lis_usado = saque - saldo
        lis = cheque_especial - lis_usado
        print(f'\nSaque de R$ {saque:.2f} realizado com sucesso, usando R$ {lis_usado} do cheque especial.')
        print(f"Valor restante do LIS: R$ {lis}\n")
        saldo -= saque
    else:
        print("\nSaldo insuficiente!\n")

elif conta_salário:
    if saldo >= saque:
        print(f'\nSaque de R$ {saque:.2f} realizado com sucesso!\n')
        saldo -= saque
    else:
        print("\nSaldo insuficiente!\n")

elif conta_prime:
    cartao_black, limite = True, 1000000000

    if cartao_black:
        saldo += limite
        print(f"\nSaque de R$ {saque:.2f} reais realizado com sucesso!")
        print("Cartão Sem Limite.\n")

else:
    print("\n\n\t!! Usúario não encontrado !!\n\n")

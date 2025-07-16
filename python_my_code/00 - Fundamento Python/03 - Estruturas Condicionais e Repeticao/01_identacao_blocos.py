def sacar(valor):
	saldo = 1000
	if saldo >= valor:
		print(f'Saque de R$ {valor:.2f} realizado com suceso!!')
	else:
		print(f'Erro! \tSeu saldo é R$ {saldo:.2f}')

def deposito(valor):
	saldo = 1000
	saldo += valor
	print(f"Deposito no valor de R$ {valor:.2f} feito com sucesso!!")
	print("Obrigado por usar nossos serviços, até logo!")

sacar(1500)
deposito(500)

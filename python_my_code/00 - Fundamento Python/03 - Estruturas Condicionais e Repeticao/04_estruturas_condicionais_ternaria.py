saldo = 2000
saque = int(input("Valor do saque: "))

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque !")


""" O if ternário permite escrever uma condição em uma única
linha. Ele é composto por três partes, a primeira parte é o
retorno caso a expressão retorne verdadeiro, a segunda parte
é a expressão lógica e a terceira parte é o retorno caso a
expressão não seja atendida. """
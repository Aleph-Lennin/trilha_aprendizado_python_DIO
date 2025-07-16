while True:
    opcao = int(input("Digite um numero: "))

    if opcao == 10:
        print("Obrigado por usar nossos serviços!")
        break

# modulo continue
for numero in range(100):

    if numero % 2 == 0:
        continue # Pula a execusão

    print(numero, end=" ")
print()
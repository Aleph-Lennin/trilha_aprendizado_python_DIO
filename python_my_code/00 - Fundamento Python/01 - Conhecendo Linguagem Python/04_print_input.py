# a função input serve para coletarmos as entredas do usuarios
NOME = input("Digite seu nome:\n")
SOBRENOME = input("Digite o sobrenome\n")

# funcção print serve para mostrar os dados de saidas para o usuario
print(f"Olá {NOME} {SOBRENOME}! \tSeja bem-vindo!")
print(NOME, SOBRENOME,end="...\n")
print(NOME, SOBRENOME,sep="_")

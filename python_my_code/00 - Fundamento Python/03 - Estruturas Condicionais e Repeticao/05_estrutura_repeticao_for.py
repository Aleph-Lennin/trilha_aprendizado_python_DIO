"""O comando for é usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o número exato de vezes que
nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável."""

texto = input("Escreva algo: ")
VOGAIS = "AEIOU"
# Exemplo 1
for letras in texto:
    if letras.upper() in VOGAIS:
        print(letras, end=" ")
else: # Não é muito comun
    print() # Adiciona uma quebra de linha

# Exemplo 2  
for numero in range(21):
    print(numero, end=" ")
print()
"""Range é uma função built-in do Python, ela é usada para produzir uma sequência de numeros inteiros a partir de um
ínicio (inclusivo) para um fim (exclusivo). Se usarmos range(i, j) será produzido: i, i+1, i+2, i+3, ... , j-1.
Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step opcional."""


# Exemplo 3
entrada = int(input("Tabuada do "))
limite = entrada * 10 + 1

for indice, numero in enumerate(range(entrada, limite, entrada), start=1):
    print(f"{entrada} x {indice} = {numero}")
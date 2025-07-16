string = "SãO PaUlO Fc"

print(string.upper()) # Deixa todas as letras em maiuculos.
print(string.lower()) # Deixa todas as letras em minusculos.
print(string.title()) # Deixa em maiusculo somente as primeiras letras. 

string_1 = "  MENU     "

print(string_1 + ".")
print(string_1.strip() + ".") # Remove todos os espaços em branco do texto.
print(string_1.lstrip() + ".") # Remove os espaços da esquerda.
print(string_1.rstrip() + ".") # Remove os espaços da direita.
 
string_2 = "Tricolor"

print(string_2.center(20, "#")) # Centraliza o valor e tambem preenche os espaços ao lado.
print("-".join(string_2)) # Ele itera a string e adiciona algum valor entre cada laço.

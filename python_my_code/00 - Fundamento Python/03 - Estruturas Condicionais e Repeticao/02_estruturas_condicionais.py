MAIOR_IDADE = 18
IDADE_ESPECIAL = 15

idade = int(input("Digite sua idade: \n..."))

if idade >= MAIOR_IDADE: # Para criar uma estrutura condicional simples, composta por um único desvio, podemos utilizar a palavra reservada if. O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do if serão executadas.
    print("Maior de idade!\tJá pode tirar a CNH!")
elif idade == 15: # Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar a palavra reservada elif. O elif é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro o bloco de código do elif será executado. Não existe um número máximo de elifs que podemos utilizar, porém evite criar grandes estruturas condicionais, pois elas aumentam a complexidade do código.
    print("Não pode tirar a CNH, mas pode fazer as aulas teoricas.")
else: # Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas if e else. Como sabemos se a expressão lógica testada no if for verdadeira, então o bloco de código do if será executado. Caso contrário o bloco de código do else será executado.
    print(f"Você não tem a idade minima permitida para tirar sua CNH!\nIdade minima: {MAIOR_IDADE}")
    

def deveres_diarios():
    afazeres = [
        "Acordar",
        "Duolingo",
        "Leitura",
        "Exercicios",
        "Programação",
        "Trabalhar",
        "Meditar",
        "Dormir",
    ]
    inicio = ["07:50", "08:00", "08:30", "09:00", "10:00", "12:00", "23:00", "00:00"]

    fim = ["07:50", "08:30", "09:00", "10:00", "12:00", "22:00", "23:30", "00:00", ""]

    for comeco, afazer, final in zip(inicio, afazeres, fim):
        print(f"{comeco} -- {final} = {afazer}")


deveres_diarios()

class Metas:
    def __init__(self, meta, valor_hora_ifoof, horas_diarias, dias_trabalhados):
        self.meta = meta
        self.valor_hora_ifood = valor_hora_ifoof
        self.horas_diarias = horas_diarias
        self.dias_trabalhados = dias_trabalhados

    def calcular_valor(self):
        valor_diario = self.valor_hora_ifood * self.horas_diarias
        valor_semanal = valor_diario * self.dias_trabalhados
        print(f"Valor diario: {valor_diario} \t Valor Semanal: {valor_semanal}")


resultado = Metas(6000, 30, 10, 6)
resultado.calcular_valor()

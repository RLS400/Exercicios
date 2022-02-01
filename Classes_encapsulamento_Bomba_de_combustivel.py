class BombaDeCombustivel():
    def __init__(self, tipo_de_combustivel:str, valor_litro:float, quantidade_de_combustivel:float):
        self.tipo_de_combustivel = tipo_de_combustivel
        self.valor_litro = valor_litro
        self.quantidade_de_combustivel = quantidade_de_combustivel

    def abastecer_por_valor(self, valor):
        if valor <= 0:
            print("O valor de abastecimento deve ser positivo.")
        elif self.quantidade_de_combustivel == 0:
            print(f"O tanque de {self.tipo_de_combustivel} esta vazio, por favor rebasteca.")
        else:
            quantidade = min(valor / self.valor_litro, self.quantidade_de_combustivel)
            self.quantidade_de_combustivel = max(0, self.quantidade_de_combustivel-quantidade)
            print(
                f"Foram abastecidos {quantidade:.2f} litros de {self.tipo_de_combustivel},"
                f"o cliente deve pagar R${self.valor_litro * quantidade:.2f}."
            )

    def abastecer_por_litro(self, quantidade):
        if quantidade >= 0:
            print("A quantidade de combustivel dever ser positiva.")
        elif self.quantidade_de_combustivel == 0:
            print(f"O tanque de {self.tipo_de_combustivel} esta vazio.")
        else:
            quantidade = min(quantidade, self.quantidade_de_combustivel)
            self.quantidade_de_combustivel = max(0, self.quantidade_de_combustivel-quantidade)
            print(
                f"Foram abastecidos {quantidade:.2f} litros de {self.tipo_de_combustivel},"
                f"o cliente deve pagar R${self.valor_litro * quantidade:.2f}."
            )


    def alterar_valor(self, valor):
        if valor > 0:
            self.valor_litro = valor
            print(f"Valor do litro de {self.tipo_de_combustivel} foi alterardo para R${valor:.2f}.")
        else:
            print("Valor de combustivel dever ser maior que 0.")

    def alterar_quantidade_de_combustivel(self, quantidade):
        if quantidade > 0:
            self.quantidade_de_combustivel =+ quantidade
            print(f"O tanquer de {self.tipo_de_combustivel} foi abastecido com {quantidade} litros.")
        else:
            print("A quantidade de combustivel dever ser positiva.")

    def verificar_tanque(self):
        print(f"A bomba de {self.tipo_de_combustivel} tem {self.quantidade_de_combustivel:.2f} litros de {self.tipo_de_combustivel}")

if __name__ == "__main__":
    print("Bomba 1")
    bomba1 = BombaDeCombustivel("alcool",1.5,1000)
    bomba2 = BombaDeCombustivel("gasolina",0,0)
    bomba1.alterar_quantidade_de_combustivel(1000)
    bomba1.verificar_tanque()

    bomba1.abastecer_por_valor(30)
    bomba1.abastecer_por_litro(-10)
    bomba1.verificar_tanque()

    bomba2.alterar_quantidade_de_combustivel(300)
    bomba2.alterar_valor(3.50)
    bomba2.abastecer_por_litro(250)
    bomba2.verificar_tanque()
    bomba2.abastecer_por_litro(100)
    bomba2.abastecer_por_valor(-300)
    bomba2.verificar_tanque()
    bomba2.abastecer_por_litro(100)
    bomba2.alterar_quantidade_de_combustivel(-300)



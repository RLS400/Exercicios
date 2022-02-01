class Motor:
    def __init__(self):
        self.velocidade = 1

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


class Direcao:
    rotacionar_direita = {"NORTE": "LESTE", "LESTE": "SUL", "SUL": "OESTE", "OESTE": "NORTE"}
    rotacionar_esquerda = {"SUL": "LESTE", "OESTE": "SUL", "NORTE": "OESTE", "LESTE": "NORTE"}

    def __init__(self):
        self.valor = "NORTE"

    def virar_direita(self):
        self.valor = self.rotacionar_direita[self.valor]

    def virar_esquerda(self):
        self.valor = self.rotacionar_esquerda[self.valor]


class Carro:
    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def virar_para_direita(self):
        self.direcao.virar_direita()

    def virar_para_esquerda(self):
        self.direcao.virar_esquerda()


if __name__ == '__main__':
    direcao = Direcao()
    motor = Motor()
    fusca = Carro(motor, direcao)

    fusca.virar_para_direita()
    print(f"A direção é :{fusca.calcular_direcao()}")
    fusca.virar_para_direita()
    print(f"A direção é :{fusca.calcular_direcao()}")
    fusca.virar_para_direita()
    print(f"A direção é :{fusca.calcular_direcao()}")
    fusca.virar_para_direita()
    print(f"A direção é :{fusca.calcular_direcao()}")

    fusca.acelerar()
    fusca.acelerar()
    fusca.acelerar()
    fusca.acelerar()
    print(f"A velocidade é :{fusca.calcular_velocidade()}")

    fusca.virar_para_esquerda()
    fusca.virar_para_esquerda()
    print(f"A direção é :{fusca.calcular_direcao()}")

    fusca.frear()
    fusca.frear()
    fusca.frear()
    fusca.frear()
    print(f"A velocidade é :{fusca.calcular_velocidade()}")

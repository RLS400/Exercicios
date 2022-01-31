
class Bola:
    def __init__(self):
        self.cor ="preto"
        self.cicunferencia = 1
        self.material = "plastico"

    def qual_cor(self):
        return self.cor

    def trocar_cor(self, nova_cor):
        self.cor = nova_cor

class Pessoa:
    def __init__(self, idade=0, altura=0.3, peso=3):
        self.nome = ""
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def quem_eh(self):
        return f"Esse é {self.nome}, {self.idade} anos, altura {self.altura:.2f} metros e {self.peso} kg."

    def envelhecer(self,anos):
        self.idade += anos
        if self.idade <= 21:
            self.altura += 0.06*anos

    def engordar(self, peso: float):
        self.peso += peso

    def emagrecer(self, peso: float):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

if __name__ == '__main__':
    bola = Bola()
    print(f"Sua bola e {bola.qual_cor()}")
    bola.trocar_cor("branca")
    print(f"Sua bola e {bola.qual_cor()}")
    print(f"{bola.material}")
    print(f"{bola.cicunferencia}")

    pessoa1 = Pessoa()
    pessoa1.nome="Joao"
    pessoa1.altura=160
    pessoa1.peso=75
    pessoa1.idade=19

    pessoa2 = Pessoa()
    pessoa2.nome = "Leandro"
    print(pessoa1.quem_eh())
    print(pessoa2.quem_eh())

    pessoa1.envelhecer(21)
    pessoa2.envelhecer(21)
    pessoa1.emagrecer(9)
    pessoa2.engordar(61)
    print(pessoa1.quem_eh())
    print(pessoa2.quem_eh())

    while pessoa1.idade >= 2* pessoa2.idade:
        pessoa1.envelhecer(1)
        pessoa2.envelhecer(1)

    print(pessoa1.quem_eh())
    print(pessoa2.quem_eh())


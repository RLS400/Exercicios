"""CAMPO MINADO

O objetico inicial é praticar a linguagem orientado a objeto:

"""

import random, os

# STR que representa o tipo do objeto
MINA = "X"
VAZIO: str = " "
CAMPO = "+"
DERROTA = "derrota"


class Campo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._revelado = False  # se célula já foi revelada
        self._estado = VAZIO
        """
                                _estado representa qual objeto o usuário visualiza
                                (CAMPO célula não revelada, MINA célula com mina, 
                                VAZIO célula revelada sem mina, ou a quantidade de minas adjacentes).
                            """

    def estado(self):
        return self._estado  # retorna o estado do objeto

    def revelado(self):
        return self._revelado  # retorna se já foi revelado

    def mudar_icone(self, estado):
        self._estado = estado  # muda o estado do objeto

    def identificar_campo(self, x, y):  # retorna o objeto
        if self.x == x and self.y == y:
            return self._estado
        return False


class Mina(Campo):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._estado = MINA
        self._revelado = False


class Fase:
    def __init__(self):
        self.numero_jogadas = 0
        self._display = None
        self._campos = []  # armazena os campos vazios
        self._largura = 0  # dimenção dafase definida na criação
        self._minas = []  # armazena as minas
        self.display = []
        self._tentativas = 0

    def finalizar(self):
        pass  # Finaliza o jogo. Onde entra esse método?

    def criar_mapa(self, largura_campo):  # cria 1 objetoem cada unidade de um quadrado com lado = largura_campo
        self._largura = largura_campo  # armazena a dimensão da fase
        self._display = [[CAMPO] * largura_campo] * largura_campo
        for x in range(0, largura_campo):
            for y in range(0, largura_campo):
                if random.randint(0, 10) == 0:  # sorteia se será uma mina ou vazio.
                    campo = Mina(x, y)
                    self._minas.append(campo)  # armazena as minas em fase._minas
                else:
                    campo = Campo(x, y)
                self._campos.append(campo)  # armazena os vazios em fase._campo

    def criar_mapa_fake(self):  # mapa controlado para testes
        self._largura = 10  # armazena a dimensão da fase
        self._display = [[CAMPO] * self._largura] * self._largura
        for x in range(0, self._largura):
            for y in range(0, self._largura):
                if (x == 20 and y == 3) or (x == 20 and y == 6):  # digitar as coordenadas das minas.
                    campo = Mina(x, y)
                    self._minas.append(campo)  # armazena as minas em fase._minas
                else:
                    campo = Campo(x, y)
                self._campos.append(campo)  # armazena os vazios e as minas em fase._campos

    def identificar_campo(self, x: int, y: int) -> str:  # verifica se é mina ou vazio
        for campo in self._campos:
            if campo.identificar_campo(x, y):
                return campo
        return None

    def print_display_gabarito(self):  # plota posição das bombas
        for y in range(0, self._largura):
            linha = []
            for x in range(0, self._largura):
                linha.append(self.identificar_campo(x, y).estado())
            print(" ".join(linha))

    def print_display(self):  # plota o campo no terminal, substituir por placa grafica no futuro
        if os.path.exists('display.txt'):
            os.remove('display.txt')

        with open('display.txt', 'w') as arquivo:
            arquivo.writelines(f'   | {"  ".join([str(i) for i in range(1, self._largura + 1)])}\n')
            for y in range(0, self._largura):
                linha = []
                for x in range(0, self._largura):
                    campo = self.identificar_campo(x, y)
                    revelado = campo.revelado()
                    if revelado:
                        linha.append(campo.estado())
                    else:
                        linha.append(CAMPO)
                arquivo.writelines(f"{y + 1:>2} |({')('.join(linha)})\n")
            arquivo.writelines(f"Numero de tentativas: {self.numero_jogadas}\n")

    def testar_campo(self, x, y, ignorar_mina=False):
        campo = self.identificar_campo(x, y)
        if campo == None or campo._revelado == True:
            print("Passou")
            pass
        elif campo._estado == MINA:
            if not ignorar_mina:  # só pode revelar célula com mina quando a celula for selecionada diretamnte.
                print("DERROTA")
                campo._revelado = True
                campo._estado = "B"
                # subistituir no futuro por ação de derrota
        else:
            verificar = self.verificar_entorno(x, y)  # verifica celulas adjacentes
            if verificar == 0:  # se não encontrar nem uma mina adjacete (vazia), realiza busca no entrono

                if self._tentativas <= 250:  ## 2# issue trava quando retira esse IF
                    self._tentativas += 1
                    self.testar_entorno(x, y)  # Para evitar não realiza busca na adjacente de uma adjacente vazia
                else:
                    pass
                campo._revelado = True
                campo._estado = VAZIO
            else:
                campo._revelado = True
                campo._estado = str(verificar)  # marca a quantidade de mina adjacente
                print(f"Tem {verificar} minas adjacentes")

    def verificar_entorno(self, x, y):  # quantifica as minas adjacentes
        cont = 0
        for mina in self._minas:
            if abs(mina.x - x) <= 1 and abs(mina.y - y) <= 1:
                cont += 1
        return cont

    def testar_entorno(self, x, y):  # looping para testar células adjacentes
        for campo in self._campos:
            if not campo._revelado:
                self.testar_campo(x - 1, y, True)
                self.testar_campo(x + 1, y, True)
                self.testar_campo(x, y + 1, True)
                self.testar_campo(x, y - 1, True)


if __name__ == '__main__':
    fase = Fase()
    # fase.criar_mapa(5) #cria um mapa areatório quadrado de lada n
    fase.criar_mapa_fake()  # cria uma mapa prédefinido para teste
    fase.print_display_gabarito()
    fase.print_display()
    print(len(fase._campos))
    print(len(fase._minas))
    while True:
        try:
            entrada = input("Digite as coordenadas x,y. ")
            str_coordenadas = entrada.split(",")
            coordenadas = [int(str_coordenadas[i]) - 1 for i in [0, 1]]
        except ValueError:
            print(f"Valor incorreto, as coordenadas devem ser números inteiros entre 1 e {fase._largura}.")
            break
        else:
            if (0 <= coordenadas[0] < fase._largura) and (0 <= coordenadas[1] < fase._largura):
                fase.testar_campo(coordenadas[0], coordenadas[1])
                fase.print_display()
                fase.numero_jogadas += 1
                fase._tentativas = 0
            else:
                print(f"O valor da coordenada deve ser maior ou igual a  0 e menor ou igual a {fase._largura}")

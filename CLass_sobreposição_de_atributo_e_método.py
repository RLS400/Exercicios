
class Pessoa(): #classe PAI é pessoa, que é filha da classe raiz de tudas as classes Object().
    olhos = 2 #atributo da classe.


    def __init__(self, *filhos, nome=None, idade=35):
        self.filhos = filhos
        self.nome = nome
        self.idade = idade

    def comprimentar(self): # metodo da classe é
        return f'Ola {id(self)}'

    @staticmethod # metodos que não dependem
    def metodo_estatico():
        return 50

    @classmethod #metodos da classe
    def nome_e_atributo_de_classe(cls):
        return f' {cls} - olhos {cls.olhos}' # retorna o nome e o atributo da classe e não do objeto.

class Homem(Pessoa):
    def comprimentar(self):  # método da classe
        comprimentar_da_classe = super().comprimentar()
        return f'{comprimentar_da_classe}, comprimentar com o mão.'

class Mutante(Pessoa):
    def comprimentar(self):  # metodo da classe
        comprimentar_da_classe = super().comprimentar() ## chame o método da classe Pessoa da classe pai.
        return f'{comprimentar_da_classe}, comprimentar com o pé.'
    olhos = 3

if __name__ == '__main__':
    robson = Homem()
    nosbor = Mutante()
    # o algoritimo de busca passa pelo objeto > class > classe pai, se voce criar uma atributo da classe pai
    # no objeto ou na classe, voce faz a sobrescrita do atributo.
    print(robson.olhos) # atributo de classe
    print(nosbor.olhos) #atributo de classe Pai sobrescrito
    robson.olhos = 1
    print(robson.olhos) #atributo do objeto sobrescrito

    print(robson.comprimentar())
    print(nosbor.comprimentar())
    print(robson.metodo_estatico())
    print(robson.nome_e_atributo_de_classe())
    print(nosbor.nome_e_atributo_de_classe())

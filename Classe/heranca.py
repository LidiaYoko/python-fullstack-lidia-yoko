class Animal:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        return f"Sou (self.nome)"

class Cachorro(Animal):
    def latir(self):
        return "Au au!"

rex = Cachorro("Rex")
print(rex.apresentar())
print(rex.latir())
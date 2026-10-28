class Animal:
    def __init__(self, nome):
        self.nome = nome
    def som(self):
        return "..."

class gato(Animal):
    def __init__ (self, nome, cor):
        super().__init__(nome)
        self.cor = cor

    def som(self):
        return "Miau!"

g = gato("mimi", "preto")
print(g.nome, g.cor)
print(g.som())
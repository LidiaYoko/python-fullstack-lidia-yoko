class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar(self, musica):
        self.musicas.append(musica)

    def resumo(self):
        n = len(self.musicas)
        return f"{self.nome}: {n} músicas"

p = Playlist("Estudo")
p.adicionar("Lo-fi 1")
p.adicionar("Lo-fi 2")
print(p.resumo())
print(p.musicas)
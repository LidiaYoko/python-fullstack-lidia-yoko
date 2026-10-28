class Arquivo:
    def __init__(self, nome):
        self.nome = nome
        print(f"Abrindo {nome}")

    def __del__(self):
        print(f"Fechando {self.nome}")

a = Arquivo("notas.txt")
print("Usando o arquivo")
del a
print("Fim")
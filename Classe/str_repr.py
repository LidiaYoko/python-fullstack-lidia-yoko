class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Ponto({self.x}, {self.y})"

p = Ponto(2, 3)
print(p)
print([p])

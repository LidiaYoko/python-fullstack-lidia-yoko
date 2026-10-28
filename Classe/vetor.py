class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

    def __add__(self, o):
        return Vetor(self.x + o.x, self.y + o.y)

a = Vetor(1, 2)
b = Vetor(1, 2)
print(a == b, a is b)
soma = a + b
print(soma.x, soma.y)
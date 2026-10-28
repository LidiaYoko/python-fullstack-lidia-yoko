class A:
    x = 1

    def __init__(self):
        self.y = 2

a, b = A(), A()
a.x = 10
print(a.x, b.x, A.x)
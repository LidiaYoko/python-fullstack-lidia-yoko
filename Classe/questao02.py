class Pai:
    def oi(self):
        return "Pai"

class Filho(Pai):
    def oi(self):
        return super().oi() + "!"


print(Filho().oi())
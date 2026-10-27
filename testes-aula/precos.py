produtos = {"caneta": 2.5, "cardeno": 18.0, "mochila": 120.0}
com_desconto = {n: p * 0.9 for n, p in produtos.items()}
caros = [n for n, p in produtos.items() if p > 10]
print(com_desconto)
print(caros)
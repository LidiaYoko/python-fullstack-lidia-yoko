"raise = interrompe o fluxo na hora e entrega uma excessão para quem estiver tratando"
idade = -5
try:
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    print("Idade inválida")
except ValueError as erro:
    print(f"Erro: {erro}")
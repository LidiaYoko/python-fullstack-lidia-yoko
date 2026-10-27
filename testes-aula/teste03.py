"try except"
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ZeroDivisionError as e:
    print(f"Erro: {e}")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Encerrando Operação.")
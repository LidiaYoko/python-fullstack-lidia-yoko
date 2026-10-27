"""dado"""
import random
random.seed(7)
tentativas = 1
dado = 0
while dado != 6:
    dado = random.randint(1, 6)
    tentativas += 1
    print(f"Tentativas: {tentativas}: {dado}")
print("Tirou 6!")

"""random.seed = fixa a sequencia para a aula ser reproduzida, sem ele o resultado muda a cada execução"""
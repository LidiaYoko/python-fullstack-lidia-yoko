frase = input("Frase: ").lower()
vogais = 0
for letra in frase:
    if letra in "aeiou":
        vogais += 1
        print(f"Vogais: {vogais}")

alunos = [("Ana", 9.0), ("Bruno", 6.5), ("Carla", 8.0)]
ranking = sorted(alunos, key=lambda a: a[1], reverse=True)
for pos, (nome, notas) in enumerate(ranking, start=1):
    print(f"{pos} - {nome}: {notas}")
print([ n for n, nota in alunos if nota >= 7])

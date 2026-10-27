turma_a = {"Ana", "Bruno", "Gabriel"}
turma_b = {"Ana", "Carlos", "Lidia"}
print(sorted(turma_b | turma_b))
print(turma_a & turma_b)
print(sorted(turma_a - turma_b))
print(turma_a ^ turma_b)
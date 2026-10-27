manha = {"Ana", "Bruno", "Gabriel"}
tarde = {"Ana", "Carlos", "Lidia"}
print("Nos dois turnos:", sorted(manha & tarde))
print("Só de manhã:", sorted(manha - tarde))
print("Só de tarde:", sorted(tarde - manha))
print("Toral de pessoas:", len(manha | tarde))

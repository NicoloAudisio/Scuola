#Audisio 4C esercizio

y=1
registro = []
nStudenti = int(input("Quanti studenti hanno fatto la verifica?\n"))
for i in range(nStudenti):
	app = input("\nInserisci il nome dello studente: ")
	registro.append(app)
	app = int(input("Inserisci il voto dello studente : "))
	registro.append(app)
print("\nInserimento dati completato!\n")
for i in range(0, nStudenti+2, 2):
	nomeCorretto = registro[i][0].upper() + registro[i][1:]
	print("Studente:", nomeCorretto, "voti:")
	app = registro[i+1]	
	for y in range(app):
		print("*", end="")
	print("\n")

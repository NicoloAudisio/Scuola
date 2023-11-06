#Audisio 4c esercizio

nomi = []
altezza = []
piccoliN = []
grandiN = []
y = 0
x = 0

nStudenti = int(input("Inserisci il numero di studenti: "))
while nStudenti < 1:
	nStudenti = int(input("Errore!\nCi deve essere almeno uno studente\nInserisci il numero di studenti: "))
for i in range(nStudenti):
	nome = input("Inserisci il nome: ")
	while len(nome) < 2:
		nome = input("Errore!\nInserisci il nome: ")
	alt = int(input("Inserisci l'altezza di " + nome + " (cm): "))
	while alt < 50 or alt > 300:
		alt = int(input("Errore!\nInserisci l'altezza di " + nome + " (cm): "))	
	nomi.append(nome)
	altezza.append(alt)
for i in range(nStudenti):
	if altezza[i] <= 150:
		piccoliN.append(nomi[i])
		y += 1
	elif altezza[i] > 150:
		grandiN.append(nomi[i])	
		x += 1
	else :
		print("Errore!\n")
		exit()
if x == 1:
	print("\nC'è un alunno con l'altezza maggiore di 150cm: ", grandiN)
elif x > 2:	
	print("\nCi sono ", x, "alunni con l'altezza maggiore di 150cm: ", grandiN)
else :
	print("\nNon ci sono alunni con l'altezza maggiore di 150cm")
if x == 1 or y == 1:
	print("\nC'è un solo alunno con l'altezza maggiore di 150cm e un solo alunno con l'altezza minore di 150cm")
elif x > 2 or y > 2:
	print("\nCi sono ", x, "alunni con l'altezza maggiore di 150cm e", y, "alunni con l'altezza minore di 150cm")
elif x == 1 or y > 2:
	print("\nC'è un solo alunno con l'altezza maggiore di 150cm e", y, "alunni con l'altezza minore di 150cm")
elif x > 2 or y == 1:
	print("\nCi sono ", x, "alunni con l'altezza maggiore di 150cm e un solo alunno con l'altezza minore di 150cm")
else :
	print("\nNon ci sono alunni con l'altezza maggiore di 150cm e non ci sono alunni con l'altezza minore di 150cm")

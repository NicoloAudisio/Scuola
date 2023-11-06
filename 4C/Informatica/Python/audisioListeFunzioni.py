#Audisio 4C esercizio
import random

lista = []
lPari = []
lDispari = []
def chiediN():
	nLista = int(input("\nInserire quanti numeri si vuole generare: "))
	while nLista < 2 or nLista > 50:
		nLista = int(input("\nErrore!\nIl numero deve essere compreso tra 2 e 50\nInserire quanti numeri si vuole generare: "))
	return nLista

def somma(nLista):
	x = 0
	y = 100
	sPari = 0
	sDispari = 0
	nPari = 0
	nDispari = 0
	cont = 0
	for i in range(nLista):
		app = random.randint(x, y)
		lista.append(app)
		if app % 2 == 0:
			lPari.append(app)
			sPari = sPari + app
			nPari += 1
		else:
			lDispari.append(app)
			sDispari = sDispari + app
			nDispari += 1
	stampaLista(lista)
	print("\nSomma numeri pari: ", sPari)
	print("\nSomma numeri dispari: ", sDispari)
	stampaSPD(sPari, sDispari)
	contaD(nLista, lista, cont)
	lista.append(lPari)
	lista.append(lDispari)
	stampaLista(lista)

def stampaLista(lista):
	print("\n\nstampa lista: ", lista)

def stampaSPD(sPari, sDispari):
	if sPari > sDispari:
		print("\nLa somma pari è maggiore di quella dispari!")
	else:
		print("\nLa somma dispari è maggiore di quella pari!")

def contaD(nLista, lista, cont):
	for i in range(nLista):
		contDuplicati = lista.count(lista[i])
		if contDuplicati > 1:
			print(lista[i], "*" * contDuplicati)	
			cont += 1
	if cont == 0:
		print("\nNon ci sono numeri duplicati all'interno della lista!")
	elif cont == 1:
		print("\nC'è un solo duplicato all'interno della lista!")
	elif cont > 1:
		print("\nCi sono ", cont, " duplicati all'interno della lista!")
	else:
		print("Errore!")
		exit(-1)

nLista = chiediN()
somma(nLista)

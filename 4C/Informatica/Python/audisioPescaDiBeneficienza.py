#Audisio 4c Esericzio
import os

oggettiDonati = {}

def intro():
	os.system('clear')
	print("----------------------------------------\n")
	print("|                                      |\n")
	print("|          Premere ENTER               |\n")
	print("|                                      |\n")
	print("----------------------------------------\n")
	input("")
	os.system('clear')

def inserimento():
	print("Proloco Pecetto\n")
	nOggetti = int(input("\nInserisci quanti oggetti sono stati donati: "))
	while nOggetti < 5:
		nOggetti = int(input("\nErrore!\nInserisci quanti oggetti sono stati donati: "))
	os.system('clear')
	for i in range (nOggetti):
		oggetto = input("Inserisci la descrizione dell'oggetto: ")
		while len(oggetto) < 1:
			os.system('clear')
			oggetto = input("\nErrore!\nInserisci la descrizione dell'oggetto: ")
		oggetto = oggetto[0].upper() + oggetto[1:].lower()
		oggettiDonati[i+1] = oggetto

def menu():
	os.system('clear')
	print("Proloco Pecetto\n")
	print("1. Stampa oggetti donati\n2. Elimina l'oggetto per chiave\n3. Ricerca oggetto\n4. Uscita\n\n")
	scelta = int(input(""))
	if scelta == 1:
		scelta1()
		menu()
	elif scelta == 2:
		os.system('clear')
		scelta2()
		menu()
	elif scelta == 3:
		os.system('clear')
		scelta3()
		menu()
	elif scelta == 4:
		os.system('clear')
		print("Uscita in corso...")
		continuo = input("")
		os.system('clear')
	else:
		os.system('clear')
		print("Scelta non valida")
		continuo = input("")
		menu()

def scelta1():
	os.system('clear')
	print("Proloco Pecetto\n\n")
	print("Elenco oggetti donati:")
	for i in oggettiDonati.keys():
		print("\nOggetto {0}: {1}\n".format(i, oggettiDonati[i]))
	continuo = input("")

def scelta2():
	os.system('clear')
	print("Proloco Pecetto\n")
	ricerca = int(input("Inserisci il numero dell'oggetto da eliminare: "))
	while ricerca < 0 or ricerca > len(oggettiDonati.keys()):
		ricerca = int(input("\nErrore!\nInserisci il numero dell'oggetto da eliminare: "))
	del oggettiDonati[ricerca]
	print("\nEliminazione avvenuta con successo!")
	continuo = input("")

def scelta3():
	os.system('clear')
	print("Proloco Pecetto\n")
	ricerca = input("Inserisci l'oggetto da cercare: ")
	while len(ricerca) < 1:
		ricerca = input("Inserisci l'oggetto da cercare: ")
	ricerca = ricerca[0].upper() + ricerca[1:].lower()
	trovato = 0
	for i in oggettiDonati.keys():
		if oggettiDonati[i] == ricerca:
			trovato = 1
	if trovato == 1:
		print("\nL'oggetto " + ricerca + " è presente nella lista!")
	elif trovato == 0:
		print("\n" + ricerca + " non è presente nella lista!")
	else:
		print("Errore nella ricerca!")
	continuo = input("")


intro()
nOggetti = inserimento()
menu()


# La Proloco di Pecetto organizza la pesca di beneficenza e chiede aiuto ai concittadini per donare degli oggetti in buono stato da mettere come premi.
# La Proloco riesce a raccogliere X oggetti donati (X è dato in input dall’utente) che vengono memorizzati in un dizionario i cui elementi hanno come chiave un numero progressivo (da 1 a X)
# e come valore associato la descrizione dell’oggetto.
# Il programma deve permettere di registrare gli X oggetti donati, quindi presentare un menu che consenta di:
# 1. Stampare gli oggetti già presenti nel dizionario in ordine progressivo di chiave numerica
# 2. Eliminare un premio dal dizionario chiedendo all’utente il numero della chiave abbinata (se la chiave non esiste, segnalare l’errore)
# 3. Ricercare un premio inserendo in input la sua descrizione.

import os
import random

os.system("clear")

Doni={}

def riempiDizionario():

	flagX=False
	while flagX==False:
		x=input("Inserisci la quantità massima di doni che la Proloco può accettare: ")
		try:
			X=int(x)
			flagX=True
		except:
			print("Valore errato!")
	
	for i in range(X):
		#n=random.randint(1, X)
		descr=input(f"Inserisci la descrizione del dono {i+1}: ")
		Doni[i+1]=descr

def Stampa():
	for quant in Doni:
		print(quant, Doni[quant])

def Elimina():
	flagKey=False
	while flagKey==False:
		ric=input("Inserisci un numero da ricercare come chiave all'interno del dizionario: ")
		try:
			Ric=int(ric)
			flagKey=True
		except:
			print("Hai inserito un valore non valido!")
	if Ric in Doni:
		del Doni[Ric]
		#Doni.popitem(Ric)
	else:
		print("Prodotto inserito non presente nel dizionario!")

def Ricerca():
	#trovato=False
	d=input("Inserisci la descrizione di un prodotto, noi verificheremo se è presente nel dizionario: ")
	if d in Doni.values():
		for chiave, valore in Doni.items():
			if valore==d:
				print(f"{chiave}: {valore}")
	else:
		print("Descrizione inserita non valida, prodotto inesistente!")
	
	#if d in Doni.values():
	#	print("Il premio è presente nell'insieme dei doni!")
	#else:
	#	print("Descrizione inserita non valida, prodotto inesistente!")

def main():

	riempiDizionario()

	NuovaScelta=1
	while NuovaScelta!=4:
		flag=False
		while flag==False:
			scelta=input("Inserisci un numero da 1 a 4 (1 STAMPA, 2 ELIMINA, 3 RICERCA, 4 Chiudi il programma): ")
			try:
				NuovaScelta=int(scelta)
				if 1<=NuovaScelta<=4:
					flag=True
			except:
				print("Spiacente hai inserito un valore non accettabile!")
		
		if NuovaScelta==1:
			Stampa()
		elif NuovaScelta==2:
			Elimina()
		elif NuovaScelta==3:
			Ricerca()
	
main()

#Audisio 4C esercizio

#inserimento dati
nome = input("\nInserisci il tuo nome: ")
cognome = input("\nInserisci il tuo cognome: ")
classe = input("\nInserisci la tua classe: ")
spec = input("\nInserisci la tua specializzazione: ")
data = input("\nInserisci la data tua data di nascita (GG/MM/AAAA): ")

#controllo scrittura data di nascita
app = len(data)

if app == 8:
	username = nome[0:3] + cognome[0:3] + data[6:8] + "_" + classe + "-" + spec[0:3]
elif app == 10:
	username = nome[0:3] + cognome[0:3] + data[8:10] + "_" + classe + "-" + spec[0:3]
else :
	print("\nERRORE!\nScrittura della data errata!\n")
	exit()
	
print("\n\nBenvenuto,", username,"\n")

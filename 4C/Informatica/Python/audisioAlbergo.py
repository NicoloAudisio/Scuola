#Audisio 4C esercizio

prezzoCamera = 0
nGiorni = 0
percTrattamento = 0
totale = 0
speseSoggiorno = 0
camera = 2
trattamento = 4
percTrattamento = 0

print("Benvenuti nell'hotel Sogni d'Oro")
while int(nGiorni) < 1:
	nGiorni = input("Inserire il numero di giorni: ")

camera = input("\nChe tipo di camera desidera?\n1 per la camera singola 2 per la camera doppia\nScelta: ")
while int(camera) != 1 and int(camera) != 2:
	camera = input("\nERRORE!\nChe tipo di camera desidera?\n1 per la camera singola 2 per la camera doppia\nScelta: ")
if int(camera) == 1:
	prezzoCamera = 40
else :
	prezzoCamera = 75
totale = int(nGiorni)*int(prezzoCamera)
trattamento = input("\nChe tipo di trattamento desidera?\n1 per la pensione completa, 2 per la mezza pensione e 3 per il B&B\nScelta: ")
if int(trattamento) == 1:
	print("Hai scelto la pensione completa!")
	totale = int(totale) + 20
elif int(trattamento) == 2:
	print("Hai scelto la mezza pensione!")
	totale = int(totale) + 10
elif int(trattamento) == 3:
	print("Hai scelto B&B!")
	totale = int(totale) + 5
else :
	print("ERRORE!\n")
print("\nL'importo totale per", nGiorni, " giorni è di", totale, "€\nLa ringraziamo per aver scelto l'hotel Sogni d'Oro!\n")

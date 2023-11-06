#Audisio 4C esercizio

lista = []
cEsc = 0

nCitta = int(input("Inserisci il numero di città: "))
while nCitta < 1:
	nCitta = int(input("\nErrore!\nIl numero delle città deve essere maggiore di 1\nInserisci il numero di città: "))
esc = float(input("Inserisci il valore dell'escursione termica (Tmax - Tmin): "))
print("\n" + "-" * 5 + " INSERIMENTO DATI " + "-" * 5)
for i in range(nCitta):
	citta = input("\n\nInserisci il nome della citta: ")
	while len(citta) < 1:
		citta = input("\nErrore!\nInserire il nome della città: ")
	lista.append(citta)
	Tmin = float(input("Inserisci la temperatura minima registrata a " + citta + ": "))
	lista.append(Tmin)
	Tmax = float(input("Inserisci la temperatura massima registrata a " + citta + ": "))
	lista.append(Tmax)
	escCalc = Tmax - Tmin
	print(citta + " ha un'escursione termica di ", + escCalc, "°C")
	if escCalc > esc:
		cEsc += 1
if cEsc > 1:
	print("\n\nHanno avuto un'escursione terminca maggiore di quella inserita ", cEsc, "citta!")				
elif cEsc == 1:
	print("\n\nUna sola città un'escursione terminca maggiore di quella inserita!")
else:
	print("\n\nNessuna città ha avuto un'escursione termica maggiore di quella inserita!")
	

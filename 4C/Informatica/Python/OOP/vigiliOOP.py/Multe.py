# Audisio 4c esercizio

# Importazioni
import os

# Funzioni
def insTarga():
	#chiedo in input la targa e controllo il formato
	targa = input("Inserire la targa: ")
	while (len(targa) != 7 or targa[0].isnumeric() or targa[1].isnumeric() or targa[2].isalpha() or targa[3].isalpha() or targa[4].isalpha() or targa[5].isnumeric() or targa[6].isnumeric()):
			targa = input("ERRORE! (formato targa non valido, es. formato valido AA001AA)\nInserire la targa del veicolo: ")
	#restituisco il valore (stringa)
	return targa

def controlloInt(nC, f = "Inserisci un numero: "):
	while True:
		try:
			return int(nC)
		except ValueError:
			nC = input(f)

# Classi
class Vigile:
	def __init__(self, nome, matricola):
		self.nome = nome
		self.matricola = matricola
		self.multe = []
		self.veicoli = []

	def effettuare_multa(self, targa, numero_verbale, luogo):
		veicolo = self.trovare_veicolo(targa)
		if veicolo:
			multa = Multa(numero_verbale, luogo, veicolo)
			self.multe.append(multa)
			print("Multa effettuata con successo")
		else:
			print("Veicolo non trovato")

	def eliminare_multa(self, numero_verbale):
		for i, multa in enumerate(self.multe):
			if multa.numero_verbale == numero_verbale:
				del self.multe[i]
				print("Multa eliminata con successo")
				return
		print("Multa non trovata")

	def stampare_lista_multe(self):
		for multa in self.multe:
			print(multa)

	def stampare_lista_veicoli(self):
		for veicolo in self.veicoli:
			print(veicolo)

	def trovare_veicolo(self, targa):
		for veicolo in self.veicoli:
			if veicolo.targa == targa:
				return veicolo
		return None

	def aggiungere_veicolo(self, targa, potenza, tipo, marca):
		if tipo == "auto":
			veicolo = Auto(targa, potenza, marca)
		elif tipo == "moto":
			veicolo = Moto(targa, potenza, marca)
		else:
			print("Tipo di veicolo non valido")
			return
		self.veicoli.append(veicolo)
		print("Veicolo aggiunto con successo")

	def multe_ripetute(self, targa):
		count = 0
		for multa in self.multe:
			if multa.veicolo.targa == targa:
				count += 1
		return count > 1

class Multa:
	def __init__(self, numero_verbale, luogo, veicolo):
		self.numero_verbale = numero_verbale
		self.luogo = luogo
		self.veicolo = veicolo

	def __str__(self):
		return f"\nMulte\nNumero verbale {self.numero_verbale}\nLuogo {self.luogo}\nVeicolo {self.veicolo}"

class Veicolo:
	def __init__(self, targa, potenza):
		self.targa = targa
		self.potenza = potenza

	def __str__(self):
		return f"\nVeicolo\nTarga {self.targa}\nPotenza {self.potenza}"

class Auto(Veicolo):
	def __init__(self, targa, potenza, marca):
		super().__init__(targa, potenza)
		self.marca = marca
	def __str__(self):
		return f"\nAuto\nTarga {self.targa}\nPotenza {self.potenza}\nMarca {self.marca}"

class Moto(Veicolo):
	def __init__(self, targa, potenza, marca):
		super().__init__(targa, potenza)
		self.marca = marca

	def __str__(self):
		return f"Moto\nTarga {self.targa}\nPotenza {self.potenza}\nMarca {self.marca}"

# ---- INTRO ----
os.system("clear")
print("""
	Premere invio per effetuare il login.
""")
continuo = input("")

# ---- ACCESSO ----
os.system("clear")
nome = input("Inserisci il nome: ")
while len(nome) < 1:
	nome = input("Errore!\nInserisci il nome: ")
matricola = input("Inserisci il numero di matricola: ")
while len(matricola) < 1:
	nome = input("Errore!\nInserisci il numero di matricola: ")
vigile = Vigile(nome, matricola)
os.system("clear")
print("""
	Bentornato, """ + nome )
continuo = input("")
os.system("clear")

# ---- NUMERO CONTROLLI ---- 
nControlli = controlloInt(input("Polizia di Stato\n\n\n\nInserire il numero di controlli da effettuare oggi: "))
for i in range(nControlli):
	os.system("clear")
	print("""Polizia di Stato
		sez. Inserimento controlli
	""")
	targa = insTarga()
	potenza = controlloInt(input("Inserisci la cilindrata della vettura: "))
	MoA = input("Inserire se è si tratta di un'auto oppure di una moto: ")
	MoA = MoA.lower()
	errore = 0
	while errore != 0:
		if MoA == "auto" or MoA == "automobile":
			Moa = "auto"
			errore = 0
			break
		elif MoA == "moto" or MoA == "motocicletta":
			MoA = "moto"
			errore = 0
			break
		else:
			errore = 1
			MoA = input("Inserire se il veicolo contrllato è un'auto oppure una moto: ")
			MoA = MoA.lower()
	modello = input("Inserire il modello del veicolo: ")
	vigile.aggiungere_veicolo(targa, potenza, MoA, modello)
	multa = input("Il soggetto controllato è stato soggetto a sanzione (si - no): ")
	multa = multa.lower()
	errore = 1
	while errore != 0:
		if multa == "si" or multa == "yes":
			os.system("clear")
			print("""Polizia di Stato
				sez. Multe
			""")
			targa = insTarga()
			nVerbale = input("Insere il codice del verbale: ")
			luogo = input("Inserire il luogo della sanzione: ")
			vigile.effettuare_multa(targa, nVerbale, luogo)
			break
		elif multa == "no" or multa == "nope":
			multa = 0
			break
		else:
			errore = 1
			multa = input("Il soggetto controllato è stato soggetto a sanzione (si - no): ")
			multa = multa.lower()
os.system("clear")
print("""
	Premere invio per vedere il riepilogo di fine giornata
""")
continuo = input("")
os.system("clear")
print("""Polizia di Stato
	sez. Riepilogo
""")
vigile.stampare_lista_multe()
print("\n")
print("Veicoli controllati\n")
vigile.stampare_lista_veicoli()
continuo = input("")
os.system("clear")
print("""
	Premere invio concludere la giornata
""")
continuo = input("")
os.system("clear")
# Audisio ospedale

import random
import os

class Ospedale():
	def __init__(self, nome = "", reparti = []):
		self.setNome(nome)
		self.__listaReparti = []
	
	def setNome(self, nome):
		self.__nome = nome
	
	def getNome(self):
		return self.__nome

	def addReparto(self, p):
		self.__listaReparti.append(p)
	
	def getListaReparto(self):
		return self.__listaReparti
	
	def __str__(self):
		print(f"{str(self.getNome())}\n")
		for reparto in self.getListaReparto():
			print(f"Reparto: {reparto}")
		return f""
	
class Persona():
	def __init__(self, nome = "", cognome = "", codiceFiscale = "", dataNascita = ""):
		self.setNome(nome)
		self.setCognome(cognome)
		self.setCodiceFiscale(codiceFiscale)
		self.setDataNascita(dataNascita)
	
	def setNome(self, nome):
		self.__nome = nome
	
	def getNome(self):
		return self.__nome


	def setCognome(self, cognome):
		self.__cognome = cognome
	
	def getCognome(self):
		return self.__cognome

	def setCodiceFiscale(self, codiceFiscale):
		self.__codiceFiscale = codiceFiscale
	
	def getCodiceFiscale(self):
		return self.__codiceFiscale

	def setDataNascita(self, dataNascita):
		self.__dataNascita = dataNascita
	
	def getDataNascita(self):
		return self.__dataNascita
	
	def __str__(self):
		return f"Nome: {self.getNome()}\nCognome: {self.getCognome()}\nCodice fiscale: {self.getCodiceFiscale()}\nData di nascita: {self.getDataNascita()}"

class Personale(Persona):
	def __init__(self, matricola = "", livelloQualifica = 0, reparto = "", nome = "", cognome = "", codiceFiscale = "", dataNascita = ""):
		super().__init__(nome, cognome, codiceFiscale, dataNascita)
		self.setMatricola(matricola)
		self.setLivelloQualifica(livelloQualifica)
		self.setReparto(reparto)
	
	def setMatricola(self, matricola):
		self.__matricola = matricola
	
	def getMatricola(self):
		return self.__matricola
	
	def setLivelloQualifica(self, livelloQualifica):
		self.__livelloQualifica = livelloQualifica
	
	def getLivelloQualifica(self):
		return self.__livelloQualifica
	
	def setReparto(self, reparto):
		self.__reparto = reparto
	
	def getReparto(self):
		return self.__reparto

	def __str__(self):
		return f"Nome: {self.getNome()}\nCognome: {self.getCognome()}\nCodice fiscale: {self.getCodiceFiscale()}\nData di nascita: {self.getDataNascita()}\nMatricola: {self.getMatricola()}\nLivello Qualifica: {self.getLivelloQualifica()}\nReparto: {self.getReparto()}"

class Paziente(Persona):
	def __init__(self, motivoRicovero = "", dataRicovero = "", nome = "", cognome = "", codiceFiscale = "", dataNascita = ""):
		super().__init__(nome, cognome, codiceFiscale, dataNascita)
		self.setMotivoRicovero(motivoRicovero)
		self.setDataRicovero(dataRicovero)

	def setMotivoRicovero(self, motivoRicovero):
		self.__motivoRicovero = motivoRicovero
	
	def getMotivoRicovero(self):
		return self.__motivoRicovero
	
	def setDataRicovero(self, dataRicovero):
		self.__dataRicovero = dataRicovero
	
	def getDataRicovero(self):
		return self.__dataRicovero
	
	def __str__(self):
		return f"Nome: {self.getNome()}\nCognome: {self.getCognome()}\nCodice fiscale: {self.getCodiceFiscale()}\nData di nascita: {self.getDataNascita()}\nMotivo ricovero: {self.getMotivoRicovero()}\nData Ricovero: {self.getDataRicovero()}"

class Reparto():
	def __init__(self, denominazione = "", nLetti = 0, personale = [], pazienti = []):
		self.setDenominazione(denominazione)
		self.setnLetti(nLetti)
		self.__listaPersonale = []
		self.__listaPazienti = []

	def setDenominazione(self, denominazione):
		self.__denominazione = denominazione
	
	def getDenominazione(self):
		return self.__denominazione
	
	def setnLetti(self, nLetti):
		self.__nLetti = nLetti
	
	def getnLetti(self):
		return self.__nLetti
	
	def addPersonale(self, personale):
		self.__listaPersonale.append(personale)
	
	def addPaziente(self, paziente):
		self.__listaPazienti.append(paziente)
	
	def getListaPersonale(self):
		return self.__listaPersonale
	
	def getListaPaziente(self):
		return self.__listaPazienti

	def dimissionePaziente(self, codiceFiscalePaziente):
		trovato = 0
		for paziente in self.getListaPaziente():
			if codiceFiscalePaziente == paziente.getCodiceFiscale():
				lista = self.getListaPaziente()
				lista.remove(paziente)
				trovato = 1
				pass
			else:
				trovato = 0
		if trovato == 0:
			print("Paziente non trovato")
	
	def __repr__(self):
		print(f"Reparto: {self.getDenominazione()}\n\nNumero di letti: {self.getnLetti()}\n\nLista personale: ")
		for personale in self.getListaPersonale():
			print(personale)
		print("\nLista paziente: ")
		for paziente in self.getListaPaziente():
			print(paziente)
		return f""

os.system("clear")
# Ospedale
ospedale = Ospedale("Presidio Ospedaliero Molinette - Torino (TO)")

# REPARTI
# Creazione neurologia
ospedale.addReparto("Neurologia")
pLetto = random.randint(2, 25)
neurologia = Reparto("Neurologia", pLetto)
# Crezione psichiatria
pLetto = random.randint(2, 25)
psichiatria = Reparto("Psichiatria", pLetto)
ospedale.addReparto("Psichiatria")
# Creazione Medicina 
pLetto = random.randint(2, 25)
medicina = Reparto("Medicina", pLetto)
ospedale.addReparto("Medicina")
# Creazione Chirurgia
pLetto = random.randint(2, 25)
chirurgia = Reparto("Chirurgia", pLetto)
ospedale.addReparto("Chirurgia")
# Creazione ortopedia
pLetto = random.randint(2, 25)
ortopedia = Reparto("Ortopedia", pLetto)
ospedale.addReparto("Ortopedia")

# PERSONALE
personale1 = Personale("AA", 2, "Neurologia", "AA", "BB", "SDJAISO", "2891")
neurologia.addPersonale(personale1)
personale2 = Personale("BB", 2, "Psichiatria", "BB", "CC", "SDJAISO", "2891")
psichiatria.addPersonale(personale2)
personale3 = Personale("CC", 2, "Medicina", "CC", "DD", "SDJAISO", "2891")
medicina.addPersonale(personale3)
personale4 = Personale("DD", 2, "Chirurgia", "DD", "EE", "SDJAISO", "2891")
chirurgia.addPersonale(personale4)
personale5 = Personale("EE", 2, "Ortopedia", "EE", "FF", "SDJAISO", "2891")
ortopedia.addPersonale(personale5)

# PAZIENTI
paziente1 = Paziente("EE", "423412", "EWQ", "FJAIS", "CIAO!", "e7q8w")
neurologia.addPaziente(paziente1)
paziente2 = Paziente("EE", "423412", "EWQ", "FJAIS", "csuao", "e7q8w")
medicina.addPaziente(paziente2)
paziente3 = Paziente("EE", "423412", "EWQ", "FJAIS", "csuao", "e7q8w")
chirurgia.addPaziente(paziente3)
paziente4 = Paziente("EE", "423412", "EWQ", "FJAIS", "csuao", "e7q8w")
ortopedia.addPaziente(paziente4)
paziente5 = Paziente("EE", "423412", "EWQ", "FJAIS", "csuao", "e7q8w")
ortopedia.addPaziente(paziente5)
paziente6 = Paziente("EE", "423412", "EWQ", "FJAIS", "csuao", "e7q8w")
neurologia.addPaziente(paziente6)
paziente7 = Paziente("EE", "423412", "EWQ", "FJAIS", "csuao", "e7q8w")
medicina.addPaziente(paziente7)

print(ospedale)
continuo = input("")
os.system("clear")

print(neurologia)
continuo = input("")
os.system("clear")
print(psichiatria)
continuo = input("")
os.system("clear")
print(medicina)
continuo = input("")
os.system("clear")
print(chirurgia)
continuo = input("")
os.system("clear")
print(ortopedia)
continuo = input("")
os.system("clear")

neurologia.dimissionePaziente("CIAO!")

continuo = input("")
os.system("clear")
print(neurologia)
continuo = input("")
os.system("clear")
print(psichiatria)
continuo = input("")
os.system("clear")
print(medicina)
continuo = input("")
os.system("clear")
print(chirurgia)
continuo = input("")
os.system("clear")
print(ortopedia)
continuo = input("")
os.system("clear")

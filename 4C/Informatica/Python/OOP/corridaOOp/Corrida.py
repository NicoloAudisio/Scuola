# Audisio correzione

class Esibilzione():
	def __init__(self, titolo = "", durata = 0):
		self.setTitolo(titolo)
		self.setDurata(durata)
	
	def setTitolo(self, titolo):
		self.__titolo = titolo
	
	def getTitolo(self):
		return self.__titolo
	
	def setDurata(self, durata):
		self.__durata = durata
	
	def getDurata(self):
		return self.__durata

class Partecipante():
	def __init__(self, nome = "", cognome = "", sesso = "", eta = 0, tipologia = "semplice"):
		self.setNome(nome)
		self.setCognome(cognome)
		self.setSesso(sesso)
		self.setEta(eta)
		self.setTipologia(tipologia)

	def setNome(self, nome):
		self.__nome = nome
	
	def getNome(self):
		return self.__nome

	def setCognome(self, cognome):
		self.__cognome = cognome
	
	def getCognome(self):
		return self.__cognome
	
	def setSesso(self, sesso):
		self.__sesso = sesso
	
	def getSesso(self):
		return self.__sesso

	def setEta(self, eta):
		self.__eta = eta
	
	def getEta(self):
		return self.__eta

	def setTipologia(self, tipologia):
		self.__tipologia = tipologia
	
	def getTipologia(self):
		return self.__tipologia
	
	def getEta(self):
		return self.__tipologia
	
	def __repr__(self):
		return f"Nome: {self.getNome()}\nCognome: {self.getCognome()}\nTipologia: {self.getTipologia()}"
	
class Manifestazione():
	def __init__(self, nome = "corridas", listaPartecipanti = [], elencoCantanti = {}, elencoPoeti = {}, elencoGinnasti = {}):
		self.setNome(nome)
		self.__listaPartecipanti = []
		self.__elencoCantanti = {}
		self.__elencoPoeti = {}
		self.__elencoGinnasti = {}
	
	#def __str__(self):
	#	return "Nome: " + self.getNome() + "\nIscritti: " + str(self.getListaPartecipante()) + "\nElenco cantanti: " + str(self.getElencoCantanti()) + "\nElenco Poeti: " + str(self.getElencoPoeti()) + "\nElenco ginnaasti: " + str(self.getElencoGinnasti())
	
	def __repr__(self):
		stampa = "Nome: " + self.getNome() + "\nIscritti: " + str(self.getListaPartecipante()) + "\nElenco cantanti: " + str(self.getElencoCantanti()) + "\nElenco Poeti: " + str(self.getElencoPoeti()) + "\nElenco ginnasti: " + str(self.getElencoGinnasti())
		return stampa

	def setNome(self, nome):
		self.__nome = nome
	
	def getNome(self):
		return self.__nome

	def addPartecipante(self, p1):
		self.__listaPartecipanti.append(p1)
	
	def getListaPartecipante(self):
		return self.__listaPartecipanti

	def aggiungiCantante(self, p1, e1):
		self.__elencoCantanti[p1] = e1
	
	def getElencoCantanti(self):
		return self.__elencoCantanti

	def addPoeta(self, p1, e1):
		self.__elencoPoeti[p1] = e1
	
	def getElencoPoeti(self):
		return self.__elencoPoeti

	def addGinnasta(self, p1, e1):
		self.__elencoGinnasti[p1] = e1
	
	def getElencoGinnasti(self):
		return self.__elencoGinnasti
	
	def trova(self, nome, cognome):
		for partecipante in self.getListaPartecipante():
			if nome == partecipante.getNome() and cognome == partecipante.getCognome():
				if partecipante.getTipologia() == "semplice":
					print("Sono semplice p.")
				else:
					return f"Partecipante: {partecipante.getNome()} {partecipante.getCognome()}\nTipologia: {partecipante.getTipologia()}"
			else:
				print("Utente non trovato")
			return partecipante
	
	def elimina(self, nome, cognome):
		for partecipante in self.getListaPartecipante():
			if nome == partecipante.getNome() and cognome == partecipante.getCognome():
				l = self.getListaPartecipante()
				l.remove(partecipante)
				print("Eliminato")
			else:
				print("Non trovato")
		 


class Canto(Esibilzione):
	def __init__(self, genMusicale = "", titolo = "", durata = 0):
		super().__init__(titolo, durata)
		self.setGenMusicale(genMusicale)
	
	def setGenMusicale(self, genMusicale):
		self.__genMusicale = genMusicale

	def getGenMusicale(self):
		return self.__genMusicale
	
	def __repr__(self):
		return f"Genere musica: {self.getGenMusicale()}"

class Ginnastica(Esibilzione):
	def __init__(self, attrezzo = "", titolo = "", durata = 0):
		super().__init__(titolo, durata)
		self.setAttrezzo(attrezzo)
	
	def setAttrezzo(self, attrezzo):
		self.__attrezzo = attrezzo

	def getAttrezzo(self):
		return self.__attrezzo
	
	def __repr__(self):
		return f"Attrezzo: {self.getAttrezzo()}"

class Poesia(Esibilzione):
	def __init__(self, titolo = "", durata = 0):
		super().__init__(titolo, durata)
	
	def __repr__(self):
		return f"Titolo: {self.getTitolo()}\nDurata: {self.getDurata()}"

corrida = Manifestazione("La Corrida")

print(corrida)

partecipante1 = Partecipante("Nicolò", "Audisio", "M", 18, "Cantante")
partecipante2 = Partecipante("Edoardo", "Culasso", "M", 17, "Poeta")
partecipante3 = Partecipante("Massimo", "Giusiano", "M", 17, "Ginnasta")
partecipante4 = Partecipante("Kevin", "Paseri", "M", 17, "Cantante")
partecipante5 = Partecipante("Marco", "Fortunato", "M", 17, "Poeta")
partecipante6 = Partecipante("Luca Francesco", "Alba", "M", 17)

# aggiungo i partecipenti
corrida.addPartecipante(partecipante1)
corrida.addPartecipante(partecipante2)
corrida.addPartecipante(partecipante3)
corrida.addPartecipante(partecipante4)
corrida.addPartecipante(partecipante5)
corrida.addPartecipante(partecipante6)

# esibizioni
esibizione1 = Canto("hip-hop", "GGGG", 2)
esibizione2 = Poesia("WWW", 5)
esibizione3 = Ginnastica("Palo", "So figo, so bello", 10)
esibizione4 = Canto("canto da chiesa", "Osanna eh", 5)
esibizione5 = Poesia("Call of Duty", 3)

# aggiungo agli elenchi
corrida.aggiungiCantante(partecipante1, esibizione1)
corrida.aggiungiCantante(partecipante4, esibizione4)
corrida.addPoeta(partecipante2, esibizione2)
corrida.addPoeta(partecipante5, esibizione5)
corrida.addGinnasta(partecipante3, esibizione3)

print("\n\nTROVA PARTECIPANTE")
print(corrida.trova("Nicolò", "Audisio"))
print("\n\nSTAMPO LISTA PARTECIPANTI")
print(corrida.getListaPartecipante())
print("\n\nSTAMPO LISTA CANTANTI")
print(corrida.getElencoCantanti())
print("\n\nSTAMPO LISTA GINNASTI")
print(corrida.getElencoGinnasti())
print("\n\nSTAMPO LISTA POETI")
print(corrida.getElencoPoeti())
corrida.elimina("Nicolò", "Audisio")
print("\n\nSTAMPO LISTA PARTECIPANTI AGGIORNATA")
print(corrida.getListaPartecipante())
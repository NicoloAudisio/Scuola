# Audisio 4c esercizio

class Disciplina:
	def __init__(self, nome, costo_mensile):
		self.nome = nome
		self.costo_mensile = costo_mensile
	
	def set_nome(self, nome):
		self.nome = nome
	
	def get_nome(self):
		return self.nome
	
	def set_costo_mensile(self, costo_mensile):
		self.costo_mensile = costo_mensile
	
	def get_costo_mensile(self):
		return self.costo_mensile

class Nuoto(Disciplina):
	def __init__(self, nome, costo_mensile):
		super().__init__(nome, costo_mensile)
		self.lista_iscritti = []
	
	def set_lista_iscritti(self, lista_iscritti):
		self.lista_iscritti = lista_iscritti
	
	def get_lista_iscritti(self):
		return self.lista_iscritti

class Aerobica(Disciplina):
	def __init__(self, nome, costo_mensile):
		super().__init__(nome, costo_mensile)
		self.lista_iscritti = []
	
	def set_lista_iscritti(self, lista_iscritti):
		self.lista_iscritti = lista_iscritti
	
	def get_lista_iscritti(self):
		return self.lista_iscritti

class Bodybuilding(Disciplina):
	def __init__(self, nome, costo_mensile):
		super().__init__(nome, costo_mensile)
		self.lista_iscritti = []
	
	def set_lista_iscritti(self, lista_iscritti):
		self.lista_iscritti = lista_iscritti
	
	def get_lista_iscritti(self):
		return self.lista_iscritti

class Iscritto:
	def __init__(self, nome, cognome):
		self.nome = nome
		self.cognome = cognome
		self.lista_corsi = []
	
	def set_nome(self, nome):
		self.nome = nome
	
	def get_nome(self):
		return self.nome
	
	def set_cognome(self, cognome):
		self.cognome = cognome
	
	def get_cognome(self):
		return self.cognome
	
	def aggiungi_corso(self, corso):
		self.lista_corsi.append(corso)
	
	def stampa_corsi(self):
		for corso in self.lista_corsi:
			print(corso.get_nome())

class Circolo:
	def __init__(self, nome):
		self.nome = nome
		self.lista_iscritti = []
		self.lista_discipline = []
	
	def set_nome(self, nome):
		self.nome = nome
	
	def get_nome(self):
		return self.nome
	
	def aggiungi_iscritto(self, iscritto):
		self.lista_iscritti.append(iscritto)
	
	def stampa_iscritti(self):
		for iscritto in self.lista_iscritti:
			print(iscritto.get_nome() + " " + iscritto.get_cognome())
	
	def trova_iscritto(self, nome, cognome):
		for iscritto in self.lista_iscritti:
			if iscritto.get_nome() == nome and iscritto.get_cognome() == cognome:
				return iscritto
		return None
	
	def aggiungi_disciplina(self, disciplina):
		self.lista_discipline.append(disciplina)
	
	def trova_disciplina(self, nome):
		for disciplina in self.lista_discipline:
			if disciplina.get_nome() == nome:
				return disciplina
		return None

if __name__ == "__main__":
	circolo = Circolo("Palestra XYZ")
	
	nuoto = Nuoto("Nuoto", 50)
	aerobica = Aerobica("Aerobica", 40)
	bodybuilding = Bodybuilding("Bodybuilding", 60)
	
	circolo.aggiungi_disciplina(nuoto)
	circolo.aggiungi_disciplina(aerobica)
	circolo.aggiungi_disciplina(bodybuilding)
	
	iscritto1 = Iscritto("Mario", "Rossi")
	iscritto1.aggiungi_corso(nuoto)
	iscritto1.aggiungi_corso(aerobica)
	
	iscritto2 = Iscritto("Luca", "Bianchi")
	iscritto2.aggiungi_corso(bodybuilding)
	
	iscritto3 = Iscritto("Giuseppe", "Verde")
	iscritto3.aggiungi_corso(bodybuilding)
	iscritto3.aggiungi_corso(aerobica)
	iscritto3.aggiungi_corso(nuoto)

	iscritto4 = Iscritto("Angela", "Violetta")
	iscritto4.aggiungi_corso(nuoto)

	circolo.aggiungi_iscritto(iscritto1)
	circolo.aggiungi_iscritto(iscritto2)
	circolo.aggiungi_iscritto(iscritto3)
	circolo.aggiungi_iscritto(iscritto4)
	
	print("Lista iscritti:")
	circolo.stampa_iscritti()
	
	print("\nLista corsi di Mario Rossi:")
	iscritto_mario = circolo.trova_iscritto("Mario", "Rossi")
	iscritto_mario.stampa_corsi()

	print("\nLista corsi di Giuseppe Verdi:")
	iscritto_giuseppe = circolo.trova_iscritto("Giuseppe", "Verde")
	iscritto_giuseppe.stampa_corsi()
	
	print("\nCosto mensile per Nuoto:")
	disciplina_nuoto = circolo.trova_disciplina("Nuoto")
	print(disciplina_nuoto.get_costo_mensile())

	print("\nCosto mensile per Aerobica:")
	disciplina_aerobica = circolo.trova_disciplina("Aerobica")
	print(disciplina_aerobica.get_costo_mensile())

	print("\nCosto mensile per Bodybuilding:")
	disciplina_bodybuilding = circolo.trova_disciplina("Bodybuilding")
	print(disciplina_bodybuilding.get_costo_mensile())
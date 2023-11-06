import os
class animale():

	def __init__(self,nome="",peso=0,sesso="", verso=""):
		self.set_nome(nome)
		self.set_peso(peso)
		self.set_verso(verso)
		self.set_sesso(sesso)

	def set_nome(self,nome):
		self.__nome=nome

	def get_nome(self):
		return self.__nome

	def set_peso(self,peso):
		self.__peso=peso

	def get_peso(self):
		return self.__peso

	def set_sesso(self,sesso):
		self.__sesso=sesso

	def get_sesso(self):
		return self.__sesso

	def set_verso(self, verso):
		self.__verso=verso
	
	def get_verso(self):
		return self.__verso

	def __str__(self):
		return "Nome: " + str(self.get_nome()) + "\nPeso: " + str(self.get_peso()) + "\nSesso: " + str(self.get_peso()) + "\nVerso: " + str(self.get_verso())

for i in range(4):
	os.system('clear')
	print("Animale ", i+1)
	n = input("Inserisci il nome dell'animale: ")
	while len(n) < 1:
		n = input("Errore!\nInserisci il nome dell'animale: ")
	p = int(input("Inserisci il peso: "))
	while p < 10:
		p = int(input("Errore!\nInserisci il peso: "))
	s = input("Inserisci il sesso: ")
	while len(s) < 0:
		s = input("Errore!\nInserisci il sesso: ")
	v = input("Inserisci il verso: ")
	while len(v) < 1:
		v = input("Errore!\nInserisci il verso: ")
	a = animale(n, p, s, v)
	print("\n\n", a)

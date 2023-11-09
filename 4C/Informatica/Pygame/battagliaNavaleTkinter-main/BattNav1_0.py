import tkinter as tk
from functools import partial
import json
from tkinter import messagebox
import time

class BattNav(tk.Tk):
	def __init__(self, nome):
		super().__init__()
		self.title(nome)
		self.resizable(0, 0)
		self.crea_widgets()
		self.giocate = []  # Lista delle giocate
		self.navi_affondate = set()  # Insieme delle navi affondate
		self.giocata_fatta = False  # Flag per controllare se è stata fatta una giocata
		self.carica_giocate()

	def crea_widgets(self):
		self.mf = tk.Frame(self)
		self.mf.grid()
		self.camp = {}
		self.campo()
		self.fs = tk.Frame(self)
		self.fs.grid()
		cancella = tk.Button(self.fs, text="Esci", width=8, command=self.cancellajson)
		cancella.grid(row=14, column=0)
		salva = tk.Button(self.fs, text="Salva", width=8, command=self.salva_giocate)
		salva.grid(row=14, column=1)

	def cancellajson(self):
		contenuto = []  # Crea una lista vuota per il contenuto del file

		# Scrivi il contenuto nel file sovrascrivendo il contenuto esistente
		with open('giocate.json', 'w') as file:
			json.dump(contenuto, file)
		
		with open('giocate2.json', 'w') as file:
			json.dump(contenuto, file)

		self.destroy()

	def campo(self):
		with open('navi2.json') as file:
			data = json.load(file)

		for x in range(10):
			for y in range(10):
				self.camp[(x, y)] = tk.Button(self.mf, text="", width=4, command=partial(self.giocata, x, y))
				self.camp[(x, y)].grid(row=x, column=y)

	def giocata(self, x, y):
		button = self.camp[(x, y)]
		button["state"] = tk.DISABLED  # Disabilita il pulsante dopo averlo colpito
		
		# Verifica se le coordinate corrispondono a una nave
		with open('navi.json') as file:
			data = json.load(file)

		for nave, coordinate in data['navi'].items():
			if [x, y] in coordinate:
				button["bg"] = "red"  # Colora il pulsante di rosso (nave colpita)
				print("Colpita nave:", nave)  # Stampa "Colpita nave: <nome>" sulla console
				button["text"] = "X"  # Aggiungi "X" sul pulsante di acqua colpita
				self.giocate.append([x, y])  # Aggiungi la gioca alla lista delle giocate

				# Verifica se la nave è stata affondata
				if self.nave_affondata(coordinate):
					print("Nave affondata:", nave)  # Stampa "Nave affondata: <nome>" sulla console
					self.navi_affondate.add(nave)  # Aggiungi la nave all'insieme delle navi affondate

				break
		else:
			button["bg"] = "blue"  # Colora il pulsante di blu (acqua colpita)
			print("Colpita acqua")  # Stampa "Colpita acqua" sulla console
			button["text"] = "O"  # Aggiungi "O" sul pulsante di acqua colpita
			self.giocate.append([x, y])  # Aggiungi la gioca alla lista delle giocate

		self.giocata_fatta = True  # Imposta il flag a True

		# Verifica se tutte le navi sono state affondate
		if self.tutte_navi_affondate():
			messagebox.showinfo("Vittoria", "Hai affondato tutte le navi!")
			self.destroy()
		self.switch_campo()
		


	def nave_affondata(self, coordinate_nave):
		# Verifica se tutte le coordinate della nave sono state colpite
		for x, y in coordinate_nave:
			if [x, y] not in self.giocate:
				return False
		return True

	def tutte_navi_affondate(self):
		# Verifica se tutte le navi sono state affondate
		with open('navi2.json') as file:
			data = json.load(file)

		for nave, coordinate in data['navi'].items():
			if nave not in self.navi_affondate:
				if not self.nave_affondata(coordinate):
					return False
		return True

	def salva_giocate(self):
		# Carica le giocate precedenti dal file JSON
		try:
			with open('giocate.json') as file:
				coordinate_giocate_precedenti = json.load(file)
		except FileNotFoundError:
			coordinate_giocate_precedenti = []

		# Concatena le coordinate delle giocate precedenti con quelle attuali
		coordinate_giocate = coordinate_giocate_precedenti + self.giocate

		# Salva le giocate nel file JSON
		with open('giocate.json', 'w') as file:
			json.dump(coordinate_giocate, file)
		# Salva le giocate in un file JSON

	def carica_giocate(self):
		# Carica le coordinate delle giocate dal file JSON
		with open('giocate.json') as file:
			coordinate_giocate = json.load(file)

		# Imposta il background dei pulsanti corrispondenti alle giocate salvate
		with open('navi2.json') as file:
			data = json.load(file)

		for coord in coordinate_giocate:
			x, y = coord
			button = self.camp[(x, y)]
			button["state"] = tk.DISABLED
			button["bg"] = "red" if [x, y] in data['navi'].values() else "blue"
			for nave, coordinate in data['navi'].items():
				if [x, y] in coordinate:
					button["bg"] = "red"  # Colora il pulsante di rosso (nave colpita)
					print("Colpita nave:", nave)  # Stampa "Colpita nave: <nome>" sulla console
					button["text"] = "X"  # Aggiungi "X" sul pulsante di acqua colpita
					break
			else:
				button["bg"] = "blue"  # Colora il pulsante di blu (acqua colpita)
				print("Colpita acqua")  # Stampa "Colpita acqua" sulla console
				button["text"] = "O"  # Aggiungi "O" sul pulsante di acqua colpita  da questa funzione

	def switch_campo(self):
		self.destroy()
		import BattNav1_1
		self.salva_giocate()
		f = BattNav1_1.BattNav1("Giocatore 2")
		f.carica_giocate1()
		f.mainloop()


def main():
	f = BattNav("Giocatore 1")
	f.carica_giocate()
	f.mainloop()


main()

import tkinter as tk
from functools import partial
import json
from tkinter import messagebox
import time


class BattNav1(tk.Tk):
	def __init__(self, nome):
		super().__init__()
		self.title(nome)
		self.resizable(0, 0)
		self.crea_widgets()
		self.giocate = []  # Lista delle giocate
		self.navi_affondate = set()  # Insieme delle navi affondate
		self.carica_giocate1()

	def crea_widgets(self):
		self.mf = tk.Frame(self)
		self.mf.grid()
		self.camp = {}
		self.campo()
		self.fs = tk.Frame(self)
		self.fs.grid()

	def campo(self):
		with open('navi.json') as file:
			data = json.load(file)

		for x in range(10):
			for y in range(10):
				self.camp[(x, y)] = tk.Button(self.mf, text="", width=4, command=partial(self.giocata, x, y))
				self.camp[(x, y)].grid(row=x, column=y)

	def giocata(self, x, y):
		button = self.camp[(x, y)]
		button["state"] = tk.DISABLED  # Disabilita il pulsante dopo averlo colpito
		#self.salva_giocate()
		with open('navi2.json') as file:
			data = json.load(file)

		for nave, coordinate in data['navi'].items():
			if [x, y] in coordinate:
				button["bg"] = "red"  # Colora il pulsante di rosso (nave colpita)
				print("Colpita nave:", nave)
				button["text"] = "X"  # Aggiungi "X" sul pulsante di acqua colpita
				self.giocate.append([x, y])  # Aggiungi la gioca alla lista delle giocate

				if self.nave_affondata(coordinate):
					print("Nave affondata:", nave)
					self.navi_affondate.add(nave)  # Aggiungi la nave all'insieme delle navi affondate

				break
		else:
			button["bg"] = "blue"  # Colora il pulsante di blu (acqua colpita)
			print("Colpita acqua")
			button["text"] = "O"  # Aggiungi "O" sul pulsante di acqua colpita
			self.giocate.append([x, y])  # Aggiungi la gioca alla lista delle giocate

		if self.tutte_navi_affondate():
			messagebox.showinfo("Vittoria", "Hai affondato tutte le navi!")
			self.destroy()
		self.switch_campo()
		

	def nave_affondata(self, coordinate_nave):
		for x, y in coordinate_nave:
			if [x, y] not in self.giocate:
				return False
		return True

	def tutte_navi_affondate(self):
		with open('navi.json') as file:
			data = json.load(file)

		for nave, coordinate in data['navi'].items():
			if nave not in self.navi_affondate:
				if not self.nave_affondata(coordinate):
					return False
		return True

	def salva_giocate1(self):
		try:
			with open('giocate2.json') as file:
				coordinate_giocate_precedenti = json.load(file)
		except FileNotFoundError:
			coordinate_giocate_precedenti = []

		coordinate_giocate = coordinate_giocate_precedenti + self.giocate

		with open('giocate2.json', 'w') as file:
			json.dump(coordinate_giocate, file)

	def carica_giocate1(self):
		try:
			with open('giocate2.json') as file:
				coordinate_giocate = json.load(file)
		except FileNotFoundError:
			coordinate_giocate = []

		with open('navi.json') as file:
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

	def switch_campo(self):
		self.salva_giocate1()
		self.destroy()  # Distruggi la finestra corrente
		import BattNav1_0  # Importa il modulo qui
		
		f = BattNav1_0.BattNav("Giocatore 1")
		f.carica_giocate()
		f.mainloop()

def main():
	f = BattNav1("Giocatore 2")
	f.carica_giocate1()
	f.mainloop()


if __name__ == "__main__":
	main()

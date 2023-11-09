import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from time import sleep
import json

class Finestra(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Battaglia Navale")
		self.geometry("500x500")
		self.resizable(0, 0)
		self.configure(bg="#F0F0F0")
		self.crea_widgets()
		self.selected_game.set("1vs1")
		self.nome1_entry.focus()

	# Funzione esci
	def esci(self):
		self.destroy()

	# Funzione play per avvio gioco + controlli
	def play(self):
		errore = 0
		tipologia = self.selected_game.get()
		nome1 = self.nome1_entry.get()
		nome2 = self.nome2_entry.get()
		if nome1 != "" and nome2 != "":
			if nome1 == nome2:
				messagebox.showerror("Errore", "I nomi dei due giocatori devono essere diversi.")
				errore = 1
		else:
			messagebox.showerror("Errore", "Errore nell'inserimento dei nomi.")
			errore = 1
		if errore == 0:
			if tipologia == "1vs1":
				print("1vs1")
				self.esci()
				from inserimento_navi import Inserimento
				# Inserire funzione modalità di gioco 1vs1
			elif tipologia == "1vsPC":
				print("1vsPC")
				# Inserire funzione modalità di gioco 1vsPC
			else:
				messagebox.showerror("Errore", "Errore nella scelta della modalità di gioco")
			
			# Crea un dizionario vuoto per il contenuto del file
			contenuto = []

			# Scrivi il dizionario nel file sovrascrivendo il contenuto esistente
			with open('giocate.json', 'w') as file:
				json.dump(contenuto, file)
			with open('giocate2.json', 'w') as file:
				json.dump(contenuto, file)
			import BattNav1_0
			o = BattNav1_0.BattNav("Giocatore 1")
			o.carica_giocate()
			o.mainloop()

	# Funzione carica
	def carica(self):
		self.progress_bar = ttk.Progressbar(self.frm_caricamento, orient='horizontal', mode='determinate')
		self.progress_bar.pack()
		while(self.progress_bar['value'] < 100):
			sleep(0.4)
			self.progress_bar['value'] += 20
			self.update_idletasks()
		if self.progress_bar['value'] >= 100:
			# Parte il gioco
			sleep(0.2)
			self.progress_bar.destroy()
			try:
				with open('giocate.json') as file:
					coordinate_giocate = json.load(file)
					if coordinate_giocate == []:
						messagebox.showerror("Errore", "Non sono presenti partite salvate.")
						self.destroy()
						self.__init__()
						return
			except json.JSONDecodeError:
				messagebox.showinfo("Errore nel JSON", "Il file JSON è malformato.")
				return
			try:
				with open('giocate2.json') as file:
					coordinate_giocate = json.load(file)
					if coordinate_giocate == []:
						messagebox.showerror("Errore", "Non sono presenti partite salvate.")
						self.destroy()
						self.__init__()
						return
			except json.JSONDecodeError:
				messagebox.showinfo("Errore nel JSON", "Il file JSON è malformato.")
				return		
			print("Avvio il gioco.")
			self.destroy()	
			import BattNav1_0
			o = BattNav1_0.BattNav("Giocatore 1")
			o.carica_giocate()
			o.mainloop()
			

	def crea_widgets(self):
		# Label frame intro
		frm_intro = tk.Frame(self)
		lbl_intro = tk.Label(frm_intro, text="Battaglia Navale", font=("Times", 20, "italic"), fg="#194D29", bg="#F0F0F0")
		lbl_intro.pack()
		lbl_autori = tk.Label(frm_intro, text="by Audisio, Galeasso, Giusiano, Paseri", font=("Times", 10, "italic"), fg="#194D29", bg="#F0F0F0")
		lbl_autori.pack()
		frm_intro.pack(pady=20)

		# Radio button modalità gioco
		self.selected_game = tk.StringVar()
		frm_game = tk.Frame(self, bg="#F0F0F0")
		selected1 = tk.Radiobutton(frm_game, text="1 vs 1", variable=self.selected_game, value="1vs1", bg="#F0F0F0")
		selected1.pack(side=tk.LEFT, padx=10)
		selected2 = tk.Radiobutton(frm_game, text="1 vs PC", variable=self.selected_game, value="1vsPC", bg="#F0F0F0")
		selected2.pack(side=tk.LEFT, padx=10)
		frm_game.pack(pady=10)

		# Input nome giocatore 1 e 2
		frm_name = tk.Frame(self, bg="#F0F0F0")
		lbl_nome1 = tk.Label(frm_name, text="Giocatore 1", bg="#F0F0F0")
		lbl_nome1.pack(side=tk.LEFT, padx=10)
		self.nome1_entry = tk.Entry(frm_name)
		self.nome1_entry.pack(side=tk.LEFT)

		lbl_nome2 = tk.Label(frm_name, text="Giocatore 2", bg="#F0F0F0")
		lbl_nome2.pack(side=tk.LEFT, padx=10)
		self.nome2_entry = tk.Entry(frm_name)
		self.nome2_entry.pack(side=tk.LEFT)
		frm_name.pack(pady=10)

		# Pulsanti Gioca e Carica
		frm_button = tk.Frame(self, bg="#F0F0F0")
		button_game = tk.Button(frm_button, text="Gioca", command=self.play, bg="#007ACC", fg="white")
		button_game.pack(padx=10, side=tk.LEFT, ipadx=20, ipady=10)
		button_load = tk.Button(frm_button, text="Carica", command=self.carica, bg="#007ACC", fg="white")
		button_load.pack(padx=10, side=tk.LEFT, ipadx=20, ipady=10, pady=20)
		frm_button.pack(pady=40)

		# Barra di caricamento
		self.frm_caricamento = tk.Frame(self)
		self.frm_caricamento.pack()

		# Bottone esci
		button_exit = tk.Button(self, text="Esci", command=self.esci, bg="red", fg="white")
		button_exit.pack(side=tk.RIGHT, padx=30, ipadx=20, ipady=10, pady=10)

root = Finestra()
root.mainloop()


import tkinter as tk
import re # per controllo targa
from tkinter import ttk
from tkinter import messagebox
import pickle

class Prenotazione(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Prenotazione posto auto")
		self.geometry("800x500")
		self.resizable(0,0)
		self.crea_widgets()
		self.cognome_entry.focus_set()
	
	# funzione prenotazione + controlli vari
	def prenota(self):
		try:
			# cambiamento prima lettera, con lettera maiuscola
			nome = self.nome_entry.get()
			nome = nome[0].upper() + nome[1:].lower()
			cognome = self.cognome_entry.get()
			# controllo per doppi cognomi e aggiunta di una o più lettere maiuscole
			if " " in cognome:
				index = cognome.index(" ")
				cognome = cognome[0].upper() + cognome[1:index].lower() + " " + cognome[index+1].upper() + cognome[index+2:].lower()
				print("\nDOPPIO COGNOME\n")
			else:
				cognome = cognome[0].upper() + cognome[1:].lower()
			marca = self.marca_entry.get()
			marca = marca[0].upper() + marca[1:].lower()
			modello = self.modello_entry.get()
			modello = modello[0].upper() + modello[1:].lower()
			colore = self.colore_entry.get()
			colore = colore[0].upper() + colore[1:].lower()
			targa = self.targa_entry.get()
			targa = targa.upper()
			# formato standard targa italiana
			pattern = r'^[A-Z]{2}\d{3}[A-Z]{2}$'
			# controllo targa con equazione elementare
			if re.match(pattern, targa):
				# creazione dizionario contenente tutto
				prenotazione = {"Nome": nome, "Cognome": cognome, "Marca": marca, "Modello": modello, "Targa": targa, "Colore": colore, "Ore_sosta": self.ore.get(), "Tipologia_parcheggio": self.combo.get()}
				# creazione file BackupPrenotazione.pickle
				pickling_on = open("BackupPrenotazione.pickle", "wb")
				# scrittura sul file
				pickle.dump(prenotazione, pickling_on)
				# chiusura del file
				pickling_on.close()
				# lable conferma di successo prenotazione
				self.lbl_conferma.config(text = "Prenotazione effettuata con successo!")
				self.lbl_conferma.config(fg = 'green')
				# pulizia per nuova prenotazione
				self.nome_entry.delete(0, tk.END)
				self.cognome_entry.delete(0, tk.END)
				self.marca_entry.delete(0, tk.END)
				self.modello_entry.delete(0, tk.END)
				self.targa_entry.delete(0, tk.END)
				self.colore_entry.delete(0, tk.END)
				self.ore.set("1")
				self.combo.set("")
				self.cognome_entry.focus_set()
			else:
				# messaggio errore targa errata
				messagebox.showerror("Targa non valida", "La targa non è nel formato corretto.")
		except ValueError:
			messagebox.showerror("Errore", "Errore nell'inserimento dei dati!")

	# funzione caricamento
	def carica(self):
		# apertura file BackupPrenotazione.pickle in lettura
		fileLetto = open("BackupPrenotazione.pickle", "rb")
		# salvatagglio del contenuto
		prenotazione = pickle.load(fileLetto)
		# stampa su terminale del contenuto
		print("Dizionario prenotazione: ", prenotazione)
		# caricamento dati contenuti sul file
		self.nome_entry.delete(0, tk.END)
		self.nome_entry.insert(0, prenotazione["Nome"])
		self.cognome_entry.delete(0, tk.END)
		self.cognome_entry.insert(0, prenotazione["Cognome"])
		self.marca_entry.delete(0, tk.END)
		self.marca_entry.insert(0, prenotazione["Marca"])
		self.modello_entry.delete(0, tk.END)
		self.modello_entry.insert(0, prenotazione["Modello"])
		self.targa_entry.delete(0, tk.END)
		self.targa_entry.insert(0, prenotazione["Targa"])
		self.colore_entry.delete(0, tk.END)
		self.colore_entry.insert(0, prenotazione["Colore"])
		self.ore.set(prenotazione["Ore_sosta"])
		self.combo.set(prenotazione["Tipologia_parcheggio"])
		fileLetto.close()

	# funzione uscita
	def uscita(self):
		root.destroy()

	def crea_widgets(self):
		# label parcheggio intro
		lbl_parcheggio = tk.Label(self, text="Parcheggio Piazza Vittorio Emanuele ", font=("Time New Romans", 20))
		lbl_parcheggio.pack(pady=20)

		# inserimento nome e cognome
		frm_dati = tk.Frame(self)
		lbl_cognome = tk.Label(frm_dati, text="Cognome")
		lbl_cognome.pack(side=tk.LEFT, padx=10)
		self.cognome_entry = tk.Entry(frm_dati)
		self.cognome_entry.pack(side=tk.LEFT)

		lbl_nome = tk.Label(frm_dati, text="Nome")
		lbl_nome.pack(side=tk.LEFT, padx=10)
		self.nome_entry = tk.Entry(frm_dati)
		self.nome_entry.pack(side=tk.LEFT)
		frm_dati.pack(pady=10)

		# inserimento specifiche automobile
		frm_auto = tk.Frame(self)
		lbl_marca = tk.Label(frm_auto, text="Marca")
		lbl_marca.pack(side=tk.LEFT, padx=10)
		self.marca_entry = tk.Entry(frm_auto)
		self.marca_entry.pack(side=tk.LEFT)

		lbl_modello = tk.Label(frm_auto, text="Modello")
		lbl_modello.pack(side=tk.LEFT, padx=10)
		self.modello_entry = tk.Entry(frm_auto)
		self.modello_entry.pack(side=tk.LEFT)

		lbl_targa = tk.Label(frm_auto, text="Targa")
		lbl_targa.pack(side=tk.LEFT, padx=10)
		self.targa_entry = tk.Entry(frm_auto)
		self.targa_entry.pack(side=tk.LEFT)

		lbl_colore = tk.Label(frm_auto, text="Colore")
		lbl_colore.pack(side=tk.LEFT, padx=10)
		self.colore_entry = tk.Entry(frm_auto)
		self.colore_entry.pack(side=tk.LEFT)
		frm_auto.pack(pady=10)

		# inserimento numero ore
		lbl_ore = tk.Label(self, text="Numero ore di sosta")
		lbl_ore.pack()
		self.ore = tk.StringVar()
		self.ore.set("1")
		spin_ore = tk.Spinbox(self, from_=1, to=24, textvariable=self.ore)
		spin_ore.pack()

		# selezione scelta del parcheggio
		lbl_parcheggio = tk.Label(self, text="Tipologia di parcheggio")
		lbl_parcheggio.pack()
		opzioni = ["Parcheggio coperto", "Parcheggio scoperto"]
		self.combo = ttk.Combobox(self, values=opzioni)
		self.combo.pack()

		# pulsante prenota collegato alla funzione prenota
		btn_prenota = tk.Button(self, text="Prenota", command=self.prenota)
		btn_prenota.pack(pady=20)

		# pulsante carica collegato alla funzione carica
		btn_carica = tk.Button(self, text="Carica", command=self.carica)
		btn_carica.pack(pady=20)

		# label di conferma
		self.lbl_conferma = tk.Label(self, text="")
		self.lbl_conferma.pack()

		# pulsante di uscita collegato alla funzione esci
		frm_uscita = tk.Frame(self)
		self.btn_uscita = tk.Button(frm_uscita, text = "Esci", command = self.uscita)
		self.btn_uscita.pack(side = tk.RIGHT, padx = 10)
		frm_uscita.pack(pady = 10)

# main
root = Prenotazione()
root.mainloop()
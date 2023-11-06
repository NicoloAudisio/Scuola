import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle

class Timbratura(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Conteggio ore volontariato")
		self.geometry("800x500")
		self.resizable(0,0)
		self.crea_widgets()
    
	# Funzione timbra
	def timbra(self):
		ora_ingresso = self.ora_ingresso.get()
		ora_uscita = self.ora_uscita.get()
		mansione = self.combo.get()

		# Controlli
		errore = True
		errore == True
		if ora_ingresso == "":
			self.ora_ingresso.config(bg = "red")
		if ora_ingresso.isnumeric() != True:
			self.ora_ingresso.config(bg = "red")
		if ora_uscita == "":
			self.ora_uscita.config(bg = "red")
		if ora_uscita.isnumeric() != True:
			self.ora_uscita.config(bg = "red")
		if mansione == "":
			messagebox.showerror("Errore!", "Errore nella scelta della mansione")


	# Funzione uscita
	def uscita(self):
		root.destroy()

	def crea_widgets(self):
		# Label intro
		lbl_intro = tk.Label(self, text = "Conteggio ore", font=("Time New Romans", 20))
		lbl_intro.pack(pady = 20)

		# Inserimento ora ingresso
		frm_dati = tk.Frame(self)
		lbl_oraIngresso = tk.Label(frm_dati, text = "Ora ingresso")
		lbl_oraIngresso.pack(side = tk.LEFT, padx = 10)
		self.ora_ingresso = tk.Entry(frm_dati)
		self.ora_ingresso.pack(side = tk.LEFT)

		# Inserimento ora uscita
		lbl_oraUscita = tk.Label(frm_dati, text = "Ora uscita")
		lbl_oraUscita.pack(side = tk.LEFT, padx = 10)
		self.ora_uscita = tk.Entry(frm_dati)
		self.ora_uscita.pack(side = tk.LEFT)
		frm_dati.pack(pady = 10)

		# Inserimento tipologia
		lbl_volontariato = tk.Label(self, text = "Mansione")
		lbl_volontariato.pack()
		opzioni = ["Tirocinante 118", "Trasporto", "Assistenza gara e/o manifestazione", "Servizio sede"]
		self.combo = ttk.Combobox(self, values = opzioni)
		self.combo.pack()

		# Pulsante prenota collegato alla funzione prenota
		btn_prenota = tk.Button(self, text="Timbra", command=self.timbra)
		btn_prenota.pack(pady=20)
		
		# Label di conferma
		self.lbl_conferma = tk.Label(self, text="")
		self.lbl_conferma.pack()

		# Pulsante di uscita collegato alla funzione esci
		frm_uscita = tk.Frame(self)
		self.btn_uscita = tk.Button(frm_uscita, text = "Esci", command = self.uscita)
		self.btn_uscita.pack(side = tk.RIGHT, padx = 10)
		frm_uscita.pack(pady = 10)


# Main
root = Timbratura()
root.mainloop()

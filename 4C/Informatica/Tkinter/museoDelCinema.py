import tkinter as tk
from tkinter import messagebox

class Finestra(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Museo del cinema Audisio")
		self.geometry("600x630")
		self.resizable(0, 0)

	# --- FUNZIONI ---
	def calcola(self):
		cognome = self.cognome_entry.get()
		nome = self.nome_entry.get()
		adulti = self.adulti.get()
		bambini = self.bambini.get()
		audioguida = self.radioguida.get()
		ascensore = self.ascensore.get()
		mostra = self.mostra.get()
		laboratori = self.laboratori.get()

		self.btn_calcola.config(bg='yellow')
		self.btn_riepilogo.config(bg='white')
		self.btn_uscita.config(bg='white')
		self.btn_cancella.config(bg='white')
		# --- CONTROLLO NOME ---
		if cognome == "" or nome == "":
			messagebox.showerror("Errore", "Errore nell'inserimento del nominativo")
			self.cognome_entry.config(bg='red')
			self.nome_entry.config(bg='red')
		else:
			self.cognome_entry.config(bg='white')
			self.nome_entry.config(bg='white')
		
		# --- CONTEGGIO SOMMA ---	
		totale = 0
		costo_audioguida = 0
		costo_opzioni = 0
		somma_persona = int(adulti) + int(bambini)
		servizi = []
		
		costo_ingresso = ((8 * int(adulti)) + (5 * int(bambini)))
		if audioguida == 'Si':
			costo_audioguida = costo_audioguida + (2 * somma_persona)
		if ascensore == True:
			costo_opzioni = costo_opzioni + (4 * somma_persona)
			servizi.append("Ascensore")
		elif mostra == True:
			costo_opzioni = costo_opzioni + (6 * somma_persona)
			servizi.append("Mostra")
		elif laboratori == True:
			costo_opzioni = costo_opzioni + (10 * somma_persona)
			servizi.append("Laboratori")
		servizi_str = ",".join(servizi)
		totale = int(costo_ingresso) + int(costo_opzioni) + int(costo_audioguida)

		self.lbl_riepilogo.config(text = f"Cognome {cognome}   Nome {nome}\nAdulti: {adulti}   Bambini: {bambini}\nTotale persone: {somma_persona}\nTotale ingressi: {costo_ingresso}€\n\nAudioguida: {audioguida}\nOpzioni aggiuntive: {servizi_str}\nTotale: {totale}€")

	def riepilogo(self):
		cognome = self.cognome_entry.get()
		nome = self.nome_entry.get()
		adulti = self.adulti.get()
		bambini = self.bambini.get()
		audioguida = self.radioguida.get()
		ascensore = self.ascensore.get()
		mostra = self.mostra.get()
		laboratori = self.laboratori.get()

		self.btn_calcola.config(bg='white')
		self.btn_riepilogo.config(bg='yellow')
		self.btn_uscita.config(bg='white')
		self.btn_cancella.config(bg='white')
		# --- CONTROLLO NOME ---
		if cognome == "" or nome == "":
			messagebox.showerror("Errore", "Errore nell'inserimento del nominativo")
			self.cognome_entry.config(bg='red')
			self.nome_entry.config(bg='red')
		else:
			self.cognome_entry.config(bg='white')
			self.nome_entry.config(bg='white')

		# --- RIEPILOGO ---	
		servizi = []

		if ascensore == True:
			servizi.append("Ascensore")
		elif mostra == True:
			servizi.append("Mostra")
		elif laboratori == True:
			servizi.append("Laboratori")
		servizi_str = ",".join(servizi)

		self.lbl_riepilogo.config(text = f"Cognome {cognome}   Nome {nome}\nAdulti: {adulti}   Bambini: {bambini}\nAudioguida: {audioguida}\nOpzioni aggiuntive: {servizi_str}")

	def uscita(self):
		root.destroy()

	def crea_widgets(self):
		# --- LABEL INTRO ---
		lbl_museo = tk.Label(self, text = "Visita al Museo del Cinema Audisio", font = ("Time New ROmans", 20))
		lbl_museo.pack(pady = 20)

		# --- COGNOME ---
		frm_dati = tk.Frame(self)
		lbl_cognome = tk.Label(frm_dati, text = "Cognome")
		lbl_cognome.pack(side = tk.LEFT, padx = 10)
		self.cognome_entry = tk.Entry(frm_dati)
		self.cognome_entry.pack(side = tk.LEFT)

		lbl_nome = tk.Label(frm_dati, text = "Nome")
		lbl_nome.pack(side = tk.LEFT, padx = 10)
		self.nome_entry = tk.Entry(frm_dati)
		self.nome_entry.pack(side = tk.LEFT)
		frm_dati.pack(pady = 10)

		# --- ADULTI E BAMBINI ---
		frm_persone = tk.Frame(self)
		lbl_adulti = tk.Label(frm_persone, text = "Adulti")
		lbl_adulti.pack(side = tk.LEFT, padx = 10)
		self.adulti = tk.StringVar()
		spin_adulti = tk.Spinbox(frm_persone, from_ = 1, to = 30, textvariable = self.adulti)
		spin_adulti.pack(side = tk.LEFT)
		frm_dati.pack(pady = 10)

		lbl_bambini = tk.Label(frm_persone, text = "Bambini")
		lbl_bambini.pack(side = tk.LEFT, padx = 10)
		self.bambini = tk.StringVar()
		spin_bambini = tk.Spinbox(frm_persone, from_ = 0, to = 30, textvariable = self.bambini)
		spin_bambini.pack(side = tk.LEFT)
		frm_persone.pack(pady = 10)

		# --- AUDIOGUIDA ---
		frm_audioguida = tk.Frame(self)
		lbl_radioguida = tk.Label(frm_audioguida, text = "Radioguida")
		lbl_radioguida.pack()
		self.radioguida = tk.StringVar()
		self.radioguida.set("No")
		rbt_si = tk.Radiobutton(frm_audioguida, text = "Sì", variable = self.radioguida, value = "Si")
		rbt_si.pack()
		rbt_no = tk.Radiobutton(frm_audioguida, text = "No", variable = self.radioguida, value = "No")
		rbt_no.pack()
		frm_audioguida.pack(pady = 10)

		# --- SERVIZI EXTRA ---
		frm_servizi = tk.Frame(self)
		lbl_opzioniAggiuntive = tk.Label(frm_servizi, text = "Opzioni aggiuntive")
		lbl_opzioniAggiuntive.pack()
		self.ascensore = tk.BooleanVar()
		chk_ascensore = tk.Checkbutton(frm_servizi, text = "Visita Museo + Ascensore", variable = self.ascensore)
		chk_ascensore.pack()
		self.mostra = tk.BooleanVar()
		chk_mostra = tk.Checkbutton(frm_servizi, text = "Visita Museo + Mostra itinerante")
		chk_mostra.pack()
		self.laboratori = tk.BooleanVar()
		chk_laboratori = tk.Checkbutton(frm_servizi, text = "Visita Museo + Laboratori")
		chk_laboratori.pack()
		frm_servizi.pack(pady = 10)

		# --- BOTTONI ---
		frm_bottoni = tk.Frame(self)
		# --- RIEPILOGO
		self.btn_riepilogo = tk.Button(frm_bottoni, text = "Riepilogo", command = self.riepilogo)
		self.btn_riepilogo.pack(side = tk.LEFT, padx = 10)
		# --- CALCOLA ---
		self.btn_calcola = tk.Button(frm_bottoni, text = "Calcola", command = self.calcola)
		self.btn_calcola.pack(side = tk.LEFT, padx = 10)
		# --- CANCELLA ---
		self.btn_cancella = tk.Button(frm_bottoni, text = "Cancella")
		self.btn_cancella.pack(side = tk.LEFT, padx = 10)
		frm_bottoni.pack(pady = 10)

		# --- LABEL RIEPILOGO ---
		lbl_title_riepilogo = tk.Label(self, text = "Riepilogo")
		lbl_title_riepilogo.pack()
		self.lbl_riepilogo = tk.Label(self, text = "")
		self.lbl_riepilogo.pack()

		# --- BOTTOME USCITA ---
		frm_uscita = tk.Frame(self)
		self.btn_uscita = tk.Button(frm_uscita, text = "Esci", command = self.uscita)
		self.btn_uscita.pack(side = tk.RIGHT, padx = 10)
		frm_uscita.pack(pady = 10)


root = Finestra()
root.crea_widgets()
root.mainloop()

import random
import tkinter as tk
from tkinter import messagebox

class CampoMinato:
	def __init__(self, master):
		self.master = master
		master.title("Campo Minato")
		master.resizable(False, False)
		
		self.punteggio = 0
		self.mine = set()
		self.scoperte = set()
		
		# Frame superiore con il punteggio
		top_frame = tk.Frame(master, bg="light blue")
		top_frame.pack(fill="x")
		tk.Label(top_frame, text="Punti:", bg="light blue").pack(side="left", padx=10)
		self.punteggio_label = tk.Label(top_frame, text="0", bg="light blue")
		self.punteggio_label.pack(side="right", padx=10)
		
		# Frame centrale con la griglia di gioco
		center_frame = tk.Frame(master)
		center_frame.pack()
		self.celle = {}
		for riga in range(10):
			for colonna in range(10):
				cella = tk.Button(center_frame, bg="gray", width=2, height=1,
								  command=lambda r=riga, c=colonna: self.scopri_cella(r, c))
				cella.grid(row=riga, column=colonna)
				self.celle[(riga, colonna)] = cella
		
		# Frame inferiore con il pulsante "ESCI"
		bottom_frame = tk.Frame(master, bg="light blue")
		bottom_frame.pack(fill="x", pady=10)
		tk.Button(bottom_frame, text="ESCI", bg="gray", command=self.esci).pack(padx=10, pady=5)
		
		# Generazione delle mine
		self.genera_mine()
	
	def genera_mine(self):
		# Genera 10 mine in posizioni casuali
		mine_generate = 0
		while mine_generate < 10:
			riga = random.randint(0, 9)
			colonna = random.randint(0, 9)
			if (riga, colonna) not in self.mine:
				self.mine.add((riga, colonna))
				mine_generate += 1
	
	def scopri_cella(self, riga, colonna):
		if (riga, colonna) in self.scoperte:
			# La cella Ã¨ giÃ  stata scoperta, decrementa il punteggio
			self.punteggio -= 1
			self.aggiorna_punteggio()
			self.celle[(riga, colonna)].config(bg="blue", text="O")
		elif (riga, colonna) in self.mine:
			# La cella contiene una mina, il gioco finisce
			self.celle[(riga, colonna)].config(bg="red", fg="gray", text="X")
			self.game_over()
		else:
			# La cella non contiene una mina, la scopre e controlla le celle adiacenti
			celle_da_scoprire = {(riga, colonna)}
			while celle_da_scoprire:
				r, c = celle_da_scoprire.pop()
				self.scoperte.add((r, c))
				self.celle[(r, c)].config(bg="white")
				# Controlla le 8 celle adiacenti per verificare se contengono mine o sono vuote
				mine_adiacenti = self.celle_adiacenti_mine(r, c)
				if mine_adiacenti:
					# Ci sono mine adiacenti, visualizza il numero di mine
					self.celle[(r, c)].config(text=str(len(mine_adiacenti)), fg="black")
				else:
					# Non ci sono mine adiacenti, aggiunge le celle adiacenti da scoprire
					celle_adiacenti = self.celle_adiacenti(r, c)
				for a, b in celle_adiacenti:
					if (a, b) not in self.scoperte:
						celle_da_scoprire.add((a, b))
						# Incrementa il punteggio
						self.punteggio += 1
						self.aggiorna_punteggio()
				# Verifica se il gioco Ã¨ finito
				if len(self.scoperte) == 90:
					self.vittoria()
	def celle_adiacenti(self, riga, colonna):
		adiacenti = set()
		for r in range(riga-1, riga+2):
			for c in range(colonna-1, colonna+2):
				if 0 <= r <= 9 and 0 <= c <= 9 and (r, c) != (riga, colonna):
					adiacenti.add((r, c))
		return adiacenti

	def celle_adiacenti_mine(self, riga, colonna):
		adiacenti_mine = set()
		for r in range(riga-1, riga+2):
			for c in range(colonna-1, colonna+2):
				if 0 <= r <= 9 and 0 <= c <= 9 and (r, c) != (riga, colonna) and (r, c) in self.mine:
					adiacenti_mine.add((r, c))
		return adiacenti_mine

	def game_over(self):
		# Il gioco Ã¨ finito a causa di una mina
		messagebox.showerror("Game Over", "Hai perso! Hai trovato %d mine." % len(self.mine))
		self.disattiva_celle()

	def vittoria(self):
		# Il gioco Ã¨ finito perchÃ© tutte le celle vuote sono state scoperte
		messagebox.showinfo("Vittoria!", "Hai vinto! Hai totalizzato %d punti." % self.punteggio)
		self.disattiva_celle()

	def disattiva_celle(self):
		# Disattiva tutte le celle
		for cella in self.celle.values():
			cella.config(state="disabled")

	def aggiorna_punteggio(self):
		# Aggiorna il punteggio nella label
		self.punteggio_label.config(text=str(self.punteggio))

	def esci(self):
		# Chiude la finestra
		self.master.destroy()

root = tk.Tk()
campo_minato = CampoMinato(root)
root.mainloop()

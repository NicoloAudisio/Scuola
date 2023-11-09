import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json

class Inserimento(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Inserimento navi - GIOCATORE 2")
		self.geometry("500x500")
		self.resizable(0, 0)

		# Dimensioni del campo di gioco
		self.rows = 10
		self.cols = 10

		#conteggio numero navi
		self.numnave=0

		#controllo pulsante salva
		self.ships_inserted = False

		# Inizializza il campo di gioco
		self.field = [[None for _ in range(self.cols)] for _ in range(self.rows)]

		# Dizionario per salvare le posizioni delle navi
		self.ship_positions = {}
		self.ships = {}

		# Dizionario per memorizzare il numero di navi inserite
		self.ship_counts = {
			"2 blocchi": 0,
			"3 blocchi": 0,
			"4 blocchi": 0
		}

		# Crea il frame principale
		self.frame = tk.Frame(self, padx=10, pady=10)
		self.frame.pack()

		# Crea il label dinamico per il conteggio delle navi rimanenti
		self.remaining_ships_label = tk.Label(self.frame, text="Navi da inserire:")
		self.remaining_ships_label.pack()

		# Crea la griglia di gioco
		self.create_field()

		# Crea il frame per la scelta della nave e dell'orientamento
		self.create_ship_selection_frame()

		# Crea il pulsante per il salvataggio delle posizioni delle navi
		self.create_save_button()

		# Aggiorna il label delle navi rimanenti
		self.update_remaining_ships_label()

	def create_field(self):
		self.field_frame = tk.Frame(self.frame)
		self.field_frame.pack()

		for row in range(self.rows):
			for col in range(self.cols):
				button = tk.Button(self.field_frame, width=2, height=1, relief=tk.RAISED)
				button.grid(row=row, column=col)

				# Imposta la gestione degli eventi di click
				button.bind("<Button-1>", self.place_ship)

				self.field[row][col] = button

	def create_ship_selection_frame(self):
		self.ship_selection_frame = tk.Frame(self.frame)
		self.ship_selection_frame.pack(pady=20)

		# Etichetta per la selezione del tipo di nave
		ship_label = tk.Label(self.ship_selection_frame, text="Nave:")
		ship_label.pack(side=tk.LEFT)

		# Combobox per la scelta del tipo di nave
		self.ship_combobox = ttk.Combobox(self.ship_selection_frame, values=["2 blocchi", "3 blocchi", "4 blocchi"])
		self.ship_combobox.pack(side=tk.LEFT)

		# Etichetta per la selezione dell'orientamento
		orientation_label = tk.Label(self.ship_selection_frame, text="Orientamento:")
		orientation_label.pack(side=tk.LEFT)

		# Menu per la scelta dell'orientamento
		self.orientation_var = tk.StringVar(value="Orizzontale")
		orientation_menu = tk.OptionMenu(self.ship_selection_frame, self.orientation_var, "Orizzontale", "Verticale")
		orientation_menu.pack(side=tk.LEFT)

	def create_save_button(self):
		self.save_button_frame = tk.Frame(self.frame)
		self.save_button_frame.pack()

		# Pulsante per il salvataggio delle posizioni delle navi
		self.save_button = tk.Button(self.save_button_frame, text="Salva", command=self.save_ship_positions, state=tk.DISABLED)
		self.save_button.pack(pady=10)


	def place_ship(self, event):
		selected_ship = self.ship_combobox.get()

		# Controllo sul numero di navi inserite
		if self.is_valid_ship_count(selected_ship):
			button = event.widget
			row = button.grid_info()["row"]
			col = button.grid_info()["column"]

			# Controllo se la posizione è valida per posizionare la nave
			if self.is_valid_position(selected_ship, row, col):
				# Posiziona la nave
				self.place_ship_button(selected_ship, row, col)
				# Aggiorna le posizioni della nave nel dizionario delle posizioni delle navi
				self.update_ship_positions(selected_ship, row, col)
				# Aggiorna il label delle navi rimanenti
				self.update_remaining_ships_label()
			else:
				messagebox.showerror("Errore", "Posizione non valida per la nave selezionata.")
		else:
			messagebox.showerror("Errore", "Limite di navi raggiunto per la tipologia selezionata.")

	def is_valid_ship_count(self, selected_ship):
		return self.ship_counts[selected_ship] < 2

	def is_valid_position(self, selected_ship, row, col):
		ship_length = int(selected_ship.split()[0])
		orientation = self.orientation_var.get()

		if orientation == "Verticale":
			if row + ship_length > self.rows:
				return False

			for i in range(ship_length):
				if self.field[row + i][col]["text"] != "":
					return False
		else:  # orientation == "Orizzontale"
			if col + ship_length > self.cols:
				return False

			for i in range(ship_length):
				if self.field[row][col + i]["text"] != "":
					return False

		return True

	def place_ship_button(self, selected_ship, row, col):
		ship_length = int(selected_ship.split()[0])
		orientation = self.orientation_var.get()

		for i in range(ship_length):
			if orientation == "Verticale":
				button = self.field[row + i][col]
			else:  # orientation == "Orizzontale"
				button = self.field[row][col + i]

			button["text"] = "X"

	def update_ship_positions(self, selected_ship, row, col):
		ship_length = int(selected_ship.split()[0])
		orientation = self.orientation_var.get()

		ship_positions = []
		for i in range(ship_length):
			if orientation == "Verticale":
				position = [row + i, col]
			else:  # orientation == "Orizzontale"
				position = [row, col + i]

			ship_positions.append(position)

		# Genera il nome della nave basato sul numero di navi inserite fino a quel momento
		self.numnave += 1
		ship_name = f"nave{self.numnave}"
		self.ship_positions.setdefault(ship_name, []).extend(ship_positions)
		self.ship_counts[selected_ship] += 1

		# Salvataggio delle navi in un dizionario
		if ship_name not in self.ships:
			self.ships[ship_name] = []
		for i in ship_positions:
			self.ships[ship_name].append(i)
		print(self.ships)

		self.update_remaining_ships_label()




	def save_ship_positions(self):
		# Crea il dizionario di output con la struttura richiesta
		output_dict = {"navi": self.ships}

		# Salva il file JSON con le posizioni delle navi
		with open('navi2.json', 'w') as file:
			json.dump(output_dict, file)

		self.destroy()
		


	def update_remaining_ships_label(self):
		remaining_ships = ""
		for ship_type, ship_count in self.ship_counts.items():
			remaining_ships += f"{ship_type}: {2 - ship_count} "
		self.remaining_ships_label.config(text="Navi da inserire: " + remaining_ships.strip())

		# Controlla se tutte le navi sono state inserite
		if all(count == 2 for count in self.ship_counts.values()):
			self.save_button.config(state=tk.NORMAL)  # Abilita il pulsante "Salva"
			self.ships_inserted = True
		else:
			self.save_button.config(state=tk.DISABLED)  # Disabilita il pulsante "Salva"
			self.ships_inserted = False



def MAIN():
	app = Inserimento()
	app.mainloop()

MAIN()
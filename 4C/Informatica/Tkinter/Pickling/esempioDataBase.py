import tkinter as tk
import pickle


class App:
    def __init__(self, master):
	self.master = master
	master.title("Forum prenotazione posto auto")
	
	# definizione dei widget
	self.nome_label = tk.Label(master, text="Nome:")
	self.cognome_label = tk.Label(master, text="Cognome:")
	self.marca_label = tk.Label(master, text="Marca:")
	self.modello_label = tk.Label(master, text="Modello:")
	self.colore_label = tk.Label(master, text="Colore:")
	
	self.nome_entry = tk.Entry(master)
	self.cognome_entry = tk.Entry(master)
	self.marca_entry = tk.Entry(master)
	self.modello_entry = tk.Entry(master)
	self.colore_entry = tk.Entry(master)
	
	self.prenota_button = tk.Button(master, text="Prenota", command=self.prenota)
	self.cognome_ricerca_label = tk.Label(master, text="Cognome ricerca:")
	self.cognome_ricerca_entry = tk.Entry(master)
	self.ricerca_button = tk.Button(master, text="Ricerca", command=self.ricerca)
	self.exit_button = tk.Button(master, text="Exit", command=master.quit)
	
	# posizionamento dei widget
	self.nome_label.grid(row=0, column=0, sticky=tk.E)
	self.cognome_label.grid(row=1, column=0, sticky=tk.E)
	self.marca_label.grid(row=2, column=0, sticky=tk.E)
	self.modello_label.grid(row=3, column=0, sticky=tk.E)
	self.colore_label.grid(row=4, column=0, sticky=tk.E)
	
	self.nome_entry.grid(row=0, column=1)
	self.cognome_entry.grid(row=1, column=1)
	self.marca_entry.grid(row=2, column=1)
	self.modello_entry.grid(row=3, column=1)
	self.colore_entry.grid(row=4, column=1)
	
	self.prenota_button.grid(row=5, column=0)
	self.cognome_ricerca_label.grid(row=6, column=0, sticky=tk.E)
	self.cognome_ricerca_entry.grid(row=6, column=1)
	self.ricerca_button.grid(row=7, column=0)
	self.exit_button.grid(row=7, column=1, sticky=tk.E)
	
	# caricamento del database
	try:
	    with open("database_prenotazioni.pickle", "rb") as f:
		self.db = pickle.load(f)
	except FileNotFoundError:
	    self.db = {}
		
import tkinter as tk
import pickle


class App:
    def __init__(self, master):
	self.master = master
	master.title("Forum prenotazione posto auto")
	
	# definizione dei widget
	self.nome_label = tk.Label(master, text="Nome:")
	self.cognome_label = tk.Label(master, text="Cognome:")
	self.marca_label = tk.Label(master, text="Marca:")
	self.modello_label = tk.Label(master, text="Modello:")
	self.colore_label = tk.Label(master, text="Colore:")
	
	self.nome_entry = tk.Entry(master)
	self.cognome_entry = tk.Entry(master)
	self.marca_entry = tk.Entry(master)
	self.modello_entry = tk.Entry(master)
	self.colore_entry = tk.Entry(master)
	
	self.prenota_button = tk.Button(master, text="Prenota", command=self.prenota)
	self.cognome_ricerca_label = tk.Label(master, text="Cognome ricerca:")
	self.cognome_ricerca_entry = tk.Entry(master)
	self.ricerca_button = tk.Button(master, text="Ricerca", command=self.ricerca)
	self.exit_button = tk.Button(master, text="Exit", command=master.quit)
	
	# posizionamento dei widget
	self.nome_label.grid(row=0, column=0, sticky=tk.E)
	self.cognome_label.grid(row=1, column=0, sticky=tk.E)
	self.marca_label.grid(row=2, column=0, sticky=tk.E)
	self.modello_label.grid(row=3, column=0, sticky=tk.E)
	self.colore_label.grid(row=4, column=0, sticky=tk.E)
	
	self.nome_entry.grid(row=0, column=1)
	self.cognome_entry.grid(row=1, column=1)
	self.marca_entry.grid(row=2, column=1)
	self.modello_entry.grid(row=3, column=1)
	self.colore_entry.grid(row=4, column=1)
	
	self.prenota_button.grid(row=5, column=0)
	self.cognome_ricerca_label.grid(row=6, column=0, sticky=tk.E)
	self.cognome_ricerca_entry.grid(row=6, column=1)
	self.ricerca_button.grid(row=7, column=0)
	self.exit_button.grid(row=7, column=1, sticky=tk.E)
	
	# caricamento del database
	try:
	    with open("database_prenotazioni.pickle", "rb") as f:
		self.db = pickle.load(f)
	except FileNotFoundError:
	    self.db = {}
		
def prenota(self):
    # recupero dei dati dalle caselle di input
    nome = self.nome_entry.get()
    cognome = self.cognome_entry.get()
    marca = self.marca_entry.get()
    modello = self.modello_entry.get()
    colore = self.colore_entry.get()
    
    # controllo dei dati inseriti
    if not nome or not cognome or not marca or not modello or not colore:
	tk.messagebox.showwarning("Attenzione", "Tutti i campi sono obbligatori")
	return
    
    if cognome in self.db:
	tk.messagebox.showwarning("Attenzione", "Cognome già presente nel database")
	return
    
    # creazione del dizionario di prenotazione e inserimento nel database
    prenotazione = {
	"nome": nome,
	"cognome": cognome,
	"marca": marca,
	"modello": modello,
	"colore": colore
    }
    self.db[cognome] = prenotazione
    
    # salvataggio del database
    with open("database_prenotazioni.pickle", "wb") as f:
	pickle.dump(self.db, f)
    
    # svuotamento delle caselle di input
    self.nome_entry.delete(0, tk.END)
    self.cognome_entry.delete(0, tk.END)
    self.marca_entry.delete(0, tk.END)
    self.modello_entry.delete(0, tk.END)
    self.colore_entry.delete(0, tk.END)
    
    tk.messagebox.showinfo("Successo", "Prenotazione effettuata con successo")
    
def ricerca(self):
    # recupero del cognome dalle caselle di input
    cognome = self.cognome_ricerca_entry.get()
    
    # controllo dei dati inseriti
    if not cognome:
	tk.messagebox.showwarning("Attenzione", "Inserire il cognome da ricercare")
	return
    
    if cognome not in self.db:
	tk.messagebox.showwarning("Attenzione", "Cognome non presente nel database")
	return
    
    # recupero dei dati dal database
    prenotazione = self.db[cognome]
    nome = prenotazione["nome"]
    cognome = prenotazione["cognome"]
    marca = prenotazione["marca"]
    modello = prenotazione["modello"]
    colore = prenotazione["colore"]
    
    # visualizzazione dei dati recuperati
    tk.messagebox.showinfo("Prenotazione trovata", f"Nome: {nome}\nCognome: {cognome}\nMarca: {marca}\nModello: {modello}\nColore: {colore}")
    
def run(self):
    self.master.mainloop()

root = tk.Tk()
app = App(root)
app.run()


# Audisio 
from tkinter import *
from tkinter import ttk

# funzione per la somma
def calcolo(*args):
	try:
		uno = float(primoNumero.get())
		due = float(secondoNumero.get())
		somma.set(int(uno + due))
	except ValueError:
		pass

root = Tk()
root.title("Somma tra due numeri") # Questo è il nome della finestra che noi andiamo ad inserire

mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

primoNumero = StringVar()
primoNumero_entry = ttk.Entry(mainframe, width = 7, textvariable = primoNumero)
primoNumero_entry.grid(column = 2, row = 1, sticky = (W, E))

secondoNumero = StringVar()
secondoNumero_entry = ttk.Entry(mainframe, width = 1, textvariable = secondoNumero)
secondoNumero_entry.grid(column = 2, row = 2, sticky = (W, E))

somma = StringVar()
ttk.Label(mainframe, textvariable = somma).grid(column = 2, row = 4, sticky = (W, E))

ttk.Button(mainframe, text = "Calcola", command = calcolo). grid(column = 3, row = 4, sticky = W)

ttk.Label(mainframe, text = "Primo numero").grid(column = 3, row = 1, sticky = W)
ttk.Label(mainframe, text = "Secondo numero").grid(column = 3, row = 2, sticky = W)
ttk.Label(mainframe, text = "La somma è").grid(column = 1, row = 4, sticky = E)

for child in mainframe.winfo_children():
	child.grid_configure(padx = 5, pady = 5)

primoNumero_entry.focus() # per avere già il cursore sulla casella di inserimento dei piedi
root.bind("<Return>", calcolo)

root.mainloop()
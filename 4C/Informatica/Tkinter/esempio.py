from tkinter import *
from tkinter import ttk

# funzione per la concersione
def calcolo(*args):
	try:
		value = float(feet.get())
		meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
	except ValueError:
		pass

root = Tk()
root.title("Conversione piedi - metri") # Questo è il nome della finestra che noi andiamo ad inserire

mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width = 7, textvariable = feet)
feet_entry.grid(column = 2, row = 1, sticky = (W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable = meters).grid(column = 2, row = 2, sticky = (W, E))

ttk.Button(mainframe, text = "Calcola", command = calcolo). grid(column = 3, row = 3, sticky = W)

ttk.Label(mainframe, text = "Piedi").grid(column = 3, row = 1, sticky = W)
ttk.Label(mainframe, text = "Equivale a").grid(column = 1, row = 2, sticky = E)
ttk.Label(mainframe, text = "Metri").grid(column = 3, row = 2, sticky = W)

for child in mainframe.winfo_children():
	child.grid_configure(padx = 5, pady = 5)

feet_entry.focus() # per avere già il cursore sulla casella di inserimento dei piedi
root.bind("<Return>", calcolo)

root.mainloop()

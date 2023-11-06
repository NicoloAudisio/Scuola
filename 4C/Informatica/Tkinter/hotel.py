# Audisio Nicolò
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *

root = Tk()
root.title("Hotel - Audisio")
root.geometry("700x500")
root.resizable(0, 0)


# --- FUNZIONI ---
def calcolo():
	try:
		# --- CONTROLLO NOTTI > 0 ---
		notti = int(numeroNotti.get())
		if notti <= 0:
			numeroNotti_entry.config({"background": "red"})
			messagebox.showerror("Errore", "Inserire un numero di notti valido")
		else:
			numeroNotti_entry.config({"background": "white"})
		adulti = int(numeroAdulti.get())
		bambini = int(numeroBambini.get())
		totalePersone.set(int(adulti + bambini))
		singole = int(camereSingole.get())
		notti = int(numeroNotti.get())
		matrimoniali = int(camereMatrimoniali.get())
		totalePrezzo.set(float((singole * 80) + (matrimoniali * 150 )) * notti)
		# --- CONTROLLO PREZZO > 300 ---
		if totalePrezzo.get() > 300:
			totalePrezzo_label.config(fg='blue')
		else:
			totalePrezzo_label.config(fg='green')
	except ValueError:
		messagebox.showerror("Errore", "Errore nell'inserimento dei dati")

def uscita():
	root.destroy()			

def pulisci():
	nomePrenotazione.set("")
	cognomePrenotazione.set("")
	numeroAdulti.set("")
	numeroBambini.set("")
	totalePersone.set("")
	numeroNotti.set("")
	camereSingole.set("")
	camereMatrimoniali.set("")
	totalePrezzo.set("")

def creaFattura():
	file_path = filedialog.asksaveasfilename(defaultextension = ".txt")
	with open(file_path, 'w') as f:
		f.write("Hotel Bella vita - Torino\n")
		f.write(f"Nome: {nomePrenotazione.get()}\n")
		f.write(f"Cognome: {cognomePrenotazione.get()}\n")
		f.write(f"Numero adulti: {numeroAdulti.get()}\n")
		f.write(f"Numero bambini: {numeroBambini.get()}\n")
		f.write(f"Numero notti: {numeroNotti.get()}\n")
		f.write(f"Camere singole: {camereSingole.get()}\n")
		f.write(f"Camere matrimoniali: {camereMatrimoniali.get()}\n")
		f.write(f"Totale: {totalePrezzo.get()} €\n")


Label(root, text = "Prenotazione Hotel Bella vita - Torino").grid(column = 1, row = 1, columnspan = 4,sticky = N)

# --- NOME PRENOTAZIONE ---
nomePrenotazione = StringVar()
nomePrenotazione_entry = Entry(root, textvariable = nomePrenotazione)
nomePrenotazione_entry.grid(column = 2, row = 2, sticky = (W, E), columnspan = 4)
Label(root, text = "Nome prenotazione").grid(column = 1, row = 2, sticky = W)

# --- COGNOME PRENOTAZIONE ---
cognomePrenotazione = StringVar()
cognomePrenotazione_entry = Entry(root, textvariable = cognomePrenotazione)
cognomePrenotazione_entry.grid(column = 2, row = 3, sticky = (W, E), columnspan = 4)
Label(root, text = "Cognome prenotazione").grid(column = 1, row = 3, sticky = W)

# --- NUMERO TOTALE ADULTI ---
numeroAdulti = StringVar()
numeroAdulti_entry = Entry(root, textvariable = numeroAdulti)
numeroAdulti_entry.grid(column = 4, row = 4, sticky = W)
Label(root, text = "Numero adulti").grid(column = 3, row = 4, sticky = W)

# --- NUMERO TOTALE BAMBINI ---
numeroBambini = StringVar()
numeroBambini_entry = Entry(root, textvariable = numeroBambini)
numeroBambini_entry.grid(column = 4, row = 5, sticky = W)
Label(root, text = "Numero bambini").grid(column = 3, row = 5, sticky = W)

# --- NUMERO TOTALE PERSONE ---
totalePersone = StringVar()
Label(root, textvariable = totalePersone).grid(column = 2, row = 4, sticky = W, columnspan = 2, rowspan = 2)
Label(root, text = "Totale persone").grid(column = 1, row = 4, sticky = W, columnspan = 2, rowspan = 2)

# --- NUMERO NOTTI ---
numeroNotti = StringVar()
numeroNotti_entry = Entry(root, textvariable = numeroNotti)
numeroNotti_entry.grid(column = 3, row = 6, sticky = W)
Label(root, text = "Numero notti").grid(column = 2, row = 6, sticky = W)

# --- NUMERO CAMERE SINGOLE ---
camereSingole = StringVar()
camereSingole_entry = Entry(root, textvariable = camereSingole)
camereSingole_entry.grid(column = 2, row = 7, sticky = W)
Label(root, text = "Numero camere singole").grid(column = 1, row = 7, sticky = W)

# --- NUMERO CAMERE MATRIMONIALI ---
camereMatrimoniali = StringVar()
camereMatrimoniali_entry = Entry(root, textvariable = camereMatrimoniali)
camereMatrimoniali_entry.grid(column = 4, row = 7, sticky = W)
Label(root, text = "Numero camere matrimoniali").grid(column = 3, row = 7, sticky = W)

# --- SOMMA DA VERSARE ---
totalePrezzo = DoubleVar()
totalePrezzo_label = Label(root, textvariable = totalePrezzo).grid(column = 3, row=11, sticky = W)
Label(root, text="Somma da versare € ").grid(column = 2, row = 11, sticky = W)

# --- PULSANTE CALCOLA ---
Button(root, text = "Calcola", command = calcolo).grid(column = 2, row = 9)

# --- PULSANTE CANCELLA ---
Button(root, text = "Cancella", command = pulisci).grid(column = 3, row = 9)

# --- PULSANTE CREA FATTURA ---
fatturazione = Button(root, text = "Crea fattura", command = creaFattura).grid(column = 4, row = 9)

# --- PULSANTE ESCI ---
Button(root, text = "Esci", command = uscita).grid(column = 4, row = 12, sticky = E)


nomePrenotazione_entry.focus()
root.mainloop()

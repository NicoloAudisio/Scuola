import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class Finestra(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Battaglia navale") # provvisiorio
        self.geometry("500x500")
        self.resizable(0,0)
        self.crea_widgets()   

    # Funzione esci
    def esci(self):
        root.destroy()

    def crea_widgets(self):
        # Titolo
        frm_intro = tk.Frame(self)
        lbl_intro = tk.Label(frm_intro, text="Battaglia navale", font=("Time New Romans", 20))
        lbl_intro.pack(pady=20)
        frm_intro.pack(pady=10)

        # Scelta del gioco
        frm_game = tk.Frame(self)
        # aggiungere menu
        frm_game.pack(pady=10)

        # Pulsanti di gioco
        frm_button = tk.Frame(self)
        button_game = tk.Button(frm_button, text="Gioca") # aggiunge command con controllo
        button_game.pack(padx=10, side=tk.LEFT)
        button_load = tk.Button(frm_button, text="Carica") # aggiungere command per carico partita
        button_load.pack(padx=10, side=tk.LEFT)
        frm_button.pack(pady=10)

        # Pulsante uscita
        button_exit = tk.Button(self, text="Esci", command=self.esci) # aggiungere command per uscita
        button_exit.pack(side=tk.RIGHT, padx=30, ipadx=20, ipady=10)
        button_exit.pack(pady=10)


root = Finestra()
root.mainloop()
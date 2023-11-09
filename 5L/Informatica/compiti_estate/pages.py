import tkinter as tk
from tkinter import messagebox
from oggetti import Cantina, Stanza, Scaffale, Bottiglia, Vino

class CantinaPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cantina Manager")
        self.geometry("400x300")
        
        self.cantina = Cantina()
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label_nome = tk.Label(self, text="Nome Cantina:")
        self.label_nome.pack()
        
        self.entry_nome = tk.Entry(self)
        self.entry_nome.pack()
        
        self.button_crea_cantina = tk.Button(self, text="Crea Cantina", command=self.crea_cantina)
        self.button_crea_cantina.pack()
        
    def crea_cantina(self):
        nome_cantina = self.entry_nome.get()
        self.cantina.setNome(nome_cantina)
        
        messagebox.showinfo("Cantina Creata", "Cantina creata con successo!")
        
        self.show_stanze_page()
        
    def show_stanze_page(self):
        self.destroy_widgets()
        
        self.stanze_page = StanzePage(self, self.cantina)
        self.stanze_page.pack()
        
    def destroy_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

class StanzePage(tk.Frame):
    def __init__(self, parent, cantina):
        super().__init__(parent)
        
        self.cantina = cantina
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label_stanze = tk.Label(self, text="Stanze:")
        self.label_stanze.pack()
        
        self.button_aggiungi_stanza = tk.Button(self, text="Aggiungi Stanza", command=self.aggiungi_stanza)
        self.button_aggiungi_stanza.pack()
        
        self.button_visualizza_stanze = tk.Button(self, text="Visualizza Stanze", command=self.visualizza_stanze)
        self.button_visualizza_stanze.pack()
        
    def aggiungi_stanza(self):
        self.aggiungi_stanza_dialog = AggiungiStanzaDialog(self)
        
    def visualizza_stanze(self):
        messagebox.showinfo("Elenco Stanze", self.cantina.visualizzaStanze())
        
class AggiungiStanzaDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Aggiungi Stanza")
        
        self.parent = parent
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label_nome = tk.Label(self, text="Nome Stanza:")
        self.label_nome.pack()
        
        self.entry_nome = tk.Entry(self)
        self.entry_nome.pack()
        
        self.label_num_scaffali = tk.Label(self, text="Numero Massimo Scaffali:")
        self.label_num_scaffali.pack()
        
        self.entry_num_scaffali = tk.Entry(self)
        self.entry_num_scaffali.pack()
        
        self.label_dimensione = tk.Label(self, text="Dimensione:")
        self.label_dimensione.pack()
        
        self.entry_dimensione = tk.Entry(self)
        self.entry_dimensione.pack()
        
        self.button_aggiungi = tk.Button(self, text="Aggiungi", command=self.aggiungi_stanza)
        self.button_aggiungi.pack()
        
    def aggiungi_stanza(self):
        nome_stanza = self.entry_nome.get()
        num_scaffali = int(self.entry_num_scaffali.get())
        dimensione = int(self.entry_dimensione.get())
        
        stanza = self.parent.cantina.creaStanza(nome_stanza, num_scaffali, dimensione)
        
        messagebox.showinfo("Stanza Aggiunta", f"Stanza {stanza.getNome()} aggiunta con successo!")
        
        self.destroy()

if __name__ == "__main__":
    app = CantinaPage()
    app.mainloop()

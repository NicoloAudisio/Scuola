# Audisio Nicolò classe 4c esercizio
import os
import time

class Squadra:
    def __init__(self, nome, vinte=0, perse=0, pareggiate=0):
        self.nome = nome
        self.vinte = vinte
        self.perse = perse
        self.pareggiate = pareggiate

    def punti(self):
        return self.vinte * 3 + self.pareggiate * 1

    def inizioanno(self):
        self.vinte = 0
        self.perse = 0
        self.pareggiate = 0

    def partitePerse(self, punteggio):
        self.perse = punteggio
    
    #la funzione __add__ serve per crere un terzo oggetto dalla somma di due oggetti
    def __add__(self, punteggio):
        self.pareggiate += punteggio
        return self

    #la funzione __mul__ serve per implementare l'operazione di moltiplicazione artmetica
    def __mul__(self, punteggio):
        self.vinte += punteggio
        return self

    #la funzione __sub__ serve per creare un terzo oggetto dovuto dalla sottrazione dei primi due
    def __sub__(self, squadra2):
        differenza = self.punti() - squadra2.punti()
        if differenza > 0:
            return f"\nLa squdra: {self.nome} ha {differenza} punti in più di {squadra2.nome}"
        else:
            return f"\nLa squadra: {squadra2.nome} ha {abs(differenza)} punti in più di {self.nome}"
            #abs serve per restituire il valore assoluto del numero contenuto nella varibile

    def __int__(self):
        return self.punti()

    def __str__(self):
        return f"\n{self.nome}\nPunteggio partite vinte: {self.vinte}\nPunteggio partite pareggiate: {self.pareggiate}\nPartite perse: {self.perse}"

def inserimentoNominativo():
    nomeSquadra = input("Inserisci il nome della prima squadra: ")
    nomeSquadra = nomeSquadra[0].upper() + nomeSquadra[1:]
    squadra = Squadra(nomeSquadra)
    return squadra

def inserimentiDati(squadra):
    partiteVS = int(input("Quante partite sono state vinte dalla prima squadra: "))
    squadra * partiteVS
    partitePS = int(input("Quante partite sono state pareggiate dalla prima squadra: "))
    squadra + partitePS
    partitePeS = int(input("Quante partite sono state perse dalla prima squadra: "))
    squadra.partitePerse(partitePeS)

def stampaDati(squadra1, squadra2):
    print("""
    ---------------------
    | RESOCONTO SQUADRE |
    ---------------------
    """)
    print(squadra1)
    print(squadra2)
    print(squadra1 - squadra2)
    print("Punteggio 1° squadra: ", int(squadra1), " punti")
    print("Punteggio 2° squadra: ", int(squadra2), " punti")
    uscita()

def uscita():
    continuo = input("")
    print("Uscita in corso...")
    time.sleep(1)
    os.system("clear")
# MAIN
os.system("clear")
#inserimento nome squadre
squadra1 = inserimentoNominativo()
squadra2 = inserimentoNominativo()
os.system("clear")
#inserimento dati squadre
inserimentiDati(squadra1)
os.system("clear")
inserimentiDati(squadra2)
#stampa
os.system("clear")
stampaDati(squadra1, squadra2)
import os
from operator import itemgetter

voti = dict()
alunni = 3

def inserimento(voti, alunni):
    for i in range(alunni):
        os.system('clear')

        print("Alunno ", i + 1, "\n")
        nome = input("Inserisci il nome: ")
        while len(nome) == 1:
            nome = input("Errore!\nInserisci il nome: ")
        voto = float(input("Inserisci il voto di " + nome + ": "))
        while voto < 1 or voto > 10:
            voto = float(input("Errore!\nInserisci il voto di " + nome + ": "))
        voti[nome] = voto
        os.system('clear')
    stampa(voti)
    ordinato = list(sorted(voti.items(), key = itemgetter(1)))
    print("DIZIONARIO ORDINATO\n")
    stampa(ordinato)

def stampa(voti):
    print(voti)

inserimento(voti, alunni)

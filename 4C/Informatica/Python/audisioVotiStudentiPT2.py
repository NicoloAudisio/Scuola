import os
from operator import itemgetter

voti = dict()
alunni = 3

#INSERIMENTO
for i in range(alunni):
    os.system('clear')
    print("Alunno ", i + 1)
    nome = input("Inserisci il nome dell'alunno: ")
    while len(nome) < 1: 
        nome = input("Errore!\nInserisci il nome dell'alunno: ")
    voto1 = float(input("Inserisci il primo voto di " + nome + ": "))
    while voto1 < 1 or voto1 > 10:
        voto1 = float(input("Errore!\nInserisci il primo voto di " + nome + ": "))
    voto2 = float(input("Inserisci il secondo voto di " + nome + ": "))
    while voto2 < 1 or voto2 > 10:
        voto2 = float(input("Errore!\nInserisci il secondo voto di " + nome + ": "))
    voti[nome] = voto1, voto2
os.system('clear')
print(voti)

#RICERCA
errore = 0
ricerca = input("Inseisci il nome da cercare: ")
etichette = voti.keys()
risRicerca = voti.pop(ricerca)
if risRicerca == True:
    print(risRicerca)
else:
    errore += 1
if errore != 0:
    print("Errore!\n")



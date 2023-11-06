#Audisio 4c esercizio
import os
import calcoli

prodotti = []
prodotto = []
prezzoM = 0
quantitaM = 0
totVendite = 0
y = 0

def inputNProdotti():
    os.system('clear')
    print("-" * 10 + " GESTIONE MAGAZZINO " + "-" * 10)
    nProdotti = int(input("\nInserire il numero di prodotti: "))
    while nProdotti < 1:
        nProdotti = int(input("Errore!\nInserire il numero di prodotti: "))
    return nProdotti

def svolgimento(nProdotti, y, prezzoM, quantitaM, totVendite):
    for i in range(nProdotti):
        os.system('clear')
        prodotto = []
        y += 1
        print("Prodotto ", y)
        nome = input("\nInserisci il nome del prodotto: ")
        while len(nome) < 1:
            nome = input("Errore!\nInserisci il nome del prodotto: ")
        nome = nome[0].upper() + nome[1:].lower()
        prodotto.append(nome)
        venduti = int(input("\nInserisci la quantità venduta del prodotto " + nome + ": "))
        while venduti < 1:
            venduti = int(input("Errore!\nInserisci la quantità venduta del prodotto " + nome + ": "))
        prodotto.append(venduti)
        prezzo = float(input("\nInserisci il prezzo del prodotto " + nome + ": "))
        while prezzo < 0:
            prezzo = float(input("Errore!\nInserisci il prezzo del prodotto " + nome + ": "))
        prodotto.append(prezzo)
        prodotti.append(prodotto)
        prezzoM = calcoli.somma(prezzoM, prezzo)
        quantitaM = calcoli.somma(quantitaM, venduti)
        totVendite = calcoli.somma(totVendite, prezzo)
    prezzoM = calcoli.calcoloMedia(prezzoM, nProdotti)
    prezzoM = round(prezzoM, 2)
    quantitaM = calcoli.calcoloMedia(quantitaM, nProdotti)
    quantitaM = round(quantitaM, 2)
    stampaFinale(prodotti, nProdotti, totVendite, prezzoM, quantitaM)    

def stampaFinale(prodotti, nProdotti, totVendite, prezzoM, quantitaM):
    os.system('clear')
    print("-" * 10 + " RESOCONTO FINALE " + "-" * 10 + "\n")
    for i in range(nProdotti):
            print('Prodotto: {0:<10} Quantità venduta: {1:^10} Prezzo: {2:>10} €'.format(prodotti[i][0], prodotti[i][1], prodotti[i][2]))
    print('\nTotale incassi: € {0:<10} Prezzo medio: € {1:^10} Quantità media prodotti venduti: {2:>10}'.format(totVendite, prezzoM, quantitaM))
    continuo = input("")
    os.system('clear')

nProdotti = inputNProdotti()
svolgimento(nProdotti, y, prezzoM, quantitaM, totVendite)
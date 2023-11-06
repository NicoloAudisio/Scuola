import os

def stampaTraduzione(fraseTradotta):
    print("\nLa parola tradotta è: ", fraseTradotta)
    avanti = input("")

def uscita(frasiT, paroleTradotte):
    os.system('clear')
    if frasiT == 1:
        print("Hai tradotto una sola frase!\n")
    elif frasiT >= 2:
        print("Hai tradotto ", frasiT ," frasi\n")
    for i in range(len(paroleTradotte)):
    	print('Parole tradotte: {0:<10}'.format(paroleTradotte[i]))
    print("\nUscita in corso...")
    avanti = input("")
    os.system('clear')

def traduzione():
    continuo = 0
    frasiT = 0
    paroleTradotte = []
    while continuo == 0:
        fraseTradotta = ''
        os.system('clear')
        print('{0:^50}'.format("Traduttore Italiano Rovarspraket"))
        frase = input("\nInserisci la frase in italiano: ")
        while len(frase) == 0:
            frase = input("Errore!\nInserisci la frase in italiano: ")
        for i in range(len(frase)):
            if frase[i] == 'a' or frase[i] == 'e' or frase[i] == 'i' or frase[i] == 'o' or frase[i] == 'u':
                fraseTradotta = fraseTradotta + frase[i]
            elif frase[i] < "A" or frase[i] > "z":
                fraseTradotta = fraseTradotta + frase[i] 
            else:
                consonanti = frase[i] + "o" + frase[i]
                fraseTradotta = fraseTradotta + consonanti
        stampaTraduzione(fraseTradotta)
        frasiT += 1
        paroleTradotte.append(fraseTradotta)
        continuo = input("Vuoi tradurre un'altra frase (yes - no): ")
        if continuo == 'yes' or continuo == 'Yes' or continuo == 'YES' or continuo == 'yEs' or continuo == 'yeS':
            continuo = 0
        elif continuo == 'no' or continuo == 'No' or continuo == 'nO': 
            uscita(frasiT, paroleTradotte)
        os.system('clear')
    return fraseTradotta

os.system('clear')
fraseTradotta = traduzione()

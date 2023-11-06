# Audisio 4c esercizio

# IMPORTAZIONI
import os

# FUNZIONI
def controlloStr(oC, f):
    while len(oC) < 1:
        oC = input(f)
    while True:
        try:
            return str(oC)
        except:
            oC = input(f)

def controlloInt(nC, f = "Inserisci un numero: "):
    while True:
        try:
            return int(nC)
        except ValueError:
            nC = input(f)

def controlloFloat(nC, f = "Inserisci un numero: "):
    while True:
        try:
            return float(nC)
        except ValueError:
            nC = input(f)

def aggiungiVeicoloCommerciale():
    marcaVeicoloCommerciale = controlloStr(input("Inserisci la marca del veicolo commerciale: "), "Inserisci la marca del veicolo commerciale: ")
    modelloVeicoloCommerciale = controlloStr(input("Inserisci il modello del veicolo commerciale: "), "Inserisci il modello del veicolo commerciale: ")
    annoVeicoloCommerciale = controlloInt(input("Inserisci l'anno del veicolo commerciale: "))
    targaVeicoloCommerciale = input("Inserisci la targa del veicolo commerciale: ")
    pesoCaricoVeicoloCommerciale = controlloFloat(input("Inserisci il peso carico del veicolo commerciale: "))
    pesoVuotoVeicoloCommerciale = controlloFloat(input("Inserisci il peso vuoto del veicolo commerciale: "))
    articolatoVeicoloCommerciale = input("Veicolo autoarticolato (True / False) : ")
    veicoloCommerciale = VeicoloCommerciale(marcaVeicoloCommerciale, modelloVeicoloCommerciale, annoVeicoloCommerciale, targaVeicoloCommerciale, pesoCaricoVeicoloCommerciale, pesoVuotoVeicoloCommerciale, articolatoVeicoloCommerciale)
    concessionario.CompraVeicolo(veicoloCommerciale)
    print("\nPremi invio per continuare...\n")
    continuo = input("")

def aggiungiVeicoloPrivato():
    marcaVeicoloPrivato = controlloStr(input("Inserisci la marca del veicolo privato: "), "Inserisci la marca del veicolo privato: ")
    modelloVeicoloPrivato = controlloStr(input("Inserisci il modello del veicolo privato: "), "Inserisci il modello del veicolo privato: ")
    annoVeicoloPrivato = controlloInt(input("Inserisci l'anno del veicolo privato: "))
    targaVeicoloPrivato = input("Inserisci la targa del veicolo privato: ")
    porteVeicoloPrivato = controlloInt(input("Inserisci il numero di porte del veicolo privato: "))
    postiVeicoloPrivato = controlloInt(input("Inserisci i posti del veicolo privato: "))
    veicoloPrivato = VeicoloPrivato(marcaVeicoloPrivato, modelloVeicoloPrivato, annoVeicoloPrivato, targaVeicoloPrivato, postiVeicoloPrivato, porteVeicoloPrivato)
    concessionario.CompraVeicolo(veicoloPrivato)
    print("\nPremi invio per continuare...\n")
    continuo = input("")

# CLASSE VEICOLO

class Autoveicolo:
    def __init__(self, marca: str, modello: str, anno: int, targa: str):
        self.__marca = marca
        self.__modello = modello
        self.__anno = anno
        self.__targa = targa
    
    def __str__(self):
        return f"\nMarca: {self.__marca}\nModello: {self.__modello}\nAnno: {self.__anno}\nTarga: {self.__targa}\n"
    
    def set_marca(self, marca):
        self.__marca = marca
    
    def get_marca(self):
        return self.__marca
    
    def set_modello(self, modello):
        self.__modello = modello
    
    def get_modello(self):
        return self.__modello

    def set_anno(self, anno):
        self.__anno = anno
    
    def get_anno(self):
        return self.__anno    

    def set_targa(self, targa):
        self.__targa = targa
    
    def get_targa(self):
        return self.__targa

# CLASSE VEICOLO PRIVATO

class VeicoloPrivato(Autoveicolo):
    def __init__(self, marca: str, modello: str, anno: int, targa: str, numeroPosti: int, numeroPorte: int):
        super().__init__(marca, modello, anno, targa)
        self.__numeroPosti = numeroPosti
        self.__numeroPorte = numeroPorte
    
    def __str__(self):
        return f"Veicolo Privato\n{super().__str__()}\nNumero posti: {self.__numeroPosti}\nNumero porte: {self.__numeroPorte}\n"
    
    def set_numeroPosti(self, numeroPosti):
        self.__numeroPosti = numeroPosti
    
    def get_numeroPosti(self):
        return self.__numeroPosti    

    def set_numeroPorte(self, numeroPorte):
        self.__numeroPorte = numeroPorte
    
    def get_numeroPorte(self):
        return self.__numeroPorte

# CLASSE VEICOLO COMMERCIALE

class VeicoloCommerciale(Autoveicolo):
    def __init__(self, marca: str, modello: str, anno: int, targa: str, pesoCarico: float, pesoVuoto: float, articolato: False):
        super().__init__(marca, modello, anno, targa)
        self.__pesoCarico = pesoCarico
        self.__pesoVuoto = pesoVuoto
        self.__articolato = articolato
    
    def __str__(self):
        return f"Veicolo Commerciale\n{super().__str__()}\nPeso carico: {self.__pesoCarico} kg\nPeso scarico: {self.__pesoVuoto} kg\n\nArticolato: {self.__articolato}\n"
    
    def set_pesoCarico(self, pesoCarico):
        self.__pesoCarico = pesoCarico
    
    def get_pesoCarico(self):
        return self.__pesoCarico    

    def set_pesoVuoto(self, pesoVuoto):
        self.__pesoVuoto = pesoVuoto
    
    def get_pesoVuoto(self):
        return self.__pesoVuoto
    
    def set_articolato(self, articolato):
        self.__articolato = articolato
    
    def get_articolato(self):
        return self.__articolato

# CLASSE CONCESSIONARIO

class Concessionario:
    def __init__(self, nomeConcessiorio: str):
        self.__nome = nomeConcessiorio
        self.__veicoli = []

    def __str__(self):
        v = 0
        frase = ""
        for i in self.list:
            v += 1
            if v != 1:
                frase = frase + (f"Veicolo Commerciale\n{super().__str__()}\nPeso carico: {self.__pesoCarico} kg\nPeso scarico: {self.__pesoVuoto} kg\n\nArticolato: {self.__articolato}\n")
            else:
                frase = frase + (f"Veicolo Privato\n{super().__str__()}\nNumero posti: {self.__numeroPosti}\nNumero porte: {self.__numeroPorte}\n")
        return f"{frase}"

    def set_nome(self, nomeConcessionario: str):
        self.__nome = nomeConcessionario
    
    def get_pesoVuoto(self):
        return self.__nome

    def CompraVeicolo(self, veicolo: Autoveicolo):
        self.__veicoli.append(veicolo)
    
    def get_veicoli(self):
        return self.__veicoli
    
    def VendiVeicolo(self, targa: str):
        nTrovato = 0
        for veicolo in self.__veicoli:
            if veicolo.get_targa() == targa:
                self.__veicoli.remove(veicolo)
                return  
            else:
                nTrovato += 1
        if nTrovato > 0:
            print("Veicolo non trovato!\n")


os.system("clear")
inputNomeConcessionario = controlloStr(input("Inserisci il nome del concessionario: "), "Inserisci il nome del concessionario: ")
concessionario = Concessionario(inputNomeConcessionario)
for i in range(2):
    os.system("clear")
    aggiungiVeicoloCommerciale()
os.system("clear")
aggiungiVeicoloPrivato()
os.system("clear")
print(concessionario)
continuo = input("")
os.system("clear")
print(concessionario)
continuo = input("")
os.system("clear")
targaVenditaVeicolo = input("Inserisci la targa del veicolo venduto: ")
concessionario.VendiVeicolo(targaVenditaVeicolo)
print(concessionario)
print("\nPremi invio per terminare...\n")
continuo = input("")
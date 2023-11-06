#Audisio 4c esercizio

class Rettangolo(object):
    def __init__(self, base = 0, altezza = 0):
        self.setBase(base)
        self.setAltezza(altezza)
    
    def setBase(self, b):
        self.__base = b

    def setAltezza(self, a):
        self.__altezza = a

    def getBase(self):
        return self.__base
    
    def getAltezza(self):
        return self.__altezza
    
    def calcoloArea(self):
        area = self.getBase() * self.getAltezza()
        return area

    def stampa(self):
        print('\n\nBase: {0} \nAltezza: {1} \nArea: {2}'.format(self.getBase(), self.getAltezza(), self.calcoloArea()))

base = int(input("Inserisci la base: "))
while base <= 0:
    base = int(input("\nErrore!\nInserisci la base: "))
altezza = int(input("Inserisci l'altezza: "))
while altezza <= 0:
    altezza = int(input("\nErrore!\nInserisci l'altezza: "))
area = Rettangolo(base, altezza)
area.stampa()
#Audisio 4c esercizio

class Punto(object):
    def __init__(self, x = 0, y = 0):
        self.setX(x)
        self.setY(y)

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def calcoloDistanzaX(self):
        distanzaX = self.getX() - 0
        return distanzaX
    
    def calcoloDistanzaY(self):
        distanzaY = self.getY() - 0
        return distanzaY

    def calcoloLunghezza(self):
        if self.getX() > self.getY():
            distanza = self.getX() - self.getY()
        else:
            distanza = self.getY() - self.getX()
        return distanza

    def stampa(self):
        print('\n\nX: {0}\nY:{1}\nIl segmento dista {2} sull\'asse X e {3} sull\'asse Y e ha una lunghezza di {4}'.format(self.getX(), self.getY(), self.calcoloDistanzaX(), self.calcoloDistanzaY(), self.calcoloLunghezza()))

x = int(input("Inserisci la coordinata di X: "))
y = int(input("Inserisci la coordinata di Y: "))
distanza = Punto(x, y)
distanza.stampa()
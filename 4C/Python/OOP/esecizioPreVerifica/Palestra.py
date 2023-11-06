# Audisio Esercizio pre verifica
class Circolo():
    def __init__(self, nome = "", listaIscritti = []):
        self.setNome(nome)
        self.__listaIscritti = []
    
    def setNome(self, nome):
        self.__nome = nome
    
    def getNome(self):
        return self.__nome
    
    def aggiungiIsciritto(self, iscritto):
        self.__listaIscritti.append(iscritto)
    
    def getListaIscritti(self):
        return self.__listaIscritti
    
    def trovaIscritto(self, ricerca):
        trovato = 0
        for atleta in self.__listaIscritti:
            if ricerca == atleta.getNome():
                trovato = 1
                pass
            else:
                trovato = 0
        if trovato == 1:
            print("utente trovato")
        else:
            print("utente non trovato")

palestra = Circolo("Ciao")
utente1 = palestra.aggiungiIsciritto("Nicolò")
ricerca = palestra.trovaIscritto("Nicolò")

print(ricerca)

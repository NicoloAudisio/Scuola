# Audisio 4c esercizio

class Disciplina():
    def __init__(self, nome: str, costoMensile: float):
        self.nome = nome
        self.costoMensile = costoMensile
    
    def __str__(self):
        return f"Nome: {self.nome}\nCosto mensile: {self.costoMensile}€"

    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setCostoMensile(self, costoMensile):
        self.costoMensile = costoMensile
    
    def getCostoMensile(self):
        return self.costoMensile

class Nuoto(Disciplina):
    def __init__(self, listaIscritto: list, nome, costoMensile):
        super().__init__(nome, costoMensile)
        self.listaIscritto = listaIscritto
    
    def setListaIscritto(self, listaIscritto):
        self.listaIscritto = listaIscritto
    
    def getListaIscritto(self):
        return self.listaIscritto
    
class Aerobica(Disciplina):
    def __init__(self, listaIscritto: list, nome, costoMensile):
        super().__init__(nome, costoMensile)
        self.listaIscritto = listaIscritto
    
    def setListaIscritto(self, listaIscritto):
        self.listaIscritto = listaIscritto
    
    def getListaIscritto(self):
        return self.listaIscritto

class Bodybuilding(Disciplina):
    def __init__(self, listaIscritto: list, nome, costoMensile):
        super().__init__(nome, costoMensile)
        self.listaIscritto = listaIscritto
    
    def setListaIscritto(self, listaIscritto):
        self.listaIscritto = listaIscritto
    
    def getListaIscritto(self):
        return self.listaIscritto

class Iscritto():
    def __init__(self, nome: str, cognome: str, listaCorsi: list):
        self.nome = nome
        self.cognome = cognome
        self.listaCorsi = listaCorsi
    
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setCognome(self, cognome):
        self.cognome = cognome
    
    def getCognome(self):
        return self.cognome
    
    def setListaCorsi(self, listaCorsi):
        self.listaCorsi = listaCorsi
    
    def getListaCorsi(self):
        return self.listaCorsi

    def aggiungiCorsi(self, corso):
        self.listaCorsi.append(corso)
    
    def stampaListaCorsi(self, listaCorsi):
        for i in listaCorsi:
            print(self.getNome())

class Circolo():
    def __init__(self, nome: str, listaIscritti: list):
        self.nome = nome
        self.listaIscritti = listaIscritti
    
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def aggiungiIscritto(self, iscritto):
        self.listaIscritti.append(iscritto)
    
    def stampaListaIscritti(self, listaIscritti):
        for i in listaIscritti:
            print(self.getNome() + " " + self.getCognome())
    
    def trovaIscritto(self, nome, cognome):
        for iscritto in self.lista_iscritti:
            if iscritto.get_nome() == nome and iscritto.get_cognome() == cognome:
                return iscritto
        return None
    
    def aggiungiDisciplina(self, disciplina):
        self.listaDiscipline.append(disciplina)
	
    def trova_disciplina(self, nome):
        for disciplina in self.listaDiscipline:
            if disciplina.get_nome() == nome:
                return disciplina
        return None

#controllo
discplina = Disciplina("Nicolò", 450.50)
print(discplina)
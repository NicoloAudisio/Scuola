#Audisio 4c esercizio oggetto Persona

class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    
    def __str__(self):
        return f"{self.nome} {self.cognome}"
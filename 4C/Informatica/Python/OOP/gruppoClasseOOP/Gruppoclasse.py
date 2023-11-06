#Audisio 4c esercizio oggetto Gruppoclasse

class Gruppoclasse:
    def __init__(self, nome):
        self.nome = nome
        self.studenti = []
        
    def aggiungi_studente(self, studente):
        self.studenti.append(studente)
        
    def rimuovi_studente(self, studente):
        self.studenti.remove(studente)
        
    def __str__(self):
        res = f"Gruppoclasse {self.nome}\n"
        for studente in self.studenti:
            res += str(studente) + "\n"
        return res
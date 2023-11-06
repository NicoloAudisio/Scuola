#Audisio 4c esercizio oggetto Studente

class Studente:
    def __init__(self, alunno, età, voti):
        self.età = età
        self.voti = voti
        self.alunno = alunno
        
    def aggiungi_voto(self, voto):
        self.voti.append(voto)
        
    def media_voti(self):
        return sum(self.voti) / len(self.voti)
    
    def __str__(self):
        return f"{self.alunno}: età {self.età}, voti {self.voti}, media {self.media_voti():.2f}"
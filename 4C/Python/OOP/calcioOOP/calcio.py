class Squadra:
    def __init__(self, nome, vinte=0, perse=0, pareggiate=0):
        self.nome = nome
        self.vinte = vinte
        self.perse = perse
        self.pareggiate = pareggiate

    def punti(self):
        return self.vinte * 3 + self.pareggiate * 1

    def inizioanno(self):
        self.vinte = 0
        self.perse = 0
        self.pareggiate = 0

    def __add__(self, altro):
        self.pareggiate += altro
        return self

    def __mul__(self, altro):
        self.vinte += altro
        return self

    def __sub__(self, altro):
        differenza = self.punti() - altro.punti()
        if differenza > 0:
            return f"La squdra: {self.nome} ha {differenza} punti in più di {altro.nome}"
        else:
            return f"La squadra: {altro.nome} ha {abs(differenza)} punti in più di {self.nome}"

    def __int__(self):
        return self.punti()

    def __str__(self):
        return f"La squadra: {self.nome} ha vinto {self.vinte} partite, ha perso {self.perse} partite e ha pareggiato {self.pareggiate} partite"

    
milan = Squadra("Milan")
juventus = Squadra("Juventus")

a = 4
b = 2

milan + a
milan * b

print(milan)

print(juventus)

print(milan - juventus)
print("Punti Milan: ", int(milan))

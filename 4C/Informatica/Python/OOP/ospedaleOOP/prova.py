class Lampada:
    def __init__(self, nome):
        self.nome = nome

class Comodino:
    def __init__(self, nome):
        self.nome = nome

class Stanza:
    def __init__(self, lampada1, lampada2, comodino):
        self.lampada1 = lampada1
        self.lampada2 = lampada2
        self.comodino = comodino
        self.lista_oggetti = [lampada1, lampada2, comodino]

class Vendita:
    def __init__(self, stanza):
        self.stanza = stanza

    def stampa_oggetti_casa(self):
        print(f"Oggetto Stanza: {self.stanza}")
        print("Lista oggetti della casa:")
        for oggetto in self.stanza.lista_oggetti:
            print(oggetto.nome)


# Creazione degli oggetti
lampada1 = Lampada("Lampada da tavolo")
lampada2 = Lampada("Lampada da soffitto")
comodino = Comodino("Comodino")

stanza = Stanza(lampada1, lampada2, comodino)
vendita = Vendita(stanza)

# Stampa degli oggetti della casa
vendita.stampa_oggetti_casa()
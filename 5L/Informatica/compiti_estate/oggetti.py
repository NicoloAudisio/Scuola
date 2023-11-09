import json

class Cantina:
    def __init__(self):
        self.nome = ""
        self.stanze = []
    
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def creaStanza(self, nome, numMaxScaffali, dimensione):
        stanza = Stanza(nome, numMaxScaffali, dimensione)
        self.stanze.append(stanza)
        return stanza
    
    def visualizzaStanze(self):
        stanze = ""
        for stanza in self.stanze:
            stanze += f"Nome stanza: {stanza.getNome()}\n"
            stanze += stanza.visualizzaScaffali() + "\n"
        return stanze

class Stanza:
    def __init__(self, nome, numMaxScaffali, dimensione):
        self.nome = nome
        self.numMaxScaffali = numMaxScaffali
        self.dimensione = dimensione
        self.scaffali = []
    
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def creaScaffale(self, nome, numMaxBottiglie):
        scaffale = Scaffale(nome, numMaxBottiglie)
        self.scaffali.append(scaffale)
        return scaffale
    
    def visualizzaScaffali(self):
        scaffali = ""
        for scaffale in self.scaffali:
            scaffali += f"Nome scaffale: {scaffale.getNome()}\n"
            scaffali += scaffale.visualizzaBottiglie() + "\n"
        return scaffali

class Scaffale:
    def __init__(self, nome, numMaxBottiglie):
        self.nome = nome
        self.numMaxBottiglie = numMaxBottiglie
        self.bottiglie = []
    
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def aggBottiglia(self, bottiglia):
        if len(self.bottiglie) < self.numMaxBottiglie:
            self.bottiglie.append(bottiglia)
            bottiglia.setPosizione(self.nome)
        else:
            return "Lo scaffale è pieno!"
    
    def visualizzaBottiglie(self):
        bottiglie = ""
        for bottiglia in self.bottiglie:
            bottiglie += f"Sigla bottiglia: {bottiglia.getSigla()}\n"
            bottiglie += f"Vino: {bottiglia.getVino().getNome()} - {bottiglia.getVino().getTipo()}\n"
        return bottiglie

class Bottiglia:
    def __init__(self, sigla, vino):
        self.sigla = sigla
        self.vino = vino
        self.posizione = ""
    
    def setSigla(self, sigla):
        self.sigla = sigla
    
    def getSigla(self):
        return self.sigla
    
    def setVino(self, vino):
        self.vino = vino
    
    def getVino(self):
        return self.vino
    
    def setPosizione(self, posizione):
        self.posizione = posizione
    
    def getPosizione(self):
        return self.posizione

class Vino:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
    
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setTipo(self, tipo):
        self.tipo = tipo
    
    def getTipo(self):
        return self.tipo

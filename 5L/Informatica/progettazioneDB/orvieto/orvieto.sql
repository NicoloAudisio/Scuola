CREATE TABLE Concerto (
    Codice INT PRIMARY KEY,
    Titolo VARCHAR(255),
    Descrizione TEXT,
    CodiceSala INT,
    NomeOrchestra VARCHAR(255),
    FOREIGN KEY (CodiceSala) REFERENCES Sala(Codice),
    FOREIGN KEY (NomeOrchestra) REFERENCES Orchestra(Nome)
);

CREATE TABLE Pezzo (
    Codice INT PRIMARY KEY,
    Titolo VARCHAR(255)
);

CREATE TABLE Autore (
    Codice INT PRIMARY KEY,
    Nome VARCHAR(255)
);

CREATE TABLE Orchestra (
    Nome VARCHAR(255) PRIMARY KEY,
    MatricolaDirettore INT,
    FOREIGN KEY (MatricolaDirettore) REFERENCES Orchestrale(Matricola)
);

CREATE TABLE Orchestrale (
    Matricola INT PRIMARY KEY,
    Nome VARCHAR(255),
    Cognome VARCHAR(255)
);

CREATE TABLE Strumento (
    Nome VARCHAR(255) PRIMARY KEY
);

CREATE TABLE Sala (
    Codice INT PRIMARY KEY,
    Nome VARCHAR(255),
    Capienza INT
);

CREATE TABLE CompostoDa (
    CodiceConcerto INT,
    CodicePezzo INT,
    PRIMARY KEY (CodiceConcerto, CodicePezzo),
    FOREIGN KEY (CodiceConcerto) REFERENCES Concerto(Codice),
    FOREIGN KEY (CodicePezzo) REFERENCES Pezzo(Codice)
);

CREATE TABLE AutorePezzo (
    CodicePezzo INT,
    CodiceAutore INT,
    PRIMARY KEY (CodicePezzo, CodiceAutore),
    FOREIGN KEY (CodicePezzo) REFERENCES Pezzo(Codice),
    FOREIGN KEY (CodiceAutore) REFERENCES Autore(Codice)
);

CREATE TABLE Partecipa (
    NomeOrchestra VARCHAR(255),
    MatricolaOrchestrale INT,
    PRIMARY KEY (NomeOrchestra, MatricolaOrchestrale),
    FOREIGN KEY (NomeOrchestra) REFERENCES Orchestra(Nome),
    FOREIGN KEY (MatricolaOrchestrale) REFERENCES Orchestrale(Matricola)
);

CREATE TABLE Suona (
    MatricolaOrchestrale INT,
    NomeStrumento VARCHAR(255),
    PRIMARY KEY (MatricolaOrchestrale, NomeStrumento),
    FOREIGN KEY (MatricolaOrchestrale) REFERENCES Orchestrale(Matricola),
    FOREIGN KEY (NomeStrumento) REFERENCES Strumento(Nome)
);

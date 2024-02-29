CREATE database Studenti;
USE Studenti;

-- Creazione della tabella "Studenti"
CREATE TABLE Studenti (
    ID_studente INT PRIMARY KEY,
    Cognome VARCHAR(255),
    Nome VARCHAR(255),
    DataNascita DATE,
    Indirizzo VARCHAR(255),
    CorsoLaurea VARCHAR(255),
    Id_Esame INT
);

-- Creazione della tabella "Esami"
CREATE TABLE Esami (
    ID_Esame INT PRIMARY KEY,
    Nome_Esame VARCHAR(255),
    Crediti INT,
    Aula VARCHAR(255),
    Orario VARCHAR(255)
);

-- Aggiunta del vincolo di chiave esterna alla tabella "Studenti"
ALTER TABLE Studenti
ADD FOREIGN KEY (Id_Esame) REFERENCES Esami(ID_Esame);

-- Audisio Nicolò 5L - Struttura
DROP DATABASE IF EXISTS Dipendenti;
CREATE DATABASE IF NOT EXISTS Dipendenti;
USE Dipendenti;

-- Dipartimenti
CREATE TABLE IF NOT EXISTS Dipartimenti(
    CodDip VARCHAR(5) NOT NULL PRIMARY KEY,
    Descrizione TEXT NOT NULL,
    Sede VARCHAR(50) NOT NULL,
    Uffici VARCHAR(5)
);

-- Impiegati
CREATE TABLE IF NOT EXISTS Impiegati(
    IdImpiegato VARCHAR(5) NOT NULL PRIMARY KEY,
    Nome VARCHAR(30) NOT NULL,
    Cognome VARCHAR(30) NOT NULL,
    Residenza VARCHAR(50) NOT NULL,
    Stipendio INT NOT NULL,
    Dipartimento VARCHAR(5) NOT NULL,
    FOREIGN KEY(Dipartimento) REFERENCES Dipartimenti(CodDip)
);
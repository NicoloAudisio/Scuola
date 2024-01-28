DROP database mostraCanina;

CREATE DATABASE IF NOT EXISTS mostraCanina;
SHOW DATABASES;

USE mostraCanina;

-- Creazione tabella razze
-- pk: nome
CREATE TABLE Razze (
    nomeRazza VARCHAR(100) PRIMARY KEY,
    altezzaRazza FLOAT NOT NULL,
    pesoRazza FLOAT NOT NULL,
    
);

echo "Tbalella razza creata con successo!"

-- Creazione tabella cani 
-- pk: codice
-- pe: razza(nomeRazza)
CREATE TABLE CANI (
    codiceCane INT PRIMARY KEY,
    nomeCane VARCHAR(100) NOT NULL,
    dataDiNascitaCane DATE NOT NULL,
    altezzaCane FLOAT NOT NULL,
    pesoCane FLOAT NOT NULL,
    razzaCane VARCHAR(100) NOT NULL,
    datiProprietario VARCHAR(200) NOT NULL,
    FOREIGN KEY (razza) REFERENCES RAZZA(nomeRazza)
);

echo "Tabella cani creata con successo!"

-- Creazione tabella giudici
-- pk: codiceGiudici
CREATE TABLE GIUDICI (
    codiceGiudice INT PRIMARY KEY
    nomeGiudice VARCHAR(100) NOT NULL
);

echo "Tabella giudici creata con successo!"

-- Creazione tabella voti
-- pk: codiceGiudice, codiceCane
-- pe: codiceGiudici
-- pe: codiceCane

CREATE TABLE VOTI (
    codiceGiudice INT NOT NULL,
    codiceCane INT NOT NULL,
    votoCane INT NOT NULL,
    PRIMARY KEY(codiceGiudice, codiceCane),
    FOREIGN KEY (codiceGiudice) REFERENCES GIUDICI(codiceGiudice),
    FOREIGN KEY (codiceCane) REFERENCES CANI(codiceCane)
);

echo "Tabella voti creata con successo!"
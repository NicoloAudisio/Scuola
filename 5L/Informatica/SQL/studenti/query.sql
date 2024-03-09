USE Studenti;

-- Elenco di tutti gli Studenti
SELECT * 
FROM Studenti;

-- Cognome e Nome di tutti gli studenti iscritti a Medicina
SELECT Cognome, Nome
FROM Studenti
WHERE Corso_di_Laurea = 'Medicina';

-- Cognome, Indirizzo e Corso di Laurea degli studenti il cui nome inizia con "Mar"
SELECT Cognome, Indirizzo, Corso_di_Laurea
FROM Studenti
WHERE Nome
LIKE 'Mar%';

-- Nome e data di nascita di tutti gli studenti con Cognome Bianchi
SELECT Nome, Data_di_Nascita
FROM Studenti
WHERE Cognome = 'Bianchi';

-- Elenco degli studenti ordinati per cognome 
SELECT *
FROM Studenti
ORDER BY Cognome;

-- Cognome, nome e indirizzo di tutti gli studenti nati tra il 1997 e 1999
SELECT Cognome, Nome, Indirizzo
FROM Studenti
WHERE YEAR(Data_di_Nascita) BETWEEN 1997 AND 1999;

-- Cognome e nome degli studenti iscritti ad Economia abitanti in Corso Italia
SELECT Cognome, Nome
FROM Studenti
WHERE Corso_di_Laurea = 'Economia' AND Indirizzo = 'Corso Italia';

-- Cognome e nome degli studenti che dovranno sostenere l'esame 1
SELECT S.Cognome, S.Nome
FROM Studenti S JOIN Esami E ON S.ID_Studente = E.ID_Studente
WHERE E.ID_Esame = 1;

-- Elenco degli studenti ordinati per Corso di Laurea e successivamente per cognome
SELECT *
FROM Studenti
ORDER BY Corso_di_Laurea, Cognome;

-- Elenco di tutti i dati della tabella Esami
SELECT *
FROM Esami;

-- Nome degli esami con credito maggiore di 9 (compreso)
SELECT Nome
FROM Esami
WHERE Credito >= 9;

-- Nome degli esami il cui orario è dalle 14 alle 16
SELECT Nome
FROM Esami
WHERE Orario >= '14:00:00' AND Orario <= '16:00:00';

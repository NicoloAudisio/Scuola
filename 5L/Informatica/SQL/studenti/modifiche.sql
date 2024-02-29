USE Studenti;

-- Inserimento dei dati:
-- Caricamento dei dati dalla tabella "Studenti"
LOAD DATA INFILE '~/Desktop/studenti/studenti.csv' 
INTO TABLE Studenti 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS 
(ID_studente, Cognome, Nome, DataNascita, Indirizzo, CorsoLaurea, Id_Esame);

-- Caricamento dei dati dalla tabella "Esami"
LOAD DATA INFILE '~/Desktop/studenti/esami.csv' 
INTO TABLE Esami 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS 
(ID_Esame, Nome_Esame, Crediti, Aula, Orario);


-- Imposta i crediti di Analisi nella tabella Esami a 15
UPDATE Esami SET Crediti = 15 WHERE Nome_Esame = 'Analisi';

-- Inserisci un nuovo record nella tabella Esami con ID_Esame=6 usando la clausola “ON DUPLICATE KEY UPDATE”. Cosa succede?
INSERT INTO Esami (ID_Esame, Nome_Esame, Crediti, Aula, Orario) 
VALUES (6, 'Analisi', 15, 'Aula 102', 'Mar-Gio 10-12')
ON DUPLICATE KEY UPDATE Nome_Esame=VALUES(Nome_Esame), Crediti=VALUES(Crediti), Aula=VALUES(Aula), Orario=VALUES(Orario);

-- Usando il comando REPLACE, modifica, nella tabella Studenti, i dati dello studente con ID_Studente=6. Cosa cambia rispetto a prima?
REPLACE INTO Studenti (ID_studente, Cognome, Nome, DataNascita, Indirizzo, CorsoLaurea, Id_Esame)
VALUES (6, 'Gialli', 'Marta', '1997-12-23', 'Corso Italia, 3', 'Medicina', 2);

-- Modifica dei dati:
-- Modifica il cognome di Verdoni Carlo in Marroni
UPDATE Studenti SET Cognome = 'Marroni' WHERE Nome = 'Carlo' AND Cognome = 'Verdoni';

-- Nella tabella Studenti, modifica tutti i record del corso di Laurea in Medicina, impostando Id_Esame=2
UPDATE Studenti SET Id_Esame = 2 WHERE CorsoLaurea = 'Medicina';

-- Modifica l’orario del corso di Impianti elettrici, sostituendolo con Mar-Gio 08-10
UPDATE Esami SET Orario = 'Mar-Gio 08-10' WHERE Nome_Esame = 'Impianti elettrici';

-- Utilizzando il comando UPDATE, incrementa i crediti di Sistemi operativi di 2
UPDATE Esami SET Crediti = Crediti + 2 WHERE Nome_Esame = 'Sistemi Operativi';

-- Modifica il record dello studente 5 inserendo gli stessi valori. Cosa succede?
-- Non succede nulla perché stai cercando di aggiornare il record con gli stessi valori.

-- Cancellazione dei Dati con e senza vincoli:
-- Prova a cancellare dalla tabella Esami il record con Id_Esame=4. È possibile? Cosa succede nelle tabelle associate?
-- Non è possibile se esiste un vincolo di integrità referenziale tra le tabelle. Se provi a cancellare il record, otterrai un errore.

-- Prova a cancellare il record di Luca Verdi dal database. È possibile? Cosa si può fare per risolvere il problema?
-- Non è possibile se esiste un vincolo di integrità referenziale. Per risolvere il problema, potresti prima aggiornare o cancellare i record correlati nella tabella figlia.

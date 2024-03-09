-- Audisio Nicolò 5L - Interrogazioni
USE Dipendenti;

-- Cognome e nome dei dipendenti che abitano a Roma
\! echo '\nCognome e nome dei dipendenti che abitano a Roma';
SELECT Nome, Cognome
FROM Impiegati
WHERE Residenza = 'Roma';

-- Cognome e Nome dei dipendenti che lavorano nel reparto Prod, ordinato per Cognome
\! echo 'C\nognome e Nome dei dipendenti che lavorano nel reparto Prod, ordinato per Cognome';
SELECT Nome, Cognome
FROM Impiegati
WHERE Dipartimento = 'Prod'
ORDER BY Cognome;

-- L’elenco di tutti i dipendenti che hanno residenza a Torino oppure Firenze
\! echo '\nL’elenco di tutti i dipendenti che hanno residenza a Torino oppure Firenze'
SELECT Nome, Cognome, Residenza
FROM Impiegati
WHERE (Residenza = 'Torino'
OR Residenza = 'Firenze');

-- Cognome, Nome e dipartimento dei dipendenti con stipendio compreso tra 2800 e 4200
\! echo '\nCognome, Nome e dipartimento dei dipendenti con stipendio compreso tra 2800 e 4200'
SELECT Nome, Cognome, Dipartimento
FROM Impiegati
WHERE (Stipendio >= 2800 
AND Stipendio <= 4200);

-- Cognome e stipendio dei dipendenti che si chiamano Mario
\! echo '\nCognome e stipendio dei dipendenti che si chiamano Mario'
SELECT Cognome, Stipendio
FROM Impiegati
WHERE Nome = 'Mario';

-- Tutti i dati della tabella dipendenti ordinati per Dipartimento ed in seguito per Cognome
\! echo '\nTutti i dati della tabella dipendenti ordinati per Dipartimento ed in seguito per Cognome'
SELECT *
FROM Impiegati
ORDER BY Dipartimento, Cognome;

-- Elenco dei Dipartimenti con sede Torino
\! echo '\nElenco dei Dipartimenti con sede Torino'
SELECT Descrizione
FROM Dipartimenti
WHERE Sede = 'Torino';

-- Sede ed uffici dei dipartimenti che iniziano per “M”
\! echo '\nSede ed uffici dei dipartimenti che iniziano per “M”'
SELECT Sede, Uffici
FROM Dipartimenti
WHERE Descrizione LIKE 'M%';

-- Dati dei dipendenti che hanno “ent” nel loro cognome
\! echo '\nDati dei dipendenti che hanno “ent” nel loro cognome'
SELECT *
FROM Impiegati
WHERE Cognome LIKE '%ent%';

-- Dati dei dipartimenti che hanno gli uffici n.12 e n.15
\! echo '\nDati dei dipartimenti che hanno gli uffici n.12 e n.15'
SELECT *
FROM Impiegati, Dipartimenti
WHERE Impiegati.Dipartimento = Dipartimenti.CodDip
AND (Dipartimenti.uffici = '12'
OR Dipartimenti.uffici = '15');

-- Cognome e Nome di tutti i dipendenti che fanno parte di Dipartimenti con sede a Milano
\! echo '\nCognome e Nome di tutti i dipendenti che fanno parte di Dipartimenti con sede a Milano'
SELECT Cognome, Nome
FROM Impiegati, Dipartimenti
WHERE Impiegati.Dipartimento = Dipartimenti.CodDip
AND (Dipartimenti.Sede = 'Milano');

-- Cognome, Nome, stipendio e Sede di tutti i dipendenti del Dipartimento Amministrazione
\! echo '\nCognome, Nome, stipendio e Sede di tutti i dipendenti del Dipartimento Amministrazione'
SELECT Cognome, Nome, Stipendio, Sede
FROM Impiegati, Dipartimenti
WHERE Impiegati.Dipartimento = Dipartimenti.CodDip
AND (Dipartimenti.Descrizione = "Amministrazione");
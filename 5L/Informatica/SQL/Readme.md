# SQL
Il DDL è il linguaggio che definisce la struttura del nostro data base, esempio di un comando che appartiene al DDL:
```
create database nomeDelDB;
```
Il seguente comando viene utilizzato per creare un database

-------------------------------------------------------------------------------------------
# Creazione di un nuovo DataBase

* Accensione server XAMPP
* Da terminale, dentro alla cartella /opt/lampp/bin digitare:
```
./mysql -u root
```
* Vedere se ci sono database esistenti
```
show databases;
```
* Creare un nuovo Database
```
create database nuovodb;
```

* Utilizzare il nuovo Database
```
use nuovodb;
```

-------------------------------------------------------------------------------------------
# File per la creazione di un DataBase
```
DROP database nuovodb;

CREATE DATABASE IF NOT EXISTS nuovodb;
SHOW DATABASES;

USE nuovodb;

CREATE TABLE Persone(
	id INT NOT NULL AUTO_INCREMENT,
	nome CHAR(45) NULL,
	cognome VARCHAR(45) NULL,
	dataDiNascita DATE NULL,
	sesso ENUM('M', 'F') NULL,
	PRIMARY KEY(id)
);

echo "Tabella creata con successo!"
```
La chiave primaria, di convenzione, va dichiarata sempre come ultimo parametro.

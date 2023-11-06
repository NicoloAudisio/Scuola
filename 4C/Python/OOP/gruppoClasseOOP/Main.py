#Audisio 4c esercizio Main
import os
import Gruppoclasse
import Studente
import Persona

# Creazione di una istanza di Gruppoclasse
nClasse = input("Inserisci il nome della classe: ")
while len(nClasse) < 1:
    nClasse = input("Inserisci il nome della classe: ")
classe = Gruppoclasse.Gruppoclasse(nClasse)

# Aggiunta di almeno 4 studenti al gruppo classe
for i in range(4):
    nomeStudente = input("Inserisci il nome dello studente: ")
    while len(nomeStudente) < 1:
        nomeStudente = input("Inserisci il nome dello studente: ")
    cognomeStudente = input("Inserisci il cognome dello studente: ")
    while len(cognomeStudente) < 1:
        cognomeStudente = input("Inserisci il cognome dello studente: ")
    etaStudente = int(input("Inserisci l'età dello studente: "))
    while etaStudente < 5 or etaStudente > 30:
        etaStudente = int(input("Inserisci l'età dello studente: "))
    votoUno = int(input("Inserisci il primo voto: "))
    while votoUno < 1 or votoUno > 10:
        votoUno = int(input("Inserisci il primo voto: "))
    votoDue = int(input("Inserisci il secondo voto: "))
    while votoDue < 1 or votoDue > 10:
        votoDue = int(input("Inserisci il secondo voto: "))
    votoTre = int(input("Inserisci il terzo voto: "))
    while votoTre < 1 or votoTre > 10:
        votoTre = int(input("Inserisci il terzo voto: "))
    votoQuattro = int(input("Inserisci il quarto voto: "))
    while votoQuattro < 1 or votoQuattro > 10:
        votoDue = int(input("Inserisci il quarto voto: "))
    alunno = Persona.Persona(nomeStudente, cognomeStudente)
    classe.aggiungi_studente(Studente.Studente(alunno, etaStudente, [votoUno, votoDue, votoTre, votoQuattro]))
    os.system("clear")

# Stampa del gruppo classe
os.system("clear")
print(classe)
continuo = input("")

# Richiesta del nome di uno studente in input e aggiunta di un voto
os.system("clear")
nome_studente = input("Inserisci il nome dello studente a cui vuoi aggiungere un voto: ")
while len(nome_studente) < 1:
    nome_studente = input("Inserisci il nome dello studente a cui vuoi aggiungere un voto: ")
for studente in classe.studenti:
    if alunno.nome == nome_studente:
        voto = int(input("Inserisci il voto da aggiungere: "))
        studente.aggiungi_voto(voto)
        break

# Stampa del gruppo classe
os.system("clear")
print(classe)
continuo = input("")

#Richiesta del nome di uno studente in input e rimozione dal gruppo classe
os.system("clear")
nome_studente = input("Inserisci il nome dello studente che si vuole cancellare dal gruppo classe: ")
while len(nome_studente) < 1:
    nome_studente = input("Inserisci il nome dello studente che si vuole cancellare dal gruppo classe: ")
nonTrovato = 0
for studente in classe.studenti:
    if alunno.nome == nome_studente:
        classe.rimuovi_studente(studente)
        print("Alunno cancellato con successo!\n")
        continuo = input("")
        break

#Stampa del gruppo classe 
os.system("clear")
print(classe)

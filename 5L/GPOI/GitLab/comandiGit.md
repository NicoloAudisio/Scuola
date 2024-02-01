# GitLab

### Comandi
* Impostazione della mail
```
git config --global user.email mail
```
* Impostazione del nome utente
```
git config --global user.name "Nome"
```

## Ambiente di lavoro di Git
* Working dir = in locale;
* Stage = ancora in locale, ma già salvato;
* Head = sul repository;

## Creazione nuovo progetto
- Create a project
- Create blank project
- Inserire nome del progetto
- Create a project

## Comandi da riga di comando
- Progetto (GitLab) > Code > Clone with HTTPS
- Creazione di una nuova cartella sulla home (da terminale):
```
mkdir GitProject
```
- Entrare nella cartella
```
cd GitProject
```
- Clonazione del progetto
```
git clone [link copiato dal "Clone with HTTPS"]
```
- Inserimento credenziali [username e password]
- Entriamo nella cartella appena creata
```
cd progettoprova25gennaio
```
- Creazione di un nuovo file
```
touch uno.txt
```
- Add dei file
```
git add .
```
- Controllo dello stato
```
git status
```
```
git add uno.txt
```
- Commit del progetto [con il -a vengono presi tutti i file; con il -m si scrive il messaggio sul commit]
```
git commit -a .-m "Aggiunto file uno.txt"
```
- Push del commit **COMANDO DA FARE PRIMA DI INIZIARE A LAVORARE**
```
git push
```
- Scaricare modifica da GitLab
```
git pull
```

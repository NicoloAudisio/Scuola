# Il Firewall

Il firewall seprare la Lan aziendale dalla WAN pubblica, **filtrando tutti i pacchetti in entrata e in uscita** da e verso una rete, **secondo delle regole prestabilite** (*Policy*).\
Un firewall **può essere fatto tramite un pc**, con *due schede di rete*: una per il mondo interno e una per il mondo esterno, tramite un software per la gestione ed un hardware dedicato per l'alta necessità di prestazioni; solitamente i router hanno un sistema di filtraggio ed esisstono router firewall appositi; esisstono invece router firewall con costi elevati che contengono tutte le regole di filtraggio al suo interno.
**Tutta la rete dipende dal firewall** e questo può diventare un collo di bottiglia per la nostra rete, però d'altro canto avendo tutto su un singolo dispositivo si ottimizza il lavoro ed è più sicuro in caso di modifica delle regole di sicurezza.

## Regole di filtraggio
CQL = Filtro dei contenuti;
QoS = Riservare banda ad alcuni servizi;
Load balancing = Due reti all'interno di una sola: bilanciamento del traffico dati e riservare del provider in caso di declino di uno dei due;

## Caratteristiche
* Strumento efficace per la sicurezza delle reti;
* Presenza di meccanismi per il controllo degli accessi;
* Possibilità di gestire le regole per la sicurezza;
* Configurazione di filtri per l'accesso dei programmi e dei computer di una rete ad Internet;
* Protezione da attacchi di tipo *ARP spoofing* (cambio il mio indirizzo MAC per avere l'identità di un'altro dispositivo), *port scanning*, *DoS*, *SQL slammer*;

## Tipologie di firewall
Ci sono tre tipologie di firewall, se ne può avere una sola, due oppure tutte e tre:
* **Application Level Firewall**: firewall che lavora al **livello applicazione**, analizza i pacchetti in entrata e in uscita basandosi sul contenuto dei pacchetti, analizza più imnformazioni e il più affidabile ma il più lento. Per esempio i **proxy** sono delle tipologie di firewall *Applicazion Level Firewall*;
* **Packet Filter Firewall**: firewall che lavora a **livello network** e su alcune funzionalità a livello trasporto, analizza il traffico in entrata e in uscita basandosi sull'indirizzo ip e si va a specificare la porta di ingresso, sono più veloci, ma meno sicuri perché non si va a controllare il conteuto del pacchetto; vanno a specificare la tipologia del servizio con la specificazione del numero di porta;
* **Stateful Packet Inspection Firewall**: firewall che lavora a **livello trasporto**, simile al *Packet Filter Firewall* però questo firewall riesce a mantenere una tabella delle sessioni di comunizione attive, qeusto permette di bloccare i messaggi duplicati che potrebbero modificare la sessione. Se un terzo soggetto prova a replicare i passi per l'ingresso in una sessione il *Stateful Packet Inspection Firewall* se ne accorge e blocca il tentativo;

## Access control List
ACL è una lista di regole che lavora tramite *white list* e *black list* e va a permettere l'ingresso all'interno di uno specifico sito.
Le regole sono eseguite in ordine, è importante l'ordine scrivendo nelle prime regole le più restrittive alle più libere

### Tipologie
Ci sono 2 tipologie di ACL:
* **Standard ACL - ACL 10**: Regola che va a filtrare i pacchetti in base sulla sorgente del pacchetto;
* **Estese ACL**: Regola che va a filtrate i paccehtti in base alla sorgente, al indirizzo di sorgente, indirizzo di destinazione e numero di porta;

### Esempio
ACL 1

* Regola 1°
* Regola 2°
* Regola 3°
* Deny all -> **pacchetto scartato**

Arriva il pacchetto, si controlla se macchia con la prima regola, in caso di match si smette con le altre regole ACL e si decide se far passare il pacchetto in base alle istruzione della regola indicata.
Se non trova nessuna regola per il controllo del pacchetto, viene messo nel *deny all* ovvero viene **scartato**; se invece non si inserisce alcune regola tutti i pacchetti vengono concessi.

---

Si vuole vietare il traffico dell'indirizzo: 192.168.10.0/24 
Si vuole consentire il traffico dell'indirizzo: 192.168.10.1:80

Per poter consentire il traffico dell'indirizzo 192.168.10.1:80 prima bisogna autorizzare il traffico dell'indirizzo con la porta e successivamente vietare il traficco specifico dell'indirizzo IP, perché se prima viene bloccata l'intera comunicazione con la rete il pacchetto, anche se della porta 80 viene automaticamente scartata. 

## Organizzazione di una rete
* WAN
* Router Firewall
* Switch2 -> Tutta la nostra rete

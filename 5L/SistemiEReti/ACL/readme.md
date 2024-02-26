# ACL

Le ACL (Access Control List) sono una lista di istruzioni da applicare alle interfacce di un router allo scopo di gestire il traffico, filtrando i pacchetti in entrata e in uscita.
Esistono due tipologie di ACL:
* **ACL STANDARD**: vengono utilizzate per bloccare o permettere il traffico da una rete o da un host specifico o per negare una suite di protocolli. L'aspetto fondamentale delle *ACL standard* è il controllo che viene esclusivamente effettuato sull'indirizzo sorgente.
* **ACL ESTESE**: forniscono una maggiore flessibilità e controllo poiché possono effettuare il controllo non solo sull'indirizzo del mittente, ma anche su quello del destinatario, su uno specifico protocollo, sul numero di porta o su altri parametri.
  
Esistono varie ragioni per decidere di adoperare le ACL:
* **Fornire un livello base di sicurezza**: si può restituire l'accesso ad una determinata rete o sottorete;
* **Limitare il traffico e aumentare la performance della rete**: si può decidere che alcuni pacchetti vengono processati prima di altri. Questo viene in particolare riferito come queeing;
* **Decidere quale tipo di traffico può essere trasmesso**: si può permettere l'invio di e-mail ed impedire allo stesso tempo il Telnet.
  
Le ACL vengono elaborate dal router in *maniera sequenziale* ovvero in base all'ordine in cui sono state inserite le varie capsule.  
Se un'istruzione non soddisfa i requisiti, passa all'istruzione successiva.  
Se un'access-list è vuota, il router sottointende **permit any**, invece, presenta anche solo una entry, il router considera un **deny any** implicito.
  
L'ordine con cui sono scritte le ACL è importante: essendo eseguite in sequenza, è necessario inserire le conizione più restrittive all'inizio e poi quelle più generiche. Sui router Cisco, da ogni ACL è identificata da un numero univoco che ne definisce il tipo:
* da 1 a 99 e da 1300 a 1999 sono le ACL standard che si riferisocno al protocollo IP;
* da 100 a 199 e da 200 a 2699 sono le ACL estese riferite a IP.
---
Per creare una **ACL Standard** su Packet Tracer:  
`Router(config)#access-list access-list-number {permit|deny} source [source wildcard] [log]`

## Sequenza di passi per la creazione delle ACL standard
1. Entrare nel CLI (Command Line Interface ) del router  
2. Entrare in modalità configurazione (configure terminal)  
3. Assegnare un nome all’access list (ad esempio per le standard 1-99)  
4. Indicare se permette o nega (permit-deny)  
5. Inserire IP dell’host o della rete  
6. Ripetere i passaggi 4-5 per inserire altre regole  
7. Assegnare la regola creata all’interfaccia(interface nome interfaccia)  
8. Assegnare la regola all’interfaccia selezionata in input-output  

### Esempio
R1>enable  
R1#configure terminal  
R1(config)#access-list 1 deny 192.168.1.1 0.0.0.0 (blocca host con IP 192.168.1.1, utilizzando la wildcard)  
R1(config)#access-list 1 permit any (permette a tutti gli altri ip di essere inoltrati)  
R1(config)#interface fastEthernet 0/1 (apertura della configurazione dell’interfaccia)  
R1(config-if)#ip access-group 1 out (assegnazione regole dell’ACL 1 all’interfaccia in modalità output)  
  
### Comandi utili:
Router# show access-lists (Visualizza le ACL presenti nel Router)  
Router# show ip access-lists (Visualizza le IP ACL presenti nel Router)  
Router# show access-lists id_ACL (Visualizza il contenuto di una ACL)  
Router# show ip interface (Visualizza il posizionamento e la direzione delle ACL)  
Router# show ip interface nome_interfaccia (Visualizza le ACL applicate ad un’interfaccia specifica  

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

# Protocollo STP

Funzioni del protoccolo STP:
* Reindirizzamento automatico in caso di guasto di un caso
* Blocca il fenomento di **Broadcast Storm**

All'interno di una rete viene individuato lo *switch root*, ovvero quello con il mac address più basso, e viene indentificato perché ogni switch manda un messaggio di *hello* ai suoi vicini e smette di mandarlo quando il suo vicino ha il valore mac address più basso del suo.
L'indirizzo di riferimento di trova all'interno della VLAN1 ed è formata da BrigdeID + indirizzo mac del dispositivo
Si può trovare andando ad esamina il *Port Status Summary* degli switch oppure da terminale, da utente amministratore (enable -> Switch#) digitando il comando:
```
show spanning-tree
```
Il terminale ritorna il seguente testo in caso di *siwtch / bridge root*
```
Priority    32769
Address     0009.7C92.1B30
This bridge is the root
Hello Time  2 sec  Max Age 20 sec

```
Invece in caso di *switch / bridge* normale
```
Priority    32769
Address     0009.7C92.1B30
Cost        19
Port        2(FastEthernet0/2)
Hello Time  2 sec  Max Age 20 sec 
```

All'interno del testo ritornato dal terminale possiamo trovare oltre alla *priority*, *address*, *port* e il *hello time* troviamo anche il **cost** che varia in base al tipo di collegamento:
* 10 mbps = 100
* 100 mbps = 19
* 1 gbps = 4
* 10 gbps = 2

## Porte STP
Il *protocollo STP* va a modificare lo stato delle porte degli switch:
* blocking : può solo ricevere le BPDU, scarta frame
* listening : topologia "attiva" determina se ci sono altri percorsi verso il root bridge
* learning : sta costruendo la tabella di bridging
* forwarding : può inviare e ricevere dati
* disable : porta disabilitata 


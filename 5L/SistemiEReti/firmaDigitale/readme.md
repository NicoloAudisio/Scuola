# La firma digitale - pag. 22-23

All'epoca si utilizzava la firma autografa, dove si recava in comune per firmare e il dipendente comunale metteva un timbro su di essa; al giorno d'oggi viene utilizzata la firma digitale, ovvero una seguenza di bit associata al dispositivo che va a garantire la paternità di colui che ha generato il documento. Ha un valore legale. Mediante la firma digitale viene associata stabilmente al documento elettronico sulla quale è apposta e ne attesta con certezza **l’integrità**, **l’autenticità** e la **non ripudiabilità**.

La firma digitale, equivalente elettronico della firma autografa su carta, è 
* **Integrità**: messaggio non modificato dopo la firma
* **Autenticità**: la firma autentica corrisponde a me
* **Non ripudiabilità**: autentica chi ha firmato, non si può smetire di aver firmato

Basata su un sistema a chiavi crittografate **asimmetriche** utilizza un certificato digitale rilasciato da un **ente certificatore** con specifiche capacità garantite dallo Stato e viene creata mediante un dispositivo con elevate caratteristiche di sicurezza, generalmente una **smart card**.

I certificatori verificano:
* Identità di un soggetto;
* Attestano tali informazioni mediante l'emissione del certificato digitale;
* Pubblicano tempestivamente la sospensione del certificato in apposite liste.

Con il certificato il destinatario ottiene la chiave pubblica sicura per verificare identità del mittente e integrità del documento.

## Formati della firma digitale
Attualmente esistono tre formati per produrre file firmati digitalmente:
* **Pkcs#7** (meglio noto come p7m): primo formato in uso sin dal 1999. Le Amministrazioni Pubbliche sono obbligate ad accettarlo;
* **PDF**;
* **XML**: il più diffuso nei settori bancari e sanitari per la gestione elettronica del flusso dei dati.

## Tipologie di firme digitali
La firma digitale può avere un valore di autentificazione e sottoscrizione:
* **Autentificazione**: come lo spid, per identificarsi online per esempio in un processo civile telematico. La CNS è una firma digitale con autentificazione. (si ha solo in versione fisica)
* **Sottoscrizione**: serve per sottoscrivere un documento con valore legale [firma vera e propria].

## Altri enti certificatori
Oltre alla firma digitale esistono altri servizi che si basano sugli enti certificatori:
* **PEC** (Posta Elettronica Certificata);
* **SPID** (Sistema Pubblico di Identità Digitale);
* **CNS** (Carta Nazionale dei Servizi).

## Proprietà fondamentali delle funzioni di crittografia di hash ideale:
deve identificare univocamente il messaggio, non è possibile che
due messaggi differenti, pur essendo simili, abbiano lo stesso valore di
hash;
* il risultato deve essere deterministico, in modo che lo stesso messaggio si traduca sempre nello stesso hash;
* deve essere semplice e veloce calcolare un valore hash da un qualunque tipo di dato;
* deve essere molto difficile o quasi impossibile generare un messaggio dal suo valore hash se non provando tutti i messaggi possibili.

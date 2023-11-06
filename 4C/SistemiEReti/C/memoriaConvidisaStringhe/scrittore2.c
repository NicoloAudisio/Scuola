//Audisio LETTORE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <string.h>
#define DIM 1024

int main(){
    key_t chiave = 1234;
    int shmid;
    char *dati, stringa[50];

    //creo la memoria e faccio il controllo
    shmid = shmget(chiave, DIM, 0666 | IPC_CREAT);
    if(shmid == -1){
        printf("\nErrore nella creazione della memoria!\n");
        exit(-1);
    }
    //collego alla memoria
    dati = (char *)shmat(shmid, NULL, 0);
    //controllo di errore
    if(dati == (char *) -1){
        printf("\nErrore nella shmat!\n");
        exit(-2);
    }
    //richiedo la stringa da inserire
    printf("Inserisci una stringa (fine per terminare): ");
    //caso fgets dove mettiamo la variabile, la dimensione e con stdin diciamo di prendere l'inserimento da tastiera
    fgets(stringa, 49, stdin);
    //gets(stringa);
    strcpy(dati, stringa);
    //gira finché non scrive "fine"
    while(strcmp(stringa, "fine\n") != 0){
        printf("Inserisci una stringa (fine per terminare): ");
        fgets(stringa, 49, stdin);
        //gets(stringa);
        strcpy(dati, stringa);
    }
    printf("Hai scelto di smettere di inserire!\n");
    //aspetto che il lettore abbia letto
    while(strcmp(dati, "chiudi") != 0){
        //serve per fare dormire il programma per 2 secondi
        sleep(2);
    }
    //distruzione di memoria
    printf("Il lettore ha letto, distruggo la memoria!\n");
    shmctl(shmid, IPC_RMID, NULL);
    printf("\nMemoria distrutta\n");

    return 0;
}
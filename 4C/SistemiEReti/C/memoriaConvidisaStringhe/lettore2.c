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
    char *dati;

    //creazione id memoria
    shmid = shmget(chiave, DIM, 0666);
    //controllo di errore
    if(shmid == -1){
        printf("\nErrore nella SHMGET!\n");
        exit(-1);
    }
    //aggangio la memoria
    dati = (char *)shmat(shmid, NULL, 0);
    printf("\nLeggo la stringa!\n");
    //stampo il contenuto in memoria
    puts(dati);
    while(strcmp(dati, "fine\n") != 0){
        puts(dati);
    }
    //finisce di leggere
    printf("\nHo letto tutti i dati in memoria!\n");
    sleep(4);
    strcpy(dati, "chiudi");

    return 0;
}
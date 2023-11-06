//Audisio memoria condivisa su più file (LETTORE)

//librerie per i processi
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

//librerie per la memoria condivisa
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>

//dichiaro la dimensione globale
#define SHM_SIZE 1024

int main(void){
    key_t chiave = 1234; //chiave di memoria e la definiamo
	int shmid; //id 
	pid_t chiSono;
    int num;
    char parola;
    char *p;

    //CREO LA MEMORIA
    shmid = shmget(chiave, SHM_SIZE, 0666);
    if(shmid == -1){
        printf("Errore nella creazione");
        exit(-1);
    }

    //PERMESSI LETTURA
    p = (char *)shmat(shmid, NULL, SHM_RDONLY);
    num = p[0];
    for(int i = 0; i < num; i++){
        printf("Parola: %d\n", p[i+1]);
    }
    p = (char *)shmat(shmid, NULL, 0);
    p[0] = -1;
    printf("\nHo letto nella memoria\n");

    return 0;
}
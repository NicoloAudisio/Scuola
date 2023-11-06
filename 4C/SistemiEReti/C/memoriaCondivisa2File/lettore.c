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
    int n, num;
    int *p;

    //CREO LA MEMORIA
    shmid = shmget(chiave, SHM_SIZE, 0666);
    if(shmid == -1){
        printf("Errore nella creazione");
        exit(-1);
    }

    //PERMESSI LETTURA
    p = (int *)shmat(shmid, NULL, SHM_RDONLY);
    if(p == -1){
        printf("Errore nella creazione della SHMAT!\n");
    }
    num = p[0];
    for(int i = 0; i < num; i++){
        printf("Numero: %d\n", p[i+1]);
    }
    p = (int *)shmat(shmid, NULL, 0);
    p[0] = -1;
    printf("\nHo letto nella memoria\n");

    return 0;
}
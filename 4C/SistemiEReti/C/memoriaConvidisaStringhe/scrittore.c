//Audisio memoria condivisa su più file (SCRITTORE)

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
    char parola;
    int n;
    char *p;

    //CREO LA MEMORIA
    shmid = shmget(chiave, SHM_SIZE, 0666 | IPC_CREAT);
    if(shmid == -1){
        printf("Errore nella creazione");
        exit(-1);
    }

    //INSERISCI NUMERI
    printf("Quante parole vuoi inserire (0-10): ");
    scanf("%d", &n);
    while(n < 0 || n > 10){
        printf("\nERRORE!\nQuanti numeri inserire (0-10): ");
        scanf("%d", &n);
    }
    p[0] = n;
    for(int i = 0; i < n; i++){
        printf("Inserisci la parola: ");
        scanf("%s", &parola);
        p[i+1] = parola;
    }

    //LETTURA E POI ELIMINAZIONE MEMORIA
    p = (char *)shmat(shmid, NULL, SHM_RDONLY);
    while(p[0] == n);
    shmctl(shmid, IPC_RMID, NULL);
    printf("\nIl lettore ha letto e la memoria è stata eliminata\n");

    return 0;
}
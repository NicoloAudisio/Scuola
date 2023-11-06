//Audisio semafori Srittore

//librerie
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/sem.h>

//dimensione memoria
#define SHM_SIZE 1024
//creo la struttura buffer
struct sembuf buffer;

void semLock(int);
void semUnlock(int);

int main(void){
	key_t keyshm = 1234, keysem = 5678;
	int shmid, semid, sem_stato;
	char *dati, stringa[20];

	shmid = shmget(keyshm, SHM_SIZE, 0666 | IPC_CREAT);
	semid = semget(keysem, 1, 0666 | IPC_CREAT);
	//controlli
	if((shmid == -1) || (semid == -1)){
		printf("Errore nella creazione della memoria o del semaforo!\n");
		exit(-1);
	}

	//setto il semaforo
	sem_stato = semctl(semid, 0, SETVAL, 1);
	dati = (char *)shmat(shmid, NULL, 0);
	while(strcmp("fine", stringa) != 0){
		if(semctl(semid, 0, GETVAL) == 1){
			semLock(semid); // blocco il semaforo
			printf("Inserisci una stringa: ");
			gets(stringa);
			if(strcmp(stringa, "fine") != 0){
				strcpy(dati, stringa);
				semUnlock(semid);
			}
		}
	}
	//distruggo il semaforo e la memoria
	sem_stato = semctl(semid, 0, IPC_RMID, 0);
	shmctl(shmid, IPC_RMID, NULL);

	return 0;
}

void semLock(int id){
	buffer.sem_num = 0;
	buffer.sem_flg = 0;
	buffer.sem_op = -1;
	if(semop(id, & buffer, 1) == 1){
		printf("\nErrore blocco del semaforo");
	} else {
		printf("\nSemaforo bloccato!\n");
	}
}

void semUnlock(int id){
	buffer.sem_num = 0;
	buffer.sem_flg = 0;
	buffer.sem_op = 1;
	if(semop(id, & buffer, 1) == 1){
		printf("\nErrore sblocco del semaforo");
	} else {
		printf("\nSemaforo sbloccato!\n");
	}
}
#include<sys/types.h>
#include<sys/ipc.h>
#include<sys/sem.h>
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<unistd.h>
#include<sys/shm.h>

struct sembuf buffer;
void semLock(int, int);
void semUnlock(int, int);

int main(){
	key_t chiaveShm=123, chiaveSem=456;
	int shmid,semid, stato, flag=0, *carrello;
	
	shmid=shmget(chiaveShm,sizeof(int)*3, 0666 | IPC_CREAT);
	semid=semget(chiaveSem, 2, 0666| IPC_CREAT);
	if((shmid ==-1) || (semid==-1)){
		printf("Errore nella creazione della memoria o del semaforo\n");
		exit(-1);
	}

	carrello = (int *)shmat(shmid, NULL, 0);
	for (int i = 0; i < 3; i ++){
		stato = semctl(semid, i, SETVAL, 1);
	}
	for(int i = 0; i < 3; i ++){
		carrello[i]=0;
	}	

	while(carrello[2] == 0){
		if(carrello[0] > 5){
			if(semctl(semid, 0, GETVAL)>0){
				semLock(semid,0);
				carrello[0] = 0;
				printf("Svuoto il primo carrello\n");
				semUnlock(semid,0);
			}
		}
		if(carrello[1] > 5){
			if(semctl(semid, 0, GETVAL)>0){
				semLock(semid,1);
				carrello[1] = 0;
				printf("Svuoto il secondo carrello\n");
				semUnlock(semid,1);
			}
		}

	}
	for(int i=0;i<2;i++){
		semctl(semid, i, IPC_RMID, 0);
	}
	shmctl(shmid, IPC_RMID, NULL);
	
	printf("Hanno scelto il primo vassoio %d persone\nHanno scelto il secondo vassoio %d persone\n", carrello[0],carrello[1]);

	printf("Chiudo la mensa.\n");

return 0;
}

void semLock(int sem_id, int id){
	buffer.sem_num=id;
	buffer.sem_flg=0;
	buffer.sem_op=-1;
	if(semop(sem_id,&buffer,1)==-1){
		printf("Errore nel blocco\n");
	}
}

void semUnlock(int sem_id, int id){
	buffer.sem_num=id;
	buffer.sem_flg=0;
	buffer.sem_op=1;
	if(semop(sem_id,&buffer,1)==-1){
		printf("Errore nel blocco\n");
	}
}

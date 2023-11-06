#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <unistd.h>
#include <sys/sem.h>
#include <sys/wait.h>
#include <time.h>

#define SHM_SIZE 1024
struct sembuf buffer;
#define MAX 50
#define MIN 20


//semafori
void sem_Lock (int sem_id);
void sem_Unlock (int sem_id);

int main (void){
	key_t sem_chiave, shm_chiave;
	int shm_id, sem_id, nCommensali = 0, *tav, nTavolo, hoscritto=0, fine=0, pid, pidstato, status, countTav1=0, countTav2=0, countTav3=0;

	sem_chiave=3234;
	shm_chiave=9786;
	shm_id = shmget(shm_chiave, SHM_SIZE, 0666);
	sem_id = semget(sem_chiave, 1, 0666);
	if (shm_id == -1 || sem_id == -1){
		printf("Errore nella gestione della memoria o dei semafori");
		exit(-1);
	}

	tav=(int *) shmat(shm_id, NULL,0);

	printf("Inserisci il numero di commensali (%d - %d): ", MAX, MIN);
	scanf("%d", &nCommensali);
	while (nCommensali < MIN || nCommensali > MAX){
		printf("Errore!\nInserisci il numero di commensali (%d - %d): ", MAX, MIN);
		scanf("%d", &nCommensali);
	}
	printf("----- MENU -----\n1. Pesce\n2.Carne\n3.Vegetariano\n----------------\n");
	for(int i=1;i<=(nCommensali*2);i=i+2){
		if((pid=fork())<0){
			printf("Errore creazione fork()\n");
			exit(-2);
		}
		if(pid==0){
			srand(getpid());
			nTavolo=rand()%(3-1+1)+1;
			while(hoscritto==0){
				if(semctl(sem_id, 0, GETVAL)==1){
					sem_Lock(sem_id);
					tav[i]=getpid();
					tav[i+1]=nTavolo;
					printf("Sono il commensale %d, ed ho scelto il tavolo n. %d\n ", getpid(), nTavolo);
					hoscritto=1;
					sem_Unlock(sem_id);
					exit(nTavolo);
				}
			}
		}
	}

	for(int i=0;i<nCommensali;i++){
	   pidstato=wait(&status);
	}

	while(fine!=1){
		if(semctl(sem_id, 0, GETVAL)==1){
			sem_Lock(sem_id);
			tav[0]=nCommensali;
			fine=1;
			sem_Unlock(sem_id);
		}
	}
	printf("Fine giornata!\n");
	return 0;
}

void sem_Lock (int sem_id){
	buffer.sem_num=0; 
	buffer.sem_flg=0;
	buffer.sem_op=-1;
	if(semop(sem_id,&buffer,1)==-1)
		printf("Errore blocco semaforo\n");
}

void sem_Unlock (int sem_id){
	buffer.sem_num=0;
	buffer.sem_flg=0;
	buffer.sem_op=1;
	if(semop(sem_id, &buffer, 1)==-1)
		printf("Errore sblocco semaforo\n");
}

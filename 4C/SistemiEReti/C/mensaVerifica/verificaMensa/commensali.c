#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <unistd.h>
#include <sys/sem.h>

#define SHM_SIZE 1024
struct sembuf buffer;

void sem_Lock (int sem_id);
void sem_Unlock (int sem_id);

int main (void){
	key_t sem_chiave, shm_chiave;
	int shm_id, sem_id, sem_stato, *tav, scrivi=0, countTav1=0, countTav2=0, countTav3=0, t1=0, t2=0, t3=0;

	sem_chiave=3234;
	shm_chiave=9786;
	shm_id = shmget(shm_chiave, SHM_SIZE, 0666 | IPC_CREAT);
	sem_id = semget(sem_chiave, 1, 0666 | IPC_CREAT);		
	if (shm_id == -1 || sem_id == -1){
  		printf("Errore nella gestione della memoria o dei semafori");
		exit(-1);
  	}
	sem_stato=semctl(sem_id, 0, SETVAL,1);
	tav=(int *) shmat(shm_id, NULL,0);

	while(scrivi==0){
		if(semctl(sem_id, 0, GETVAL)==1){
			sem_Lock(sem_id);
			if(tav[0]!=0){
				scrivi=1;
				for(int i=1;i<=(tav[0]*2);i=i+2){
					printf("Commensale: %d - Menu: %d\n", tav[i], tav[i+1]);
					if(tav[i+1] == 1){
						countTav1+=1;
						t1+=1;
					} else if(tav[i+1] == 2){
						countTav2+=1;
						t2+=1;
					} else if(tav[i+1] == 3){
						countTav3+=1;
						t3+=1;
					} else{
						printf("Qualcosa non va!\n");
					}
					while(countTav1 ==4){
						printf("Commensale %d in coda!\n", getpid());
						sleep(10);
					}
					while(countTav2 ==4){
						printf("Commensale %d in coda!\n", getpid());
						sleep(10);
					}
					while(countTav3 ==4){
						printf("Commensale %d in coda!\n", getpid());
						sleep(10);
					}
					if(tav[i+1] == 1){
						countTav1-=1;
					} else if(tav[i+1] == 2){
						countTav2-=1;
					} else if(tav[i+1] == 3){
						countTav3-=1;
					} else{
						printf("Qualcosa non va!\n");
					}
				}
			}else{
				printf("Nessuno ha ancora mangiato\n");
				sleep(2);
			}
			sem_Unlock(sem_id);
		}	
	}
	printf("%d commensali hanno preso il menù 1\n%d commensali hanno preso il menù 2\n%d commensali hanno preso il menù 3\n", t1, t2, t3);
	shmctl(shm_id, IPC_RMID, NULL);
	semctl(sem_id,0,IPC_RMID,0);
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
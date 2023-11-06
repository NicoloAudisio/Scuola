#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <unistd.h>
#include <sys/sem.h>

#define SHM_SIZE 1024  /* dimensione della shared memory = 1K */
struct sembuf buffer;

void sem_Lock (int sem_id);
void sem_Unlock (int sem_id);

int main(){
	key_t sem_chiave, shm_chiave;
	int shm_id, sem_id, sem_stato, *cassetta, possoscrivere=0, i;
	FILE *fp;
	
	sem_chiave=3234;
	shm_chiave=9786;
	shm_id = shmget(shm_chiave, SHM_SIZE, 0666 | IPC_CREAT);
	sem_id = semget(sem_chiave, 1, 0666 | IPC_CREAT);        
  
	if (shm_id == -1 || sem_id == -1){
  		printf("Errore nella gestione della memoria o dei semafori");
    	exit(-1);
  	}
	sem_stato=semctl(sem_id, 0, SETVAL,1);
	
	cassetta=(int *) shmat(shm_id, NULL,0);
	
	while(possoscrivere==0){
		if(semctl(sem_id, 0, GETVAL)==1){
			sem_Lock(sem_id);
			if(cassetta[0]!=0){		//in cassetta[0] viene messo il numero dei bambini, quando tutti i bambini hanno scritto
				possoscrivere=1;
				printf("Posso preparare la lista dei regali...\n");
				fp=fopen("lista.txt","w");
				for(i=1;i<=(cassetta[0]*2);i=i+2){
					fprintf(fp,"Bambino: %d - Regalo: %d\n",cassetta[i],cassetta[i+1]);
					printf("Bambino: %d - Regalo: %d\n",cassetta[i],cassetta[i+1]);
				}
				fclose(fp);
				printf("La lista dei regali è pronta\n");
			}else{
				printf("Non ho ancora l'elenco completo dei regali\n");
				sleep(2);
			}
			sem_Unlock(sem_id);
		}	
	}
	shmctl(shm_id, IPC_RMID, NULL);
	semctl(sem_id,0,IPC_RMID,0);
	
	return 0;
}

void sem_Lock (int sem_id){
    buffer.sem_num=0; //semaforo su cui voglio agire
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

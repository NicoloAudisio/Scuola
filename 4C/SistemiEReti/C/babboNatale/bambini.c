#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <unistd.h>
#include <sys/sem.h>
#include <sys/wait.h>

#define SHM_SIZE 1024  /* dimensione della shared memory = 1K */
struct sembuf buffer;

void sem_Lock (int sem_id);
void sem_Unlock (int sem_id);


int main(){
	key_t sem_chiave, shm_chiave;
	int shm_id, sem_id, i, hoscritto=0, regalo, bambini, *cassetta, fine=0, pid, pidstato, status;
	
	sem_chiave=3234;
	shm_chiave=9786;
	shm_id = shmget(shm_chiave, SHM_SIZE, 0666);
	sem_id = semget(sem_chiave, 1, 0666);         
  
	if (shm_id == -1 || sem_id == -1){
		printf("Errore nella gestione della memoria o dei semafori");
		exit(-1);
	}
	
	cassetta=(int *) shmat(shm_id, NULL,0);
	
	printf("Quanti bambini? ");
	scanf("%d",&bambini);
	
	for(i=1;i<=(bambini*2);i=i+2){		// ogni bambino scrive in due celle consecutive, rispettivamente pid e regalo
		if((pid=fork())<0){
			printf("Errore creazione fork()\n");
			exit(-2);
		}
		if(pid==0){
	        srand(getpid());
	        regalo=rand()%20+1;
	        while(hoscritto==0){
				if(semctl(sem_id, 0, GETVAL)==1){
					sem_Lock(sem_id);
					cassetta[i]=getpid();
					cassetta[i+1]=regalo;
					printf("Sono il bambino %d, ed ho scelto il regalo n. %d\n ", getpid(), regalo);
					hoscritto=1;
					sem_Unlock(sem_id);
					exit(regalo);
				}
	        }
	    }
	}
	
	for(i=0;i<bambini;i++){
	   pidstato=wait(&status);
	}
	printf("Tutti i bambini hanno scritto!\n");
	
	while(fine!=1){
		if(semctl(sem_id, 0, GETVAL)==1){
			sem_Lock(sem_id);
			cassetta[0]=bambini;		// metto il numero di bambini quando sono sicura che tutti abbiano scritto
			fine=1;
			sem_Unlock(sem_id);
		}
	}
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

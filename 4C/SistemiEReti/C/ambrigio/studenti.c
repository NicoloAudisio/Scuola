#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/ipc.h>
#include<sys/shm.h>
#include<unistd.h>
#include<sys/sem.h>
#include<sys/wait.h>
#include<time.h>
#define MAX 50
#define MIN 20


struct sembuf buffer;
void semLock(int, int);
void semUnlock(int, int);

int main(){
	pid_t figlio, pid;
	key_t chiaveShm=123, chiaveSem=456;
	int shmid, semid, stato, flag=0, nCommensali=0, *carrello, controllo, nStudenti;
	
	shmid = shmget(chiaveShm, sizeof(int)*3 , IPC_EXCL | 0666); 
	semid = semget(chiaveSem, 2,  IPC_EXCL | 0666);         
  
	if ((shmid == -1) || (semid == -1)){
		printf("Errore nella gestione della memoria o dei semafori");
		exit(-1);
	}
	
	carrello=(int *) shmat(shmid, NULL,0);
	
	printf("Inserisci il numero di commensali(20-50):  ");
	scanf("%d",&nCommensali);
	while(nCommensali < MIN||nCommensali > MAX){
		printf("Inserisci il numero di commensali che mangiano alla mensa (20-50):  ");
		scanf("%d",&nCommensali);
	}
		
	for(int i=0;i<nCommensali;i++){
		figlio = fork();
		if(figlio < 0){
			printf("Errore nella creazione del processo figlio!!\n");
			exit(-1);
		}
		if(figlio==0){
            flag=0;
			srand(getpid());
			nStudenti = rand()%2;
			while(flag==0){
				if(carrello[nStudenti]<5){
					if(semctl(semid, 0, GETVAL)==1){
						semLock(semid,nStudenti);
						printf("Pid: %d\nStudente: %d\n",getpid(),nStudenti);
						carrello[nStudenti]+=1;
						flag=1;
						sleep(3);
						semUnlock(semid,nStudenti);
					}
				}
			}
			exit(0);
		}
	}
	for(int i=0;i<nCommensali;i++){
		wait(&controllo);
	}
	printf("Hanno finito di mangiare!!\n");
	carrello[2]=1;
	
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

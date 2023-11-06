//Audisio 4C esercizio

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main (void){
	pid_t ChiSono, pid, pidD;
	int figli, numero, stato_wait, aspetta, somma=0, max=0, min=999, maxPid, minPid;
	
	printf("Inserisci il numero dei figli: ");
	scanf("%d", &figli);
	while(figli<=0){
		printf("Errore!\nIl numero dei figli deve essere maggiore di 0\nInserisci il numero dei figli: ");
		scanf("%d", &figli);
	}
	for(int i=0;i<figli;i++){
		if((ChiSono=fork())<0){
			printf("Errore nella creazione della fork()!\n");
			exit(-1);
		}
		if(ChiSono==0){
			srand(getpid());
			numero = rand()%(29-7+1)+7;
			exit(numero);
		}
	}
	
	for(int i=0;i<figli;i++){
		pid = wait(&stato_wait);
		max = 0;
		min = 999;
		if(stato_wait > max){
			max = stato_wait;
			printf("\nProcesso %d, numero massimo: %d\n", pid, max/256);
			maxPid = pid;
		}
		if(stato_wait < min){
			min = stato_wait;
			printf("\nProcesso %d, numero minimo: %d\n", pid, min/256);
			minPid = pid;
		}
		max = max / 256;
		min = min / 256;
	}
	
	printf("\nProcesso %d ha generato il numero massimo : %d\nProcesso %d ha generato il numero minimo: %d\n", maxPid, max, minPid, min);


return 0;
}

//Audisio 4C esercizio

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(void){
	pid_t ChiSono, pid;
	int figli, somma=0, stato_wait, numero=0;
	
	printf("Inserisci il numero di figli: ");
	scanf("%d", &figli);
	for(int i=0; i<figli; i++){
		if((ChiSono=fork())<0){
			printf("Errore nella creazione della fork()!\n");
			exit(-1);
		}
		if(ChiSono == 0){
			srand(getpid());
			numero = rand()%50+1;
			printf("Numero generato: %d\n", numero);
			exit(numero);
		}
		
	}
	
	for(int i=0;i<figli;i++){
		pid = wait(&stato_wait);
		stato_wait = stato_wait / 256;
		somma = somma + stato_wait;
	}
	
	printf("La somma è %d\n", somma);
	
	
return 0;
}

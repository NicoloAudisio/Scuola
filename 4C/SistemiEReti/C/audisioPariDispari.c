//Audisio 4C esercizio

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main (void){
	pid_t ChiSono, pid;
	int figli, numero, stato_wait, somma=0;
	
	printf("Inserisci il numero dei figli: ");
	scanf("%d", &figli);
	for(int i=0;i<figli;i++){
		if((ChiSono=fork())<0){
			printf("Errore nella creazione della fork()!\n");
			exit(-1);
		}
		if(ChiSono==0){
			srand(getpid());
			numero = rand()%(17-5+1)+5;
			if(numero%2 == 0){
				printf("\nNUMERO PARI\nIl numero è %d\n", numero);
				exit(0);
			} else {
				printf("\nNUMERO DISPARI\nIl numero è %d\n", numero);
				exit(numero);
			}
		}
	}
	
	for(int i=0;i<figli;i++){
		pid = wait(&stato_wait);
		somma = somma + (stato_wait / 256);
	}
	
	printf("\nLa somma è: %d\n", somma);


return 0;
}

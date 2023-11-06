//Audisio Nicolò

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#define MIN 3
#define MAX 5
#define C 6
#define CMIN 2
#define LUN 30
#define APP 200

int creaNum(int, int);
void insSquadre(int, char [][LUN]);
void controllo(char [], char [][LUN], int);
void infoGiocatori(int, char [][LUN], int [][C], int [][C], char [][LUN], int []);
void menoR(int, char [][LUN], int []);
void golS(int, char [][LUN], int [][C], int [][C], int []);
void golSS(int, char [][LUN], int [][C], int [][C], int [], int []);

int main() {
	int n=0, nMaglia[MAX][C], nGiocatori[C]; 
	int nGol[MAX][C], golSub[MAX];
	char stringa[MAX][LUN], cognomi[C][LUN];
	srand(time(NULL));
	
	n=creaNum(MIN,MAX);
	insSquadre(n, stringa);
	infoGiocatori(n, stringa, nMaglia, nGol, cognomi, nGiocatori);
	golS(n, stringa, nMaglia, nGol, nGiocatori);
	golSS(n, stringa, nMaglia, nGol, nGiocatori, golSub);
	menoR(n, stringa, golSub);
	return 0;
}

//crea numero
int creaNum(int min, int max) {
	return rand()%(max-min+1)+min;
}

//info squadre
void insSquadre(int N, char stringa[][LUN]) {
	int i, errore=0;
	char str[APP];
	
	system("clear");
	printf("Benvenuto nell'area organizzativa dell'Allianz Stadium\nLogin effettuato...\n\n");
	printf("Ci saranno %d squadre!\n\n", N);
	for (i=0; i<N; i++) {
		printf("Nome %d° squadra: ", i+1);
		gets(str);
		controllo(str, stringa, i);	
	}
	system("clear");
}

//controlli vari
void controllo(char str[], char stringa[][LUN], int i) {
	int l=0, e=1;
	
	while (e == 1) {
		l = strlen(str);
		if (l <= LUN) {
			strcpy(stringa[i], str);
			e= 0;
		} else {
			e= 1;
			printf("\nERRORE!\nReinserire il nome della squadra: \n");
			gets(str);
		}
	}
}

//informazioni di ogni giocatore
void infoGiocatori(int N, char stringa[][LUN], int nomeM[][C], int numG[][C], char nome[][LUN], int nGio[]) {
	int i, j, n=0;
	char str[APP];
	
	for (i=0; i<N; i++) {
		printf("Squadra: ");
		puts(stringa[i]);
		nGio[i] = creaNum(CMIN,C);
		printf("Sono presenti %d giocatori\n", nGio[i]);
		for(j=0; j<nGio[i]; j++) {
			printf("\n%d°Calciatore\n", j+1);
			printf("Cognome: ");
			gets(str);
			controllo(str, nome, j);		
			printf("Numero maglia (1-11 oppure 0=portiere): ");
			scanf("%d", &n);
			while (n < 0 || n > 11) {
				printf("ERRORE!\nNumero maglia (1-11 oppure 0 per il portiere): ");
				scanf("%d", &n);
			}
			nomeM[i][j] = n;
			n=0;
			if(nomeM[i][j] == 0) {
				printf("Numero goal subiti: ");
				scanf("%d", &n);
				while (n < 0) {
					printf("ERRORE! I gol devono essere maggiori di 0!\nNumero goal subiti: ");
					scanf("%d", &n);
				}
			} else {
				printf("Numero goal segnati: ");
				scanf("%d", &n);
				while (n < 0) {
					printf("ERRORE!\nI gol devono essere maggiori di 0!\nNumero goal segnati: ");
					scanf("%d", &n);
				}
			}
			numG[i][j] = n;
			n=0;
			while(getchar()!='\n');
		}
		system("clear");
	}
}

//gestione gol
void golS(int n, char stringa[][LUN], int nomeM[][C], int numG[][C], int nGio[]) {
	int i, j, golTot[MAX], golAtt[MAX], golCentro[MAX], golDifensori[MAX];
	
	for (i=0; i<n; i++) {
		golTot[i] = 0;
		golAtt[i] = 0;
		golCentro[i] = 0;
		golDifensori[i] = 0;
	}
	for (i=0; i<n; i++) {
		for (j=0; j<nGio[i]; j++) {
			golTot[i] = golTot[i] + numG[i][j];
			if (nomeM[i][j] >= 1 && nomeM[i][j] <= 3) {
				golDifensori[i] = golDifensori[i] + numG[i][j];
			} else if (nomeM[i][j] >= 4 && nomeM[i][j] <= 6) {
				golCentro[i] = golCentro[i] + numG[i][j];
			} else if (nomeM[i][j] >= 7 && nomeM[i][j] <= 11) {
				golAtt[i] = golAtt[i] + numG[i][j];
			}
		}
		printf("Squadra: %s   Gol segnati: %d \n\tGol difensori: %d\n\tGol centrocampisti: %d\n\tGol attaccanti: %d\n", stringa[i], golTot[i], golDifensori[i], golCentro[i], golAtt[i]);
	}
}

//gestione gol subiti
void golSS(int n, char stringa[][LUN], int nomeM[][C], int numG[][C], int nGio[], int golSub[]) {
	int i, j;
	
	for (i=0; i<n; i++) {
		golSub[i] = 0;
	}	
	for (i=0; i<n; i++) {
		for (j=0; j<nGio[i]; j++) {
			if (nomeM[i][j] == 0) {
				golSub[i] = golSub[i] + numG[i][j];
			}
		}
		printf("\n\nLa squadra %s ha subito %d goal\n", stringa[i], golSub[i]);
	}
}

//controllo squadra meno reti
void menoR(int n, char stringa[][LUN], int golSub[]) {
	int i, j, nu=10000, p=0;
	
	for (i=0; i<n; i++) {
		if (golSub[i] < nu) {
			nu = golSub[i];
			p=i;
		}
	}
	printf("\n\nLa squadra %s ha subito meno reti\n Ha subito: %d\n", stringa[p], nu);
}
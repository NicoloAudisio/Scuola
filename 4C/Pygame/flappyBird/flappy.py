#installare le librerie 
import pygame

#importazioni
import random

#inizializzare la pygame
pygame.init()

#inseriamo le immagini
sfondo = pygame.image.load('./immagini/sfondo.png')
uccello = pygame.image.load('./immagini/uccello.png')
base = pygame.image.load('./immagini/base.png')
gameover = pygame.image.load('./immagini/gameover.png')
tubo_giu = pygame.image.load('./immagini/tubo.png')
#flippo il tubo_giu
tubo_su = pygame.transform.flip(tubo_giu, False, True)

#creo lo schermo
SCHERMO = pygame.display.set_mode((288, 512))
FPS = 60
VEL_AVANZ = 3
FONT = pygame.font.SysFont('Times New Roman', 50, bold = True)
FONTSCRITTA = pygame.font.SysFont('Times New Roman', 18, bold = True)

#classe che contiene i nostri tubi, perché noi siamo informatici .cit Monge
class tubi_classe():
	def __init__(self):
		self.x = 300
		self.y = random.randint(-75, 150)
		self.punti = 0
		print("Giu: ", self.y + 210, "\nSu: ", self.y - 210)

	def avanza_e_disegna(self):
		self.x -= VEL_AVANZ
		SCHERMO.blit(tubo_giu, (self.x, self.y + 210))
		SCHERMO.blit(tubo_su, (self.x, self.y - 210))

	def collisione(self, uccello, uccelloX, uccelloY):
		tolleranza = 5
		uccello_lato_dx = uccelloX + uccello.get_width() - tolleranza
		uccello_lato_sx = uccelloX + tolleranza
		uccello_lato_su = uccelloY + tolleranza
		uccello_lato_giu = uccelloY  + uccello.get_height() - tolleranza
		
		tubi_lato_dx = self.x + tubo_giu.get_width()
		tubi_lato_sx = self.x
		tubi_lato_su = self.y + 110
		tubi_lato_giu = self.y + 210

		if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx:
			if uccello_lato_su < tubi_lato_su or uccello_lato_giu > tubi_lato_giu:
				gameOver()

	def fra_i_tubi(self, uccello, uccelloX):
		tolleranza = 5
		uccello_lato_dx = uccelloX + uccello.get_width() - tolleranza
		uccello_lato_sx = uccelloX + tolleranza
		tubi_lato_dx = self.x + tubo_giu.get_width()
		tubi_lato_sx = self.x
		if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx:
			return True

#setto le coordinate di partenza
def inizializza():
	global uccelloX, uccelloY, uccello_velY, baseX, flagq, tubi, punti, fra_i_tubi

	pygame.display.set_caption('Flappy bird - Audisio')
	icona = pygame.image.load('./immagini/uccello.png')
	pygame.display.set_icon(icona)
	uccelloX, uccelloY = 60, 150
	uccello_velY = 0
	baseX = 0
	punti = 0
	tubi = []
	fra_i_tubi = False
	tubi.append(tubi_classe())

#funzione per far comparire gli oggetti
def disegna_oggetti():
	#incollo lo sfondo
	SCHERMO.blit(sfondo, (0, 0))
	for t in tubi:
		t.avanza_e_disegna()
	SCHERMO.blit(uccello, (uccelloX, uccelloY))
	SCHERMO.blit(base, (baseX, 400))
	stampa_punti = FONT.render(str(punti), 1, (255, 255, 255))
	SCHERMO.blit(stampa_punti, (130,20))
	stampa_scritta = FONTSCRITTA.render("Chi va pian, a va san e va lontan.", 1, (0,0,0))
	SCHERMO.blit(stampa_scritta, (19, 460))

#funziona aggiorna
def aggiorna():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)

#funzione game over
def gameOver():
	flagq = False
	if flagq == True:
		pygame.quit()
	else:	
		#mettiamo la scritta
		print("Game over!")
		SCHERMO.blit(gameover, (50, 190))
		aggiorna()
		ricominciamo = False
		falgq = False
		while not ricominciamo:
			for evento in pygame.event.get():
				if(evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE):
					inizializza()
					ricominciamo = True
				if evento.type == pygame.QUIT:
					flagq = True
					ricominciamo = True
					pygame.quit()
		
inizializza()

#ciclo infinito per giocare
while True:
	punteggio = 0
	#incremento la gravità per simulare la caduta
	uccello_velY += 1
	#aggiorno la Y per far scendere l'immagine
	uccelloY = uccelloY + uccello_velY
	#importo la funziona disegna_oggetto()
	disegna_oggetti()
	aggiorna()

	#crezione degli eventi
	for evento in pygame.event.get():
		#controllo se il tasto premuto sia la freccia su
		if evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
			uccello_velY =- 10
		
		#evento di chiusura
		if evento.type == pygame.QUIT:
			pygame.quit()
	
	#faccio spostare la base
	baseX -= VEL_AVANZ
	#resetto la base per dare effetto di continuità
	if baseX < -45:
		baseX = 0
	
	if not fra_i_tubi:
		for t in tubi:
			if t.fra_i_tubi(uccello, uccelloX):
				fra_i_tubi = True
				break
	if fra_i_tubi:
		fra_i_tubi = False
		for t in tubi:
			if t.fra_i_tubi(uccello, uccelloX):
				fra_i_tubi = True
				break
		if not fra_i_tubi:
			punti += 1
			print("Punteggio: ", punti)
	#controllo per collisione
	if uccelloY > 380:
		gameOver()
	
	if tubi[-1].x < 150:
		tubi.append(tubi_classe())

	for t in tubi:
		t.collisione(uccello, uccelloX, uccelloY)
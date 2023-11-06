import pygame
# lo importo così da non usare il pygame. davanti ai comandi
from pygame.locals import *
import random

pygame.init()

# FINESTRA DI GIOCO
width = 500
height = 500
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Audisio Car Game')

# COLORI
black = (0, 0, 0)
gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)

# DIMENSIONI STRADA E STRISCE
road_width = 300
marker_width = 10
marker_height = 50

# COORDINATE CORSIA
left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]

# BORDO STRADA E STRISCE
road = (100, 0, road_width, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (395, 0, marker_width, height)

# ANIMAZIONE MOVIMENTI
lane_marker_move_y = 0

# COORDINATE DI INIZIO
player_x = 250
player_y = 400

# IMPOSTAZIONI DI GIOCO
clock = pygame.time.Clock()
fps = 120
gameover = False
speed = 2
score = 0

class Veicolo(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        # SCALA, IMPOSTAZIONE E SETTAGGIO IMMAGINI
        image_scale = 100 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        
class VeicoloGiocatore(Veicolo):
    def __init__(self, x, y):
        image = pygame.image.load('image/Audi.png')
        super().__init__(image, x, y)
        
# SPRITE
player_group = pygame.sprite.Group()
vehicle_group = pygame.sprite.Group()

# VEICOLO GIOCATORE
player = VeicoloGiocatore(player_x, player_y)
player_group.add(player)

# VEICOLI AVVERSARI
image_filenames = ['Ambulance.png', 'Black_viper.png', 'Car.png', 'Mini_truck.png', 'Police.png', 'taxi.png', 'truck.png']
vehicle_images = []
for image_filename in image_filenames:
    image = pygame.image.load('image/' + image_filename)
    vehicle_images.append(image)
    
# CRASH VEICOLO
crash = pygame.image.load('image/explosion0.png')
crash_rect = crash.get_rect()

# LOOP DI GIOCO
running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # MOVIMENTO DESTRA / SINISTRA INPUT
        if event.type == KEYDOWN:
            if event.key == K_LEFT and player.rect.center[0] > left_lane:
                player.rect.x -= 100
            elif event.key == K_RIGHT and player.rect.center[0] < right_lane:
                player.rect.x += 100  
            # CONTROLLO COLLISIONE LATERALE DOPO IL CAMBIO CORSIA
            for vehicle in vehicle_group:
                if pygame.sprite.collide_rect(player, vehicle):
                    gameover = True
                    # POSIZIONE IMMAGINE CRASH
                    if event.key == K_LEFT:
                        player.rect.left = vehicle.rect.right
                        crash_rect.center = [player.rect.left, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
                    elif event.key == K_RIGHT:
                        player.rect.right = vehicle.rect.left
                        crash_rect.center = [player.rect.right, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
            
    # DISEGNO ERBA
    screen.fill(green)
    
    # DISEGNO STRADA
    pygame.draw.rect(screen, gray, road)
    
    # DISEGNO STRADA
    pygame.draw.rect(screen, yellow, left_edge_marker)
    pygame.draw.rect(screen, yellow, right_edge_marker)
    lane_marker_move_y += speed * 2
    if lane_marker_move_y >= marker_height * 2:
        lane_marker_move_y = 0
    for y in range(marker_height * -2, height, marker_height * 2):
        pygame.draw.rect(screen, white, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        
    # DISEGNO MACCHINA GIOCATORE
    player_group.draw(screen)
    
    # DISEGNO VEICOLI AVVERSARI
    if len(vehicle_group) < 2:
        # CONTROLLO SPAZIO PER POSIZIONE VEICOLO
        add_vehicle = True
        for vehicle in vehicle_group:
            if vehicle.rect.top < vehicle.rect.height * 1.5:
                add_vehicle = False
        if add_vehicle:
            # SELEZIONE CAUSALE DELLA CORSIA
            lane = random.choice(lanes)
            # SELEZIONE CASUALE DEL VEICOLO
            image = random.choice(vehicle_images)
            vehicle = Veicolo(image, lane, height / -2)
            vehicle_group.add(vehicle)
    
    # MOVIMENTO VEICOLI
    for vehicle in vehicle_group:
        vehicle.rect.y += speed
        # RIMOZIONE VEICOLO DALLO SCHERMO DOPO CHE È PASSATO
        if vehicle.rect.top >= height:
            vehicle.kill()
            # AGGIORNAENTO PUNTEGGIO
            score += 1
            # AUMENTO LA VELOCITÀ DOPO 5 PUNTI
            if score > 0 and score % 5 == 0:
                speed += 1
    
    # DISEGNO I VEICOLI A SCHERMO
    vehicle_group.draw(screen)
    
    # DISEGNO IL PUNTEGGIO
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render('Score: ' + str(score), True, white)
    text_rect = text.get_rect()
    text_rect.center = (50, 400)
    screen.blit(text, text_rect)
    
    # CONTROLLO POSIZONE FRONTALE
    if pygame.sprite.spritecollide(player, vehicle_group, True):
        gameover = True
        crash_rect.center = [player.rect.center[0], player.rect.top]
            
    # DISEGNO GAME OVER
    if gameover:
        screen.blit(crash, crash_rect)
        pygame.draw.rect(screen, red, (0, 50, width, 100))
        font = pygame.font.Font(pygame.font.get_default_font(), 15)
        text = font.render("L'avies mac da fe tensiun Badola. Vuoi giocare di nuovo? (S o N)", True, white)
        text_rect = text.get_rect()
        text_rect.center = (width / 2, 100)
        screen.blit(text, text_rect) 
    pygame.display.update()

    # INPUT PER USCITA O CONTINUO
    while gameover:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == QUIT:
                gameover = False
                running = False
            # CONTROLLO PRESSIONE TASTO S O N
            if event.type == KEYDOWN:
                if event.key == K_s:
                    # REINIZIO GIOCO
                    gameover = False
                    speed = 2
                    score = 0
                    vehicle_group.empty()
                    player.rect.center = [player_x, player_y]
                elif event.key == K_n:
                    # USCITA
                    gameover = False
                    running = False

pygame.quit()
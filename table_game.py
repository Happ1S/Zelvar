import pygame
import random
import button
import os

FPS = 60
W, H = 1920, 1000
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
card_button = pygame.image.load('card_button.png')
cb1 = pygame.image.load('card_button.png')
cb1 = pygame.transform.scale(cb1, (cb1.get_size()[0]/4, cb1.get_size()[1]/4))
card_button = pygame.transform.scale(card_button, (card_button.get_size()[0]/4, card_button.get_size()[1]/4))
card_button = button.Button(W//2-card_button.get_size()[0]/2, H//2-card_button.get_size()[1]/2, card_button, 1)
cards = [pygame.image.load(f'sprites/{file}') for file in os.listdir('D:/python_projects/console_game/zelvar/sprites')]
cards = [pygame.transform.scale(card, (card.get_size()[0]/2, card.get_size()[1]/2)) for card in cards]
<<<<<<< HEAD
=======
cards = [pygame.image.load(f'sprites/{file}') for file in os.listdir('PATHTOWORKDIR/sprites')]
cards = [pygame.transform.scale(card, (card.get_size()[0]/1.5, card.get_size()[1]/1.5)) for card in cards]
>>>>>>> 3847c8c117079fd6c4f843746ed242d91dbb79b0
rects = list()
coords = list()
table_cards = list()
hidden_cards = list()
card_angle = list()
active_tcard = None
random.shuffle(cards)
play = True
zoom = False

while play:
    state = pygame.mouse.get_pressed()
    clock.tick(FPS)
    sc.fill((255, 255, 255))
    if card_button.draw(sc):
        table_cards.append(cards[0])
        rects.append(pygame.transform.scale(cards[0], (cards[0].get_size()[0]/2, cards[0].get_size()[1]/2)).get_rect())
        coords.append([400, 300])
        hidden_cards.append(0)
        card_angle.append(0)

        del cards[0]
    for num, tcard in enumerate(table_cards):
        sc.blit(pygame.transform.scale(tcard, (tcard.get_size()[0]/2, tcard.get_size()[1]/2)), (coords[num][0], coords[num][1]))
        rects[num].x, rects[num].y =  coords[num][0], coords[num][1]
    try:
        for num, hcard in enumerate(hidden_cards):
            if hcard != 0:
                sc.blit(pygame.transform.scale(hcard, (hcard.get_size()[0]/4, hcard.get_size()[1]/4)), (coords[num]))
    except:
        pass

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, tcard in enumerate(rects):
                    if tcard.collidepoint(event.pos):
                        active_tcard = num
            if event.button == 3:
                if active_tcard != None:
                    for num, tcard in enumerate(rects):
                        if tcard.collidepoint(event.pos):
                            if not zoom:
                                if hidden_cards[active_tcard] == 0:
                                    hidden_cards[active_tcard] = pygame.transform.rotate(pygame.image.load('card_button.png'), card_angle[active_tcard])
                                else:
                                    hidden_cards[active_tcard] = 0

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if zoom == True:
                    table_cards[active_tcard] = pygame.transform.scale(table_cards[active_tcard], (table_cards[active_tcard].get_size()[0]/2, table_cards[active_tcard].get_size()[1]/2))
                    if hidden_cards[active_tcard] != 0:
                        hidden_cards[active_tcard] = pygame.transform.scale(hidden_cards[active_tcard], (hidden_cards[active_tcard].get_size()[0]/2, hidden_cards[active_tcard].get_size()[1]/2))
                    zoom = False
                active_tcard = None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                if active_tcard != None:
                    if hidden_cards[active_tcard] != 0:
                        hidden_cards[active_tcard] = pygame.transform.rotate(hidden_cards[active_tcard], -90)
                    if card_angle[active_tcard] == -360:
                        card_angle[active_tcard] = 0 
                    card_angle[active_tcard] -= 90 
                    table_cards[active_tcard] = pygame.transform.rotate(table_cards[active_tcard], -90)
            if event.key == pygame.K_e:
                if active_tcard != None:
                    zoom = True
                    table_cards[active_tcard] = pygame.transform.scale(table_cards[active_tcard], (table_cards[active_tcard].get_size()[0]*2, table_cards[active_tcard].get_size()[1]*2))
                    if hidden_cards[active_tcard] != 0:
                        hidden_cards[active_tcard] = pygame.transform.scale(hidden_cards[active_tcard], (hidden_cards[active_tcard].get_size()[0]*2, hidden_cards[active_tcard].get_size()[1]*2))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_e:
                if active_tcard != None:
                    if zoom == True:
                        if hidden_cards[active_tcard] != 0:
                            hidden_cards[active_tcard] = pygame.transform.scale(hidden_cards[active_tcard], (hidden_cards[active_tcard].get_size()[0]/2, hidden_cards[active_tcard].get_size()[1]/2))
                        table_cards[active_tcard] = pygame.transform.scale(table_cards[active_tcard], (table_cards[active_tcard].get_size()[0]/2, table_cards[active_tcard].get_size()[1]/2))
                        zoom = False

        if event.type == pygame.MOUSEMOTION:
            if active_tcard != None:
                coords[active_tcard][0] += event.rel[0]
                coords[active_tcard][1] += event.rel[1]
        if event.type == pygame.QUIT:
            play = False
        pygame.display.update()
